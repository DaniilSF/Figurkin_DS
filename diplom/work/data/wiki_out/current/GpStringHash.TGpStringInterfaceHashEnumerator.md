# Класс: TGpStringInterfaceHashEnumerator

**Наследник:** TObject
**Видимость:** public
**Источник:** [[GpStringHash]]
**Исходник:** `src/GpStringHash.pas`

## RAG-поисковые ключи

- kind: class
- id: GpStringHash.TGpStringInterfaceHashEnumerator
- unit: GpStringHash
- structure_type: class
- source_path: src/GpStringHash.pas
- ancestor: TObject
- methods: Create, Destroy, GetCurrent, MoveNext
- properties: Current

## Описание

**TGpStringInterfaceHashEnumerator** — перечислитель для последовательного доступа к элементам хеша `TGpStringInterfaceHash`. Обеспечивает итерацию по парам (ключ-интерфейс), возвращая объекты типа `TGpStringInterfaceHashKV`. Класс инкапсулирует внутренний перечислитель `TGpStringHashEnumerator` и отвечает за корректное преобразование внутреннего представления значений (`int64`) в интерфейсные ссылки (`IInterface`).

---

## Иерархия наследования
TGpStringInterfaceHashEnumerator ← TObject

---

## Методы

### Method: TGpStringInterfaceHashEnumerator.Create

**ID:** `GpStringHash.TGpStringInterfaceHashEnumerator.Create`
**Объявление:** `constructor Create(stringHash: TGpStringHash);`
**Видимость:** public

Нет описания

### Method: TGpStringInterfaceHashEnumerator.Destroy

**ID:** `GpStringHash.TGpStringInterfaceHashEnumerator.Destroy`
**Объявление:** `destructor Destroy; override;`
**Видимость:** public

Нет описания

### Method: TGpStringInterfaceHashEnumerator.GetCurrent

**ID:** `GpStringHash.TGpStringInterfaceHashEnumerator.GetCurrent`
**Объявление:** `function GetCurrent: TGpStringInterfaceHashKV;`
**Видимость:** public

Нет описания

### Method: TGpStringInterfaceHashEnumerator.MoveNext

**ID:** `GpStringHash.TGpStringInterfaceHashEnumerator.MoveNext`
**Объявление:** `function MoveNext: boolean;`
**Видимость:** public

Нет описания


## Поля


## Свойства

### Current

**Тип:** TGpStringInterfaceHashKV
**Видимость:** public
**Reader:** GetCurrent

Нет описания


---

**Источник:** [[GpStringHash]]
