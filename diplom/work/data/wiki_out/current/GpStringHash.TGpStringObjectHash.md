# Класс: TGpStringObjectHash

**Наследник:** TObject
**Видимость:** public
**Источник:** [[GpStringHash]]
**Исходник:** `src/GpStringHash.pas`

## RAG-поисковые ключи

- kind: class
- id: GpStringHash.TGpStringObjectHash
- unit: GpStringHash
- structure_type: class
- source_path: src/GpStringHash.pas
- ancestor: TObject
- methods: FreeObject, GetObjects, SetObjects, Create, Create, Destroy, Add, Count, Find, ForEach, GetEnumerator, HasKey, Update, ValueOf
- properties: Objects

## Описание

**TGpStringObjectHash** — хеш-таблица с строковыми ключами и значениями типа `TObject`. Класс обеспечивает быстрый доступ к объектам по имени, храня указатели внутри внутреннего `TGpStringHash`. Основная ответственность — управление коллекцией объектов с автоматическим уничтожением при необходимости (флаг `OwnsObjects`).

---

## Иерархия наследования
TGpStringObjectHash ← TObject

---

## Методы

### Method: TGpStringObjectHash.FreeObject

**ID:** `GpStringHash.TGpStringObjectHash.FreeObject`
**Объявление:** `procedure FreeObject(item: TGpStringObjectHashKV);`
**Видимость:** protected

Нет описания

### Method: TGpStringObjectHash.GetObjects

**ID:** `GpStringHash.TGpStringObjectHash.GetObjects`
**Объявление:** `function GetObjects(const key: string): TObject;`
**Видимость:** protected

Нет описания

### Method: TGpStringObjectHash.SetObjects

**ID:** `GpStringHash.TGpStringObjectHash.SetObjects`
**Объявление:** `procedure SetObjects(const key: string; const value: TObject);`
**Видимость:** protected

Нет описания

### Method: TGpStringObjectHash.Create

**ID:** `GpStringHash.TGpStringObjectHash.Create#1`
**Объявление:** `constructor Create(numItems: cardinal; ownsObjects: boolean = true; canGrow: boolean = false); overload;`
**Видимость:** public

Нет описания

### Method: TGpStringObjectHash.Create

**ID:** `GpStringHash.TGpStringObjectHash.Create#2`
**Объявление:** `constructor Create(numBuckets, numItems: cardinal; ownsObjects: boolean = true; canGrow: boolean = false); overload;`
**Видимость:** public

Нет описания

### Method: TGpStringObjectHash.Destroy

**ID:** `GpStringHash.TGpStringObjectHash.Destroy`
**Объявление:** `destructor Destroy; override;`
**Видимость:** public

Нет описания

### Method: TGpStringObjectHash.Add

**ID:** `GpStringHash.TGpStringObjectHash.Add`
**Объявление:** `procedure Add(const key: string; value: TObject);`
**Видимость:** public

Нет описания

### Method: TGpStringObjectHash.Count

**ID:** `GpStringHash.TGpStringObjectHash.Count`
**Объявление:** `function Count: integer;`
**Видимость:** public

Нет описания

### Method: TGpStringObjectHash.Find

**ID:** `GpStringHash.TGpStringObjectHash.Find`
**Объявление:** `function Find(const key: string; var value: TObject): boolean;`
**Видимость:** public

Нет описания

### Method: TGpStringObjectHash.ForEach

**ID:** `GpStringHash.TGpStringObjectHash.ForEach`
**Объявление:** `procedure ForEach(enumerator: TGpStringObjectHashEnumMethod);`
**Видимость:** public

Нет описания

### Method: TGpStringObjectHash.GetEnumerator

**ID:** `GpStringHash.TGpStringObjectHash.GetEnumerator`
**Объявление:** `function GetEnumerator: TGpStringObjectHashEnumerator;`
**Видимость:** public

Нет описания

### Method: TGpStringObjectHash.HasKey

**ID:** `GpStringHash.TGpStringObjectHash.HasKey`
**Объявление:** `function HasKey(const key: string): boolean;`
**Видимость:** public

Нет описания

### Method: TGpStringObjectHash.Update

**ID:** `GpStringHash.TGpStringObjectHash.Update`
**Объявление:** `procedure Update(const key: string; value: TObject);`
**Видимость:** public

Нет описания

### Method: TGpStringObjectHash.ValueOf

**ID:** `GpStringHash.TGpStringObjectHash.ValueOf`
**Объявление:** `function ValueOf(const key: string): TObject;`
**Видимость:** public

Нет описания


## Поля


## Свойства

### Objects

**Тип:** TObject
**Видимость:** public
**Reader:** GetObjects
**Writer:** SetObjects

Нет описания


---

**Источник:** [[GpStringHash]]
