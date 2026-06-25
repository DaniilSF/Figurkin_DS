#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
import io
import json
import re
import tokenize
from dataclasses import dataclass
from datetime import datetime
from typing import Any, Dict, List, Optional


PH_PREFIX = "__PH__"
PH_SUFFIX = "__"

PLACEHOLDER_RE = re.compile(r"\$[A-Za-z_][A-Za-z0-9_]*")


@dataclass
class PatternTok:
    """Элемент шаблона: LIT — точное совпадение, PH — плейсхолдер под любой NAME."""
    kind: str  # "LIT" или "PH"
    ttype: Optional[int] = None
    tstr: Optional[str] = None
    ph_name: Optional[str] = None


@dataclass
class MatchSpan:
    """Диапазон строк в исходнике (1-based), где найдено совпадение."""
    start_line: int
    end_line: int


IGNORE_TOKEN_TYPES = {
    tokenize.ENCODING,
    tokenize.NL,
    tokenize.NEWLINE,
    tokenize.INDENT,
    tokenize.DEDENT,
    tokenize.COMMENT,
    tokenize.ENDMARKER,
}


def read_text(path: str) -> str:
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def write_text(path: str, text: str) -> None:
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)


def leading_ws(s: str) -> str:
    """Возвращает отступ (пробелы/табуляции) в начале строки."""
    return s[: len(s) - len(s.lstrip(" \t"))]


def tokenize_python(code: str) -> List[tokenize.TokenInfo]:
    """Токенизация Python-кода с отбрасыванием «шума» (переносы/отступы/комментарии)."""
    out: List[tokenize.TokenInfo] = []
    reader = io.StringIO(code).readline
    for tok in tokenize.generate_tokens(reader):
        if tok.type in IGNORE_TOKEN_TYPES:
            continue
        out.append(tok)
    return out


def preprocess_placeholders(pattern: str) -> str:
    """Заменяет $NAME на валидный идентификатор Python: __PH__NAME__."""
    def repl(m: re.Match) -> str:
        name = m.group(0)[1:]
        return f"{PH_PREFIX}{name}{PH_SUFFIX}"

    return PLACEHOLDER_RE.sub(repl, pattern)


def compile_pattern(find_text: str) -> List[PatternTok]:
    """Компилирует find-шаблон: __PH__X__ -> плейсхолдер, остальные -> литералы."""
    pre = preprocess_placeholders(find_text)
    toks = tokenize_python(pre)

    pat: List[PatternTok] = []
    for t in toks:
        if t.type == tokenize.NAME and t.string.startswith(PH_PREFIX) and t.string.endswith(PH_SUFFIX):
            name = t.string[len(PH_PREFIX) : -len(PH_SUFFIX)]
            pat.append(PatternTok(kind="PH", ph_name=name))
        else:
            pat.append(PatternTok(kind="LIT", ttype=t.type, tstr=t.string))
    return pat


def find_matches_in_tokens(
    src_tokens: List[tokenize.TokenInfo],
    pattern: List[PatternTok],
) -> List[MatchSpan]:
    """Поиск совпадений шаблона по токенам исходника (скользящее окно)."""
    if not pattern:
        return []

    matches: List[MatchSpan] = []
    n = len(src_tokens)
    m = len(pattern)
    if m > n:
        return matches

    for i in range(0, n - m + 1):
        ok = True
        for j in range(m):
            pt = pattern[j]
            st = src_tokens[i + j]

            if pt.kind == "PH":
                if st.type != tokenize.NAME:
                    ok = False
                    break
            else:
                if st.type != pt.ttype or st.string != pt.tstr:
                    ok = False
                    break

        if ok:
            window = src_tokens[i : i + m]
            start_line = min(t.start[0] for t in window)
            end_line = max(t.end[0] for t in window)
            matches.append(MatchSpan(start_line=start_line, end_line=end_line))

    return matches


def detect_start_insertion_line(lines: List[str]) -> int:
    """Вставка в начало: пропускаем shebang и coding cookie."""
    idx = 0
    if idx < len(lines) and lines[idx].startswith("#!"):
        idx += 1

    enc_re = re.compile(r"coding[:=]\s*[-\w.]+")
    if idx < len(lines) and enc_re.search(lines[idx]):
        idx += 1
    elif idx == 1 and idx < len(lines) and enc_re.search(lines[idx]):
        idx += 1

    return idx


def make_commented_block_with_id(rule_id: str, text: str, indent: str) -> List[str]:
    """
    Делает блок комментариев:
      {indent}#id <rule_id>
      {indent}# <строка 1>
      ...
    """
    out: List[str] = []
    out.append(f"{indent}#id {rule_id}\n")

    for line in text.splitlines():
        if line.strip() == "":
            out.append(f"{indent}#\n")
        else:
            out.append(f"{indent}# {line}\n")

    if len(out) == 1:
        out.append(f"{indent}#\n")

    return out


@dataclass
class InsertOp:
    """Операция вставки: позиция строки + блок строк + номер для устойчивого порядка."""
    line_index: int
    block_lines: List[str]
    seq: int


@dataclass
class ReportEntry:
    """Запись отчёта для одной вставки (позиции берём по исходнику, до вставок)."""
    rule_id: str
    pattern_type: str
    comment: str
    where: str  # start / after
    start_line: Optional[int] = None
    end_line: Optional[int] = None


