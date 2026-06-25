# Класс: TGpStringObjectHashKV

**Наследник:** TObject
**Видимость:** public
**Источник:** [[GpStringHash]]
**Исходник:** `src/GpStringHash.pas`

## RAG-поисковые ключи

- kind: class
- id: GpStringHash.TGpStringObjectHashKV
- unit: GpStringHash
- structure_type: class
- source_path: src/GpStringHash.pas
- ancestor: TObject
- properties: Key, Value

## Описание

**TGpStringObjectHashKV** — вспомогательный класс, представляющий внешнее представление элемента хеш-таблицы в виде пары «ключ-значение». Используется при перечислении элементов `TGpStringObjectHash`. Хранит строковый ключ (`Key`) и объект (`Value` типа `TObject`). Служит контейнером для доступа к данным при итерации по хеш-таблице объектов.

---

## Иерархия наследования
TGpStringObjectHashKV ← TObject

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

**Тип:** TObject
**Видимость:** public
**Reader:** kvValue
**Writer:** kvValue

Нет описания


---

**Источник:** [[GpStringHash]]
