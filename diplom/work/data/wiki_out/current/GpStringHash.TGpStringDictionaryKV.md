# Класс: TGpStringDictionaryKV

**Наследник:** TObject
**Видимость:** public
**Источник:** [[GpStringHash]]
**Исходник:** `src/GpStringHash.pas`

## RAG-поисковые ключи

- kind: class
- id: GpStringHash.TGpStringDictionaryKV
- unit: GpStringHash
- structure_type: class
- source_path: src/GpStringHash.pas
- ancestor: TObject
- properties: Index, Key, Value

## Описание

**TGpStringDictionaryKV** — вспомогательный класс для представления элементов словаря `TGpStringDictionary` во внешнем интерфейсе. Хранит триплет данных: индекс элемента в строковой таблице (`Index`), строковый ключ (`Key`) и целочисленное значение (`Value`). Используется перечислителями и методами обратного вызова для передачи информации о найденных элементах.

---

## Иерархия наследования
TGpStringDictionaryKV ← TObject

---

## Методы


## Поля


## Свойства

### Index

**Тип:** Cardinal
**Видимость:** public
**Reader:** kvIndex
**Writer:** kvIndex

Нет описания

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
