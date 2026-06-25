# Класс: TGpStringInterfaceHash

**Наследник:** TObject
**Видимость:** public
**Источник:** [[GpStringHash]]
**Исходник:** `src/GpStringHash.pas`

## RAG-поисковые ключи

- kind: class
- id: GpStringHash.TGpStringInterfaceHash
- unit: GpStringHash
- structure_type: class
- source_path: src/GpStringHash.pas
- ancestor: TObject
- methods: GetInterfaces, ReleaseInterface, SetInterfaces, Create, Create, Destroy, Add, Count, Find, ForEach, GetEnumerator, HasKey, Update, ValueOf
- properties: Interfaces

## Описание

**TGpStringInterfaceHash** — это хеш-таблица с индексацией по строкам, предназначенная для хранения интерфейсов (IInterface). Класс обеспечивает быстрый поиск, добавление и обновление значений по строковому ключу, автоматически управляя подсчётом ссылок интерфейсов (_AddRef/_Release). Реализация основана на внутреннем TGpStringHash и предоставляет перебор элементов через enumerator.

---

## Иерархия наследования
TGpStringInterfaceHash ← TObject

---

## Методы

### Method: TGpStringInterfaceHash.GetInterfaces

**ID:** `GpStringHash.TGpStringInterfaceHash.GetInterfaces`
**Объявление:** `function GetInterfaces(const key: string): IInterface;`
**Видимость:** protected

Нет описания

### Method: TGpStringInterfaceHash.ReleaseInterface

**ID:** `GpStringHash.TGpStringInterfaceHash.ReleaseInterface`
**Объявление:** `procedure ReleaseInterface(item: TGpStringInterfaceHashKV);`
**Видимость:** protected

Нет описания

### Method: TGpStringInterfaceHash.SetInterfaces

**ID:** `GpStringHash.TGpStringInterfaceHash.SetInterfaces`
**Объявление:** `procedure SetInterfaces(const key: string; const value: IInterface);`
**Видимость:** protected

Нет описания

### Method: TGpStringInterfaceHash.Create

**ID:** `GpStringHash.TGpStringInterfaceHash.Create#1`
**Объявление:** `constructor Create(numItems: cardinal; canGrow: boolean = false); overload;`
**Видимость:** public

Нет описания

### Method: TGpStringInterfaceHash.Create

**ID:** `GpStringHash.TGpStringInterfaceHash.Create#2`
**Объявление:** `constructor Create(numBuckets, numItems: cardinal; canGrow: boolean = false); overload;`
**Видимость:** public

Нет описания

### Method: TGpStringInterfaceHash.Destroy

**ID:** `GpStringHash.TGpStringInterfaceHash.Destroy`
**Объявление:** `destructor Destroy; override;`
**Видимость:** public

Нет описания

### Method: TGpStringInterfaceHash.Add

**ID:** `GpStringHash.TGpStringInterfaceHash.Add`
**Объявление:** `procedure Add(const key: string; const value: IInterface);`
**Видимость:** public

Нет описания

### Method: TGpStringInterfaceHash.Count

**ID:** `GpStringHash.TGpStringInterfaceHash.Count`
**Объявление:** `function Count: integer;`
**Видимость:** public

Нет описания

### Method: TGpStringInterfaceHash.Find

**ID:** `GpStringHash.TGpStringInterfaceHash.Find`
**Объявление:** `function Find(const key: string; var value: IInterface): boolean;`
**Видимость:** public

Нет описания

### Method: TGpStringInterfaceHash.ForEach

**ID:** `GpStringHash.TGpStringInterfaceHash.ForEach`
**Объявление:** `procedure ForEach(enumerator: TGpStringInterfaceHashEnumMethod);`
**Видимость:** public

Нет описания

### Method: TGpStringInterfaceHash.GetEnumerator

**ID:** `GpStringHash.TGpStringInterfaceHash.GetEnumerator`
**Объявление:** `function GetEnumerator: TGpStringInterfaceHashEnumerator;`
**Видимость:** public

Нет описания

### Method: TGpStringInterfaceHash.HasKey

**ID:** `GpStringHash.TGpStringInterfaceHash.HasKey`
**Объявление:** `function HasKey(const key: string): boolean;`
**Видимость:** public

Нет описания

### Method: TGpStringInterfaceHash.Update

**ID:** `GpStringHash.TGpStringInterfaceHash.Update`
**Объявление:** `procedure Update(const key: string; const value: IInterface);`
**Видимость:** public

Нет описания

### Method: TGpStringInterfaceHash.ValueOf

**ID:** `GpStringHash.TGpStringInterfaceHash.ValueOf`
**Объявление:** `function ValueOf(const key: string): IInterface;`
**Видимость:** public

Нет описания


## Поля


## Свойства

### Interfaces

**Тип:** IInterface
**Видимость:** public
**Reader:** GetInterfaces
**Writer:** SetInterfaces

Нет описания


---

**Источник:** [[GpStringHash]]
