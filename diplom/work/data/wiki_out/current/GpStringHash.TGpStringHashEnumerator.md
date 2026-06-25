# Класс: TGpStringHashEnumerator

**Наследник:** TObject
**Видимость:** public
**Источник:** [[GpStringHash]]
**Исходник:** `src/GpStringHash.pas`

## RAG-поисковые ключи

- kind: class
- id: GpStringHash.TGpStringHashEnumerator
- unit: GpStringHash
- structure_type: class
- source_path: src/GpStringHash.pas
- ancestor: TObject
- methods: Create, Destroy, GetCurrent, MoveNext
- properties: Current

## Описание

**TGpStringHashEnumerator** — перечислитель для последовательного доступа к элементам хеш-таблицы `TGpStringHash`. Обеспечивает итерацию по парам (ключ-значение) типа `(string, int64)` в порядке их добавления, реализуя стандартный шаблон перечислителя с методами `MoveNext` и `GetCurrent`. Используется для перебора всех записей хеша через `for..in` циклы или метод `ForEach`.

---

## Иерархия наследования
TGpStringHashEnumerator ← TObject

---

## Методы

### Method: TGpStringHashEnumerator.Create

**ID:** `GpStringHash.TGpStringHashEnumerator.Create`
**Объявление:** `constructor Create(stringHash: TGpStringHash);`
**Видимость:** public

Нет описания

### Method: TGpStringHashEnumerator.Destroy

**ID:** `GpStringHash.TGpStringHashEnumerator.Destroy`
**Объявление:** `destructor Destroy; override;`
**Видимость:** public

Нет описания

### Method: TGpStringHashEnumerator.GetCurrent

**ID:** `GpStringHash.TGpStringHashEnumerator.GetCurrent`
**Объявление:** `function GetCurrent: TGpStringHashKV;`
**Видимость:** public

Нет описания

### Method: TGpStringHashEnumerator.MoveNext

**ID:** `GpStringHash.TGpStringHashEnumerator.MoveNext`
**Объявление:** `function MoveNext: boolean;`
**Видимость:** public

Нет описания


## Поля


## Свойства

### Current

**Тип:** TGpStringHashKV
**Видимость:** public
**Reader:** GetCurrent

Нет описания


---

**Источник:** [[GpStringHash]]
