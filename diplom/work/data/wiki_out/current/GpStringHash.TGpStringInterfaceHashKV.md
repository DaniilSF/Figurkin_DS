# Класс: TGpStringInterfaceHashKV

**Наследник:** TObject
**Видимость:** public
**Источник:** [[GpStringHash]]
**Исходник:** `src/GpStringHash.pas`

## RAG-поисковые ключи

- kind: class
- id: GpStringHash.TGpStringInterfaceHashKV
- unit: GpStringHash
- structure_type: class
- source_path: src/GpStringHash.pas
- ancestor: TObject
- properties: Key, Value

## Описание

**TGpStringInterfaceHashKV** — класс-контейнер для представления элемента хеш-таблицы внешнего интерфейса. Хранит пару «ключ-значение», где ключ представлен строкой (`string`), а значение — интерфейсом (`IInterface`). Используется при перечислении элементов `TGpStringInterfaceHash` для предоставления доступа к отдельным записям хеш-коллекции.

---

## Иерархия наследования
TGpStringInterfaceHashKV ← TObject

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

**Тип:** IInterface
**Видимость:** public
**Reader:** kvValue
**Writer:** kvValue

Нет описания


---

**Источник:** [[GpStringHash]]
