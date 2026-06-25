# Класс: TGpLockFreeQueue

**Наследник:** TObject
**Видимость:** public
**Источник:** [[GpLockFreeQueue]]
**Исходник:** `src/GpLockFreeQueue.pas`

## RAG-поисковые ключи

- kind: class
- id: GpLockFreeQueue.TGpLockFreeQueue
- unit: GpLockFreeQueue
- structure_type: class
- source_path: src/GpLockFreeQueue.pas
- ancestor: TObject
- methods: AllocateAligned, AllocateBlock, Cleanup, Initialize, NextSlot, PartitionMemory, PreallocateMemory, PrevSlot, ReleaseBlock, Create, Destroy, Dequeue, Enqueue

## Описание

**TGpLockFreeQueue** — класс реализует динамически выделяемую, потокобезопасную очередь без блокировок (lock-free) с гарантированной O(1) производительностью операций enqueue и dequeue. Класс обеспечивает микроблокировку через атомарные операции CAS, позволяя безопасно использовать очередь в многопоточной среде без традиционных мьютексов. Основная ответственность класса — обеспечение быстрой и эффективной организации очереди для передачи данных между потоками с минимальными задержками и отсутствием блокировок.

---

## Иерархия наследования
TGpLockFreeQueue ← TObject

---

## Методы

### Method: TGpLockFreeQueue.AllocateAligned

**ID:** `GpLockFreeQueue.TGpLockFreeQueue.AllocateAligned`
**Объявление:** `function AllocateAligned(size, alignment: integer; var memPtr: pointer): pointer;`
**Видимость:** protected

Нет описания

### Method: TGpLockFreeQueue.AllocateBlock

**ID:** `GpLockFreeQueue.TGpLockFreeQueue.AllocateBlock`
**Объявление:** `function AllocateBlock: PGpLFQueueTaggedValue;`
**Видимость:** protected

Нет описания

### Method: TGpLockFreeQueue.Cleanup

**ID:** `GpLockFreeQueue.TGpLockFreeQueue.Cleanup`
**Объявление:** `procedure Cleanup; virtual;`
**Видимость:** protected

Нет описания

### Method: TGpLockFreeQueue.Initialize

**ID:** `GpLockFreeQueue.TGpLockFreeQueue.Initialize`
**Объявление:** `procedure Initialize; virtual;`
**Видимость:** protected

Нет описания

### Method: TGpLockFreeQueue.NextSlot

**ID:** `GpLockFreeQueue.TGpLockFreeQueue.NextSlot`
**Объявление:** `function NextSlot(slot: PGpLFQueueTaggedValue): PGpLFQueueTaggedValue;`
**Видимость:** protected

Нет описания

### Method: TGpLockFreeQueue.PartitionMemory

**ID:** `GpLockFreeQueue.TGpLockFreeQueue.PartitionMemory`
**Объявление:** `procedure PartitionMemory(memory: PGpLFQueueTaggedValue);`
**Видимость:** protected

Нет описания

### Method: TGpLockFreeQueue.PreallocateMemory

**ID:** `GpLockFreeQueue.TGpLockFreeQueue.PreallocateMemory`
**Объявление:** `procedure PreallocateMemory;`
**Видимость:** protected

Нет описания

### Method: TGpLockFreeQueue.PrevSlot

**ID:** `GpLockFreeQueue.TGpLockFreeQueue.PrevSlot`
**Объявление:** `function PrevSlot(slot: PGpLFQueueTaggedValue): PGpLFQueueTaggedValue;`
**Видимость:** protected

Нет описания

### Method: TGpLockFreeQueue.ReleaseBlock

**ID:** `GpLockFreeQueue.TGpLockFreeQueue.ReleaseBlock`
**Объявление:** `procedure ReleaseBlock(firstSlot: PGpLFQueueTaggedValue; forceFree: boolean = false);`
**Видимость:** protected

Нет описания

### Method: TGpLockFreeQueue.Create

**ID:** `GpLockFreeQueue.TGpLockFreeQueue.Create`
**Объявление:** `constructor Create(blockSize: integer = 65536; numCachedBlocks: integer = 2);`
**Видимость:** public

Нет описания

### Method: TGpLockFreeQueue.Destroy

**ID:** `GpLockFreeQueue.TGpLockFreeQueue.Destroy`
**Объявление:** `destructor Destroy; override;`
**Видимость:** public

Нет описания

### Method: TGpLockFreeQueue.Dequeue

**ID:** `GpLockFreeQueue.TGpLockFreeQueue.Dequeue`
**Объявление:** `function Dequeue(var value: int64): boolean;`
**Видимость:** public

Нет описания

### Method: TGpLockFreeQueue.Enqueue

**ID:** `GpLockFreeQueue.TGpLockFreeQueue.Enqueue`
**Объявление:** `procedure Enqueue(const value: int64);`
**Видимость:** public

Нет описания


## Поля


## Свойства


---

**Источник:** [[GpLockFreeQueue]]
