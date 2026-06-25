# Класс: TGpStringTable

**Наследник:** TObject
**Видимость:** public
**Источник:** [[GpStringHash]]
**Исходник:** `src/GpStringHash.pas`

## RAG-поисковые ключи

- kind: class
- id: GpStringHash.TGpStringTable
- unit: GpStringHash
- structure_type: class
- source_path: src/GpStringHash.pas
- ancestor: TObject
- methods: CheckPointer, GetKey, GetValue, Grow, SetValue, Create, Destroy, Add, ForEach, Get, GetEnumerator
- properties: Key, Value

## Описание

**TGpStringTable** — это предварительно выделенная таблица для хранения пар «строка + int64». Класс обеспечивает простое и эффективное хранение строк с ассоциированными значениями, где позиция элемента (индекс) остаётся неизменной после добавления и может использоваться как стабильный идентификатор. Основная ответственность класса — обеспечение быстрого доступа к данным по индексу и поддержка операций добавления с возможностью динамического роста. Класс не поддерживает удаление элементов и служит основой для реализации TGpStringDictionary.

---

## Иерархия наследования
TGpStringTable ← TObject

---

## Методы

### Method: TGpStringTable.CheckPointer

**ID:** `GpStringHash.TGpStringTable.CheckPointer`
**Объявление:** `procedure CheckPointer(pData: pointer; dataSize: cardinal);`
**Видимость:** protected

Нет описания

### Method: TGpStringTable.GetKey

**ID:** `GpStringHash.TGpStringTable.GetKey`
**Объявление:** `function GetKey(index: cardinal): string;`
**Видимость:** protected

Нет описания

### Method: TGpStringTable.GetValue

**ID:** `GpStringHash.TGpStringTable.GetValue`
**Объявление:** `function GetValue(index: cardinal): int64;`
**Видимость:** protected

Нет описания

### Method: TGpStringTable.Grow

**ID:** `GpStringHash.TGpStringTable.Grow`
**Объявление:** `procedure Grow(requiredSize: cardinal);`
**Видимость:** protected

Нет описания

### Method: TGpStringTable.SetValue

**ID:** `GpStringHash.TGpStringTable.SetValue`
**Объявление:** `procedure SetValue(index: cardinal; const value: int64);`
**Видимость:** protected

Нет описания

### Method: TGpStringTable.Create

**ID:** `GpStringHash.TGpStringTable.Create`
**Объявление:** `constructor Create(initialSize: cardinal; canGrow: boolean = true);`
**Видимость:** public

Нет описания

### Method: TGpStringTable.Destroy

**ID:** `GpStringHash.TGpStringTable.Destroy`
**Объявление:** `destructor Destroy; override;`
**Видимость:** public

Нет описания

### Method: TGpStringTable.Add

**ID:** `GpStringHash.TGpStringTable.Add`
**Объявление:** `function Add(const key: string; value: int64): cardinal;`
**Видимость:** public

Нет описания

### Method: TGpStringTable.ForEach

**ID:** `GpStringHash.TGpStringTable.ForEach`
**Объявление:** `procedure ForEach(enumerator: TGpStringTableEnumMethod);`
**Видимость:** public

Нет описания

### Method: TGpStringTable.Get

**ID:** `GpStringHash.TGpStringTable.Get`
**Объявление:** `procedure Get(index: cardinal; var key: string; var value: int64);`
**Видимость:** public

Нет описания

### Method: TGpStringTable.GetEnumerator

**ID:** `GpStringHash.TGpStringTable.GetEnumerator`
**Объявление:** `function GetEnumerator: TGpStringTableEnumerator;`
**Видимость:** public

Нет описания


## Поля


## Свойства

### Key

**Тип:** string
**Видимость:** public
**Reader:** GetKey

Нет описания

### Value

**Тип:** int64
**Видимость:** public
**Reader:** GetValue
**Writer:** SetValue

Нет описания


---

**Источник:** [[GpStringHash]]
