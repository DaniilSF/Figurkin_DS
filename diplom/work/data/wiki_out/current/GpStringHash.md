# Unit: GpStringHash

**Исходник:** `src/GpStringHash.pas`

## RAG-поисковые ключи

- kind: unit
- id: GpStringHash
- source_path: src/GpStringHash.pas
- classes: TGpStringHashKV, TGpStringHashEnumerator, TGpStringHash, TGpStringObjectHashKV, TGpStringObjectHashEnumerator, TGpStringObjectHash, TGpStringInterfaceHashKV, TGpStringInterfaceHashEnumerator, TGpStringInterfaceHash, TGpStringTableKV, TGpStringTableEnumerator, TGpStringTable, TGpStringDictionaryKV, TGpStringDictionaryEnumerator, TGpStringDictionary
- routines: GetGoodHashSize, HashOf, HashOf

## Общее описание
2.0: 2017-03-31 - Fixed pointer operations in 64-bit code. 1.11a: 2015-10-04 - Removed dependency on DSiWin32. 1.11: 2012-02-06 - TGpStringObjectHash.Find returns 'nil' in 'value' parameter if key is not found. 1.10c: 2011-12-20 - Fixed HashOf operation in 64-bit code. 1.10b: 2011-10-25 - Fixed bug in TGpStringInterfaceHash.Find implementation. 1.10a: 2011-02-27 - Fixed bugs in TGpStringInterfaceHash implementation. 1.10: 2011-02-09 - Implemented TGpStringInterfaceHash, a string-indexed hash of interfaces. 1.09: 2010-09-27 - Faster TGpStringDictionary enumerator, enumerates items in insertion order. 1.08: 2010-09-25 - Always define enumerators, they can be used explicitly in pre-2005 Delphi's (see ForEach method in each class for example). - Defined ForEach method in each enumerator-supporting class. - TGpStringHash enumerator returns (string, integer) pairs. - TGpStringObjectHash enumerator returns (string, TObject) pairs. - TGpStringDictionary enumerator returns (string, cardinal, int64) triplets. 1.07: 2010-08-18 - Use better hashing function written by Paul Hsieh (Delphi translation by Davy Landman). 1.06c: 2010-07-18 - HashOf hashes complete string in Unicode Delphis. 1.06b: 2010-06-28 - [lkessler] In TGpStringHash.Add, hash must be calculated *after* Grow is called. 1.06a: 2010-04-09 - Unicode fixes in TGpStringTable. 1.06: 2010-03-04 - String hashing function made public. 1.05b: 2010-01-26 - Fixed a bug in TGpStringTable.SetValue. 1.05: 2008-11-09 - Fixed a bug in TGpStringTable.Grow and TGpStringDictionary.Grow which caused random memory overwrites. 1.05: 2008-11-08 - Added function Count to TGpStringTable, TGpStringDictionary and TGpStringHash. 1.04: 2008-10-20 - Added TGpStringTable string storage. - Added TGpStringDictionary - a hash that uses TGpStringTable for string storage. 1.03: 2008-10-04 - Added support for growing. 1.02: 2007-12-06 - Much enhanced TGpStringHash. - TGpStringObjectHash class added. 1.01: 2006-04-13 - Added simplified constructor.

---

## Структуры (классы)
### Class: TGpStringHashKV

**Ссылка:** [[GpStringHash.TGpStringHashKV|TGpStringHashKV]]
**Наследник:** TObject

**TGpStringHashKV** — это вспомогательный класс-контейнер для представления пар ключ-значение (string → int64) во внешнем интерфейсе. Он используется перечислителями (TGpStringHashEnumerator) для возврата элементов хеш-таблицы при итерации. Класс предоставляет публичные свойства Key и Value для доступа к данным.

### Class: TGpStringHashEnumerator

**Ссылка:** [[GpStringHash.TGpStringHashEnumerator|TGpStringHashEnumerator]]
**Наследник:** TObject

