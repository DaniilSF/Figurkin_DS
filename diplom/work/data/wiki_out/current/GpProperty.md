# Unit: GpProperty

**Исходник:** `src/GpProperty.pas`

## RAG-поисковые ключи

- kind: unit
- id: GpProperty
- source_path: src/GpProperty.pas
- routines: CreateGpProperty, CreateGpProperty, GetFloatProp, SetFloatProp, GetWideStrProp, SetWideStrProp, SetToString, StringToSet

## Общее описание

# GpProperty

**Назначение:** Упрощённый доступ к опубликованным (published) свойствам объектов Delphi.

## Основные сущности

### IGpProperty (интерфейс)
Интерфейс для работы с опубликованными свойствами объекта. Предоставляет типизированный доступ к значениям свойств через индексацию:

- `StringValue`, `AnsiStringValue`, `WideStringValue` — строковые значения
- `IntegerValue`, `Int64Value` — целочисленные значения
- `BooleanValue` — булевы значения
- `FloatValue`, `ExtendedValue` — значения с плавающей точкой
- `EnumValue` — перечислимые значения
- `VariantValue` — произвольные значения

Дополнительные возможности:
- `Name[]` — получение имени свойства по индексу
- `PropInfo[]` — доступ к PPropInfo
- `Count` — количество свойств
- `IndexOf()` — поиск свойства по имени

### TGpProperty (класс)
Реализация интерфейса IGpProperty. Автоматически перечисляет все опубликованные свойства объекта при вызове `Access()`.

### CreateGpProperty()
Фабричные функции для создания экземпляра TGpProperty:
- `CreateGpProperty(instance)` — для текущего класса объекта
- `CreateGpProperty(instance, classInfo)` — для указанного базового класса

### Вспомогательные функции
- `GetFloatProp/SetFloatProp` — работа с float-свойствами (совместимость с D7)
- `GetWideStrProp/SetWideStrProp` — работа со wide-строками
- `SetToString/StringToSet` — конвертация множеств (set) в строку и обратно

---

## Структуры (классы)

## Типы


## Переменные уровня unit


---
*Сгенерировано из: src/GpProperty.pas*