def load_rules(path: str) -> List[Dict[str, Any]]:
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
    if not isinstance(data, list):
        raise ValueError("Корневой элемент JSON должен быть списком правил")
    return data


def rule_find_text(rule: Dict[str, Any]) -> str:
    f = rule.get("find", "")
    if isinstance(f, dict):
        return str(f.get("pattern", ""))
    return str(f or "")


def build_ops_and_report(
    rules: List[Dict[str, Any]],
    src_text: str
) -> (List[InsertOp], List[ReportEntry]):
    lines = src_text.splitlines(keepends=True)
    src_tokens = tokenize_python(src_text)

    ops: List[InsertOp] = []
    report: List[ReportEntry] = []
    seq = 0

    for rule in rules:
        rule_id = str(rule.get("id", "")).strip() or "UNKNOWN"
        pattern_type = str(rule.get("pattern_type", "")).strip()
        comment = str(rule.get("comment", "")).strip()

        insert = rule.get("insert", {}) or {}
        where = str(insert.get("where", "")).strip().lower()
        ins_text = str(insert.get("text", "") or "")

        ftxt = rule_find_text(rule)

        if where == "start":
            idx = detect_start_insertion_line(lines)
            block = make_commented_block_with_id(rule_id, ins_text, indent="")
            ops.append(InsertOp(line_index=idx, block_lines=block, seq=seq))
            report.append(ReportEntry(
                rule_id=rule_id,
                pattern_type=pattern_type,
                comment=comment,
                where="start",
                start_line=None,
                end_line=None
            ))
            seq += 1
            continue

        if where != "after":
            continue

        if not ftxt.strip():
            continue

        pattern = compile_pattern(ftxt)
        matches = find_matches_in_tokens(src_tokens, pattern)

        for ms in matches:
            start_line_idx = ms.start_line - 1
            indent = ""
            if 0 <= start_line_idx < len(lines):
                indent = leading_ws(lines[start_line_idx])

            insert_at = ms.end_line  # after => после end_line
            block = make_commented_block_with_id(rule_id, ins_text, indent=indent)
            ops.append(InsertOp(line_index=insert_at, block_lines=block, seq=seq))
            report.append(ReportEntry(
                rule_id=rule_id,
                pattern_type=pattern_type,
                comment=comment,
                where="after",
                start_line=ms.start_line,
                end_line=ms.end_line
            ))
            seq += 1

    return ops, report


def apply_ops(src_text: str, ops: List[InsertOp]) -> str:
    """Вставки применяем снизу вверх, чтобы индексы строк не «поехали»."""
    lines = src_text.splitlines(keepends=True)
    ops_sorted = sorted(ops, key=lambda o: (o.line_index, o.seq), reverse=True)

    for op in ops_sorted:
        idx = max(0, min(op.line_index, len(lines)))
        lines[idx:idx] = op.block_lines

    return "".join(lines)


def write_report_txt(report_entries: List[ReportEntry], report_path: str = "report.txt") -> None:
    """
    Пишем отчёт только по тем правилам, которые реально сработали (т.е. есть записи).
    Без списка несработавших правил.
    """
    # Сгруппируем по rule_id, чтобы не повторять comment/тип тысячу раз
    grouped: Dict[str, Dict[str, Any]] = {}
    for e in report_entries:
        g = grouped.setdefault(e.rule_id, {
            "rule_id": e.rule_id,
            "pattern_type": e.pattern_type,
            "comment": e.comment,
            "count": 0,
            "items": []
        })
        g["count"] += 1
        if e.where == "start":
            g["items"].append("вставка: start (в начало файла)")
        else:
            g["items"].append(f"совпадение: строки {e.start_line}-{e.end_line}, вставка after (после строки {e.end_line})")

    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    lines: List[str] = []
    lines.append(f"ОТЧЁТ О ВСТАВКАХ (report.txt)\n")
    lines.append(f"Время: {now}\n")
    lines.append(f"Срабатываний (вставок) всего: {len(report_entries)}\n")
    lines.append("\n")

    # Пишем только правила, которые реально сработали
    for rule_id in sorted(grouped.keys()):
        g = grouped[rule_id]
        lines.append(f"ID: {g['rule_id']}\n")
        if g["pattern_type"]:
            lines.append(f"Тип: {g['pattern_type']}\n")
        if g["comment"]:
            lines.append(f"Комментарий правила: {g['comment']}\n")
        lines.append(f"Количество вставок: {g['count']}\n")
        lines.append("Где:\n")
        for item in g["items"]:
            lines.append(f"  - {item}\n")
        lines.append("\n")

    write_text(report_path, "".join(lines))


def main() -> None:
    ap = argparse.ArgumentParser(
        description="Прототип: вставка комментариев в Python-код по JSON-правилам и токен-шаблонам."
    )
    ap.add_argument("rules_json", help="Путь к JSON с правилами (новый формат)")
    ap.add_argument("input_file", help="Путь к входному .py файлу")
    ap.add_argument("output_file", help="Путь к выходному .py файлу")
    args = ap.parse_args()

    rules = load_rules(args.rules_json)
    src_text = read_text(args.input_file)

    ops, report_entries = build_ops_and_report(rules, src_text)
    out_text = apply_ops(src_text, ops)

    write_text(args.output_file, out_text)
    write_report_txt(report_entries, report_path="report.txt")

    print(f"Готово. Вставлено блоков: {len(ops)}. Результат: '{args.output_file}'. Отчёт: 'report.txt'.")


if __name__ == "__main__":
    main()