**TGpStringHashEnumerator** — перечислитель для последовательного доступа к элементам хеш-таблицы `TGpStringHash`. Обеспечивает итерацию по парам (ключ-значение) типа `(string, int64)` в порядке их добавления, реализуя стандартный шаблон перечислителя с методами `MoveNext` и `GetCurrent`. Используется для перебора всех записей хеша через `for..in` циклы или метод `ForEach`.

### Class: TGpStringHash

**Ссылка:** [[GpStringHash.TGpStringHash|TGpStringHash]]
**Наследник:** TObject

**TGpStringHash** — это предварительно выделенная хеш-таблица с строковыми ключами и значениями типа `int64`. Класс обеспечивает быстрый доступ к данным (O(1) в среднем случае) через операции добавления, поиска, обновления и проверки наличия ключа. Основная ответственность — эффективное хранение и извлечение пар "строка-целое" с поддержкой динамического роста таблицы при необходимости.

### Class: TGpStringObjectHashKV

**Ссылка:** [[GpStringHash.TGpStringObjectHashKV|TGpStringObjectHashKV]]
**Наследник:** TObject

**TGpStringObjectHashKV** — вспомогательный класс, представляющий внешнее представление элемента хеш-таблицы в виде пары «ключ-значение». Используется при перечислении элементов `TGpStringObjectHash`. Хранит строковый ключ (`Key`) и объект (`Value` типа `TObject`). Служит контейнером для доступа к данным при итерации по хеш-таблице объектов.

### Class: TGpStringObjectHashEnumerator

**Ссылка:** [[GpStringHash.TGpStringObjectHashEnumerator|TGpStringObjectHashEnumerator]]
**Наследник:** TObject

**TGpStringObjectHashEnumerator** — перечислитель для последовательного доступа к элементам хеша `TGpStringObjectHash`. Обеспечивает итерацию по парам (ключ, объект), преобразуя внутреннее представление `int64` в `TObject`. Реализует шаблон перебора с методами `MoveNext` и `GetCurrent`, используя внутренний `TGpStringHashEnumerator` для навигации по данным.

### Class: TGpStringObjectHash

**Ссылка:** [[GpStringHash.TGpStringObjectHash|TGpStringObjectHash]]
**Наследник:** TObject

**TGpStringObjectHash** — хеш-таблица с строковыми ключами и значениями типа `TObject`. Класс обеспечивает быстрый доступ к объектам по имени, храня указатели внутри внутреннего `TGpStringHash`. Основная ответственность — управление коллекцией объектов с автоматическим уничтожением при необходимости (флаг `OwnsObjects`).

### Class: TGpStringInterfaceHashKV

**Ссылка:** [[GpStringHash.TGpStringInterfaceHashKV|TGpStringInterfaceHashKV]]
**Наследник:** TObject

**TGpStringInterfaceHashKV** — класс-контейнер для представления элемента хеш-таблицы внешнего интерфейса. Хранит пару «ключ-значение», где ключ представлен строкой (`string`), а значение — интерфейсом (`IInterface`). Используется при перечислении элементов `TGpStringInterfaceHash` для предоставления доступа к отдельным записям хеш-коллекции.

### Class: TGpStringInterfaceHashEnumerator

**Ссылка:** [[GpStringHash.TGpStringInterfaceHashEnumerator|TGpStringInterfaceHashEnumerator]]
**Наследник:** TObject

**TGpStringInterfaceHashEnumerator** — перечислитель для последовательного доступа к элементам хеша `TGpStringInterfaceHash`. Обеспечивает итерацию по парам (ключ-интерфейс), возвращая объекты типа `TGpStringInterfaceHashKV`. Класс инкапсулирует внутренний перечислитель `TGpStringHashEnumerator` и отвечает за корректное преобразование внутреннего представления значений (`int64`) в интерфейсные ссылки (`IInterface`).

### Class: TGpStringInterfaceHash

**Ссылка:** [[GpStringHash.TGpStringInterfaceHash|TGpStringInterfaceHash]]
**Наследник:** TObject

