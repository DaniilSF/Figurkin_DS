# Класс: TGpStringDictionary

**Наследник:** TObject
**Видимость:** public
**Источник:** [[GpStringHash]]
**Исходник:** `src/GpStringHash.pas`

## RAG-поисковые ключи

- kind: class
- id: GpStringHash.TGpStringDictionary
- unit: GpStringHash
- structure_type: class
- source_path: src/GpStringHash.pas
- ancestor: TObject
- methods: FindBucket, GetHashItem, GetItems, Grow, LinkAtTail, SetItems, Create, Destroy, Add, Count, Find, ForEach, Get, GetEnumerator, HasKey, Update, ValueOf
- properties: HashItems, Items

## Описание

**TGpStringDictionary** — хеш-словарь для хранения триплетов `<строка, cardinal, int64>`. Класс обеспечивает быстрый доступ к данным по строковому ключу с использованием хеш-таблицы, а также поддерживает перечисление элементов в порядке их добавления. Основная ответственность класса — эффективное управление ассоциативным массивом строковых ключей с целочисленными значениями с предсказуемым поведением при обходе коллекции.

---

## Иерархия наследования
TGpStringDictionary ← TObject

---

## Методы

### Method: TGpStringDictionary.FindBucket

**ID:** `GpStringHash.TGpStringDictionary.FindBucket`
**Объявление:** `function FindBucket(const key: string): cardinal;`
**Видимость:** protected

Нет описания

### Method: TGpStringDictionary.GetHashItem

**ID:** `GpStringHash.TGpStringDictionary.GetHashItem`
**Объявление:** `function GetHashItem(idxHashItem: cardinal): PGpTableHashItem;`
**Видимость:** protected

Нет описания

### Method: TGpStringDictionary.GetItems

**ID:** `GpStringHash.TGpStringDictionary.GetItems`
**Объявление:** `function GetItems(const key: string): int64;`
**Видимость:** protected

Нет описания

### Method: TGpStringDictionary.Grow

**ID:** `GpStringHash.TGpStringDictionary.Grow`
**Объявление:** `procedure Grow;`
**Видимость:** protected

Нет описания

### Method: TGpStringDictionary.LinkAtTail

**ID:** `GpStringHash.TGpStringDictionary.LinkAtTail`
**Объявление:** `procedure LinkAtTail(bucket: PGpTableHashItem; bucketIdx: cardinal);`
**Видимость:** protected

Нет описания

### Method: TGpStringDictionary.SetItems

**ID:** `GpStringHash.TGpStringDictionary.SetItems`
**Объявление:** `procedure SetItems(const key: string; const value: int64);`
**Видимость:** protected

Нет описания

### Method: TGpStringDictionary.Create

**ID:** `GpStringHash.TGpStringDictionary.Create`
**Объявление:** `constructor Create(initialArraySize: cardinal);`
**Видимость:** public

Нет описания

### Method: TGpStringDictionary.Destroy

**ID:** `GpStringHash.TGpStringDictionary.Destroy`
**Объявление:** `destructor Destroy; override;`
**Видимость:** public

Нет описания

### Method: TGpStringDictionary.Add

**ID:** `GpStringHash.TGpStringDictionary.Add`
**Объявление:** `function Add(const key: string; value: int64): cardinal;`
**Видимость:** public

Нет описания

### Method: TGpStringDictionary.Count

**ID:** `GpStringHash.TGpStringDictionary.Count`
**Объявление:** `function Count: integer;`
**Видимость:** public

Нет описания

### Method: TGpStringDictionary.Find

**ID:** `GpStringHash.TGpStringDictionary.Find`
**Объявление:** `function Find(const key: string; var index: cardinal; var value: int64): boolean;`
**Видимость:** public

Нет описания

### Method: TGpStringDictionary.ForEach

**ID:** `GpStringHash.TGpStringDictionary.ForEach`
**Объявление:** `procedure ForEach(enumerator: TGpStringDictionaryEnumMethod);`
**Видимость:** public

Нет описания

### Method: TGpStringDictionary.Get

**ID:** `GpStringHash.TGpStringDictionary.Get`
**Объявление:** `procedure Get(index: cardinal; var key: string; var value: int64);`
**Видимость:** public

Нет описания

### Method: TGpStringDictionary.GetEnumerator

**ID:** `GpStringHash.TGpStringDictionary.GetEnumerator`
**Объявление:** `function GetEnumerator: TGpStringDictionaryEnumerator;`
**Видимость:** public

Нет описания

### Method: TGpStringDictionary.HasKey

**ID:** `GpStringHash.TGpStringDictionary.HasKey`
**Объявление:** `function HasKey(const key: string): boolean;`
**Видимость:** public

Нет описания

### Method: TGpStringDictionary.Update

**ID:** `GpStringHash.TGpStringDictionary.Update`
**Объявление:** `procedure Update(const key: string; value: int64);`
**Видимость:** public

Нет описания

### Method: TGpStringDictionary.ValueOf

**ID:** `GpStringHash.TGpStringDictionary.ValueOf`
**Объявление:** `function ValueOf(const key: string): int64;`
**Видимость:** public

Нет описания


## Поля


## Свойства

### HashItems

**Тип:** PGpTableHashItem
**Видимость:** protected
**Reader:** GetHashItem

Нет описания

### Items

**Тип:** int64
**Видимость:** public
**Reader:** GetItems
**Writer:** SetItems

Нет описания


---

**Источник:** [[GpStringHash]]
