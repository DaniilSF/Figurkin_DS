# Класс: TGpStringTableKV

**Наследник:** TObject
**Видимость:** public
**Источник:** [[GpStringHash]]
**Исходник:** `src/GpStringHash.pas`

## RAG-поисковые ключи

- kind: class
- id: GpStringHash.TGpStringTableKV
- unit: GpStringHash
- structure_type: class
- source_path: src/GpStringHash.pas
- ancestor: TObject
- properties: Key, Value

## Описание

**TGpStringTableKV** — вспомогательный класс, представляющий элемент хеш-таблицы в виде пары «ключ-значение» (string, int64). Используется в качестве внешнего представления записей при перечислении (enumeration) данных в TGpStringTable. Класс предоставляет доступ к ключу и значению через свойства Key и Value, обеспечивая удобный способ получения данных при итерации по таблице.

---

## Иерархия наследования
TGpStringTableKV ← TObject

---

## Методы


## Поля


## Свойства

### Key

**Тип:** string
**Видимость:** public
**Reader:** kvKey
**Writer:** kvKey

Нет описания

### Value

**Тип:** int64
**Видимость:** public
**Reader:** kvValue
**Writer:** kvValue

Нет описания


---

**Источник:** [[GpStringHash]]