**TGpStringInterfaceHash** — это хеш-таблица с индексацией по строкам, предназначенная для хранения интерфейсов (IInterface). Класс обеспечивает быстрый поиск, добавление и обновление значений по строковому ключу, автоматически управляя подсчётом ссылок интерфейсов (_AddRef/_Release). Реализация основана на внутреннем TGpStringHash и предоставляет перебор элементов через enumerator.

### Class: TGpStringTableKV

**Ссылка:** [[GpStringHash.TGpStringTableKV|TGpStringTableKV]]
**Наследник:** TObject

**TGpStringTableKV** — вспомогательный класс, представляющий элемент хеш-таблицы в виде пары «ключ-значение» (string, int64). Используется в качестве внешнего представления записей при перечислении (enumeration) данных в TGpStringTable. Класс предоставляет доступ к ключу и значению через свойства Key и Value, обеспечивая удобный способ получения данных при итерации по таблице.

### Class: TGpStringTableEnumerator

**Ссылка:** [[GpStringHash.TGpStringTableEnumerator|TGpStringTableEnumerator]]
**Наследник:** TObject

**TGpStringTableEnumerator**

Класс-перечислитель для последовательного доступа к элементам `TGpStringTable`. Реализует паттерн итератора, позволяя перебирать все пары (ключ, значение) в таблице строк. Поддерживает стандартный интерфейс перечисления Delphi с методами `MoveNext` и свойством `Current`. Отвечает за навигацию по внутреннему буферу данных `TGpStringTable`, извлечение строк ключей и 64-битных значений, а также определение окончания перечисления.

### Class: TGpStringTable

**Ссылка:** [[GpStringHash.TGpStringTable|TGpStringTable]]
**Наследник:** TObject

**TGpStringTable** — это предварительно выделенная таблица для хранения пар «строка + int64». Класс обеспечивает простое и эффективное хранение строк с ассоциированными значениями, где позиция элемента (индекс) остаётся неизменной после добавления и может использоваться как стабильный идентификатор. Основная ответственность класса — обеспечение быстрого доступа к данным по индексу и поддержка операций добавления с возможностью динамического роста. Класс не поддерживает удаление элементов и служит основой для реализации TGpStringDictionary.

### Class: TGpStringDictionaryKV

**Ссылка:** [[GpStringHash.TGpStringDictionaryKV|TGpStringDictionaryKV]]
**Наследник:** TObject

**TGpStringDictionaryKV** — вспомогательный класс для представления элементов словаря `TGpStringDictionary` во внешнем интерфейсе. Хранит триплет данных: индекс элемента в строковой таблице (`Index`), строковый ключ (`Key`) и целочисленное значение (`Value`). Используется перечислителями и методами обратного вызова для передачи информации о найденных элементах.

### Class: TGpStringDictionaryEnumerator

**Ссылка:** [[GpStringHash.TGpStringDictionaryEnumerator|TGpStringDictionaryEnumerator]]
**Наследник:** TObject

**TGpStringDictionaryEnumerator**

Класс-перечислитель для итерации по элементам `TGpStringDictionary`. Реализует паттерн перечисления с методами `GetCurrent`, `MoveNext` и свойством `Current`, возвращающим объекты типа `TGpStringDictionaryKV` (содержащие индекс, ключ и значение). Обеспечивает перебор элементов словаря в порядке их добавления (insertion order).

### Class: TGpStringDictionary

**Ссылка:** [[GpStringHash.TGpStringDictionary|TGpStringDictionary]]
**Наследник:** TObject

**TGpStringDictionary** — хеш-словарь для хранения триплетов `<строка, cardinal, int64>`. Класс обеспечивает быстрый доступ к данным по строковому ключу с использованием хеш-таблицы, а также поддерживает перечисление элементов в порядке их добавления. Основная ответственность класса — эффективное управление ассоциативным массивом строковых ключей с целочисленными значениями с предсказуемым поведением при обходе коллекции.


## Типы


## Переменные уровня unit


---
*Сгенерировано из: src/GpStringHash.pas*
