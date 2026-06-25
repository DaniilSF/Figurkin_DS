# Класс: TGpStringTableEnumerator

**Наследник:** TObject
**Видимость:** public
**Источник:** [[GpStringHash]]
**Исходник:** `src/GpStringHash.pas`

## RAG-поисковые ключи

- kind: class
- id: GpStringHash.TGpStringTableEnumerator
- unit: GpStringHash
- structure_type: class
- source_path: src/GpStringHash.pas
- ancestor: TObject
- methods: Create, Destroy, GetCurrent, MoveNext
- properties: Current

## Описание

**TGpStringTableEnumerator**

Класс-перечислитель для последовательного доступа к элементам `TGpStringTable`. Реализует паттерн итератора, позволяя перебирать все пары (ключ, значение) в таблице строк. Поддерживает стандартный интерфейс перечисления Delphi с методами `MoveNext` и свойством `Current`. Отвечает за навигацию по внутреннему буферу данных `TGpStringTable`, извлечение строк ключей и 64-битных значений, а также определение окончания перечисления.

---

## Иерархия наследования
TGpStringTableEnumerator ← TObject

---

## Методы

### Method: TGpStringTableEnumerator.Create

**ID:** `GpStringHash.TGpStringTableEnumerator.Create`
**Объявление:** `constructor Create(pTable, pTail: pointer);`
**Видимость:** public

Нет описания

### Method: TGpStringTableEnumerator.Destroy

**ID:** `GpStringHash.TGpStringTableEnumerator.Destroy`
**Объявление:** `destructor Destroy; override;`
**Видимость:** public

Нет описания

### Method: TGpStringTableEnumerator.GetCurrent

**ID:** `GpStringHash.TGpStringTableEnumerator.GetCurrent`
**Объявление:** `function GetCurrent: TGpStringTableKV;`
**Видимость:** public

Нет описания

### Method: TGpStringTableEnumerator.MoveNext

**ID:** `GpStringHash.TGpStringTableEnumerator.MoveNext`
**Объявление:** `function MoveNext: boolean;`
**Видимость:** public

Нет описания


## Поля


## Свойства

### Current

**Тип:** TGpStringTableKV
**Видимость:** public
**Reader:** GetCurrent

Нет описания


---

**Источник:** [[GpStringHash]]
