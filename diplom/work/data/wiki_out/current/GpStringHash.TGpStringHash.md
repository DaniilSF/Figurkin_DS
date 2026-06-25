# Класс: TGpStringHash

**Наследник:** TObject
**Видимость:** public
**Источник:** [[GpStringHash]]
**Исходник:** `src/GpStringHash.pas`

## RAG-поисковые ключи

- kind: class
- id: GpStringHash.TGpStringHash
- unit: GpStringHash
- structure_type: class
- source_path: src/GpStringHash.pas
- ancestor: TObject
- methods: FindBucket, GetHashItem, GetItems, Grow, SetItems, Create, Create, Create, Destroy, Add, Count, Find, ForEach, GetEnumerator, HasKey, Update, ValueOf
- properties: HashItems, Items

## Описание

**TGpStringHash** — это предварительно выделенная хеш-таблица с строковыми ключами и значениями типа `int64`. Класс обеспечивает быстрый доступ к данным (O(1) в среднем случае) через операции добавления, поиска, обновления и проверки наличия ключа. Основная ответственность — эффективное хранение и извлечение пар "строка-целое" с поддержкой динамического роста таблицы при необходимости.

---

## Иерархия наследования
TGpStringHash ← TObject

---

## Методы

### Method: TGpStringHash.FindBucket

**ID:** `GpStringHash.TGpStringHash.FindBucket`
**Объявление:** `function FindBucket(const key: string): cardinal;`
**Видимость:** protected

Нет описания

### Method: TGpStringHash.GetHashItem

**ID:** `GpStringHash.TGpStringHash.GetHashItem`
**Объявление:** `function GetHashItem(idxHashItem: cardinal): PGpHashItem;`
**Видимость:** protected

Нет описания

### Method: TGpStringHash.GetItems

**ID:** `GpStringHash.TGpStringHash.GetItems`
**Объявление:** `function GetItems(const key: string): int64;`
**Видимость:** protected

Нет описания

### Method: TGpStringHash.Grow

**ID:** `GpStringHash.TGpStringHash.Grow`
**Объявление:** `procedure Grow;`
**Видимость:** protected

Нет описания

### Method: TGpStringHash.SetItems

**ID:** `GpStringHash.TGpStringHash.SetItems`
**Объявление:** `procedure SetItems(const key: string; const value: int64);`
**Видимость:** protected

Нет описания

### Method: TGpStringHash.Create

**ID:** `GpStringHash.TGpStringHash.Create#1`
**Объявление:** `constructor Create; overload;`
**Видимость:** public

Нет описания

### Method: TGpStringHash.Create

**ID:** `GpStringHash.TGpStringHash.Create#2`
**Объявление:** `constructor Create(numItems: cardinal; canGrow: boolean = false); overload;`
**Видимость:** public

Нет описания

### Method: TGpStringHash.Create

**ID:** `GpStringHash.TGpStringHash.Create#3`
**Объявление:** `constructor Create(numBuckets, numItems: cardinal; canGrow: boolean = false); overload;`
**Видимость:** public

Нет описания

### Method: TGpStringHash.Destroy

**ID:** `GpStringHash.TGpStringHash.Destroy`
**Объявление:** `destructor Destroy; override;`
**Видимость:** public

Нет описания

### Method: TGpStringHash.Add

**ID:** `GpStringHash.TGpStringHash.Add`
**Объявление:** `procedure Add(const key: string; value: int64);`
**Видимость:** public

Нет описания

### Method: TGpStringHash.Count

**ID:** `GpStringHash.TGpStringHash.Count`
**Объявление:** `function Count: integer;`
**Видимость:** public

Нет описания

### Method: TGpStringHash.Find

**ID:** `GpStringHash.TGpStringHash.Find`
**Объявление:** `function Find(const key: string; var value: int64): boolean;`
**Видимость:** public

Нет описания

### Method: TGpStringHash.ForEach

**ID:** `GpStringHash.TGpStringHash.ForEach`
**Объявление:** `procedure ForEach(enumerator: TGpStringHashEnumMethod);`
**Видимость:** public

Нет описания

### Method: TGpStringHash.GetEnumerator

**ID:** `GpStringHash.TGpStringHash.GetEnumerator`
**Объявление:** `function GetEnumerator: TGpStringHashEnumerator;`
**Видимость:** public

Нет описания

### Method: TGpStringHash.HasKey

**ID:** `GpStringHash.TGpStringHash.HasKey`
**Объявление:** `function HasKey(const key: string): boolean;`
**Видимость:** public

Нет описания

### Method: TGpStringHash.Update

**ID:** `GpStringHash.TGpStringHash.Update`
**Объявление:** `procedure Update(const key: string; value: int64);`
**Видимость:** public

Нет описания

### Method: TGpStringHash.ValueOf

**ID:** `GpStringHash.TGpStringHash.ValueOf`
**Объявление:** `function ValueOf(const key: string): int64;`
**Видимость:** public

Нет описания


## Поля


## Свойства

### HashItems

**Тип:** PGpHashItem
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
