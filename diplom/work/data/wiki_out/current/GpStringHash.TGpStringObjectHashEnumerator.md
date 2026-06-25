# Класс: TGpStringObjectHashEnumerator

**Наследник:** TObject
**Видимость:** public
**Источник:** [[GpStringHash]]
**Исходник:** `src/GpStringHash.pas`

## RAG-поисковые ключи

- kind: class
- id: GpStringHash.TGpStringObjectHashEnumerator
- unit: GpStringHash
- structure_type: class
- source_path: src/GpStringHash.pas
- ancestor: TObject
- methods: Create, Destroy, GetCurrent, MoveNext
- properties: Current

## Описание

**TGpStringObjectHashEnumerator** — перечислитель для последовательного доступа к элементам хеша `TGpStringObjectHash`. Обеспечивает итерацию по парам (ключ, объект), преобразуя внутреннее представление `int64` в `TObject`. Реализует шаблон перебора с методами `MoveNext` и `GetCurrent`, используя внутренний `TGpStringHashEnumerator` для навигации по данным.

---

## Иерархия наследования
TGpStringObjectHashEnumerator ← TObject

---

## Методы

### Method: TGpStringObjectHashEnumerator.Create

**ID:** `GpStringHash.TGpStringObjectHashEnumerator.Create`
**Объявление:** `constructor Create(stringHash: TGpStringHash);`
**Видимость:** public

Нет описания

### Method: TGpStringObjectHashEnumerator.Destroy

**ID:** `GpStringHash.TGpStringObjectHashEnumerator.Destroy`
**Объявление:** `destructor Destroy; override;`
**Видимость:** public

Нет описания

### Method: TGpStringObjectHashEnumerator.GetCurrent

**ID:** `GpStringHash.TGpStringObjectHashEnumerator.GetCurrent`
**Объявление:** `function GetCurrent: TGpStringObjectHashKV;`
**Видимость:** public

Нет описания

### Method: TGpStringObjectHashEnumerator.MoveNext

**ID:** `GpStringHash.TGpStringObjectHashEnumerator.MoveNext`
**Объявление:** `function MoveNext: boolean;`
**Видимость:** public

Нет описания


## Поля


## Свойства

### Current

**Тип:** TGpStringObjectHashKV
**Видимость:** public
**Reader:** GetCurrent

Нет описания


---

**Источник:** [[GpStringHash]]
