# Класс: TGpStringDictionaryEnumerator

**Наследник:** TObject
**Видимость:** public
**Источник:** [[GpStringHash]]
**Исходник:** `src/GpStringHash.pas`

## RAG-поисковые ключи

- kind: class
- id: GpStringHash.TGpStringDictionaryEnumerator
- unit: GpStringHash
- structure_type: class
- source_path: src/GpStringHash.pas
- ancestor: TObject
- methods: Create, Destroy, GetCurrent, MoveNext
- properties: Current

## Описание

**TGpStringDictionaryEnumerator**

Класс-перечислитель для итерации по элементам `TGpStringDictionary`. Реализует паттерн перечисления с методами `GetCurrent`, `MoveNext` и свойством `Current`, возвращающим объекты типа `TGpStringDictionaryKV` (содержащие индекс, ключ и значение). Обеспечивает перебор элементов словаря в порядке их добавления (insertion order).

---

## Иерархия наследования
TGpStringDictionaryEnumerator ← TObject

---

## Методы

### Method: TGpStringDictionaryEnumerator.Create

**ID:** `GpStringHash.TGpStringDictionaryEnumerator.Create`
**Объявление:** `constructor Create(pItems: PGpTableHashItemArr; firstBucket: cardinal; stringTable: TGpStringTable);`
**Видимость:** public

Нет описания

### Method: TGpStringDictionaryEnumerator.Destroy

**ID:** `GpStringHash.TGpStringDictionaryEnumerator.Destroy`
**Объявление:** `destructor Destroy; override;`
**Видимость:** public

Нет описания

### Method: TGpStringDictionaryEnumerator.GetCurrent

**ID:** `GpStringHash.TGpStringDictionaryEnumerator.GetCurrent`
**Объявление:** `function GetCurrent: TGpStringDictionaryKV;`
**Видимость:** public

Нет описания

### Method: TGpStringDictionaryEnumerator.MoveNext

**ID:** `GpStringHash.TGpStringDictionaryEnumerator.MoveNext`
**Объявление:** `function MoveNext: boolean;`
**Видимость:** public

Нет описания


## Поля


## Свойства

### Current

**Тип:** TGpStringDictionaryKV
**Видимость:** public
**Reader:** GetCurrent

Нет описания


---

**Источник:** [[GpStringHash]]
