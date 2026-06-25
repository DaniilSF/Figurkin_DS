# Unit: GpLockFreeQueue

**Исходник:** `src/GpLockFreeQueue.pas`

## RAG-поисковые ключи

- kind: unit
- id: GpLockFreeQueue
- source_path: src/GpLockFreeQueue.pas
- classes: TGpLockFreeQueue

## Общее описание
Primoz Gabrijelcic This software is distributed under the BSD license. Copyright (c) 2010 Primoz Gabrijelcic All rights reserved. Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met: - Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer. - Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution. - The name of the Primoz Gabrijelcic may not be used to endorse or promote products derived from this software without specific prior written permission. THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE. Author : Primoz Gabrijelcic Creation date : 2010-02-10 Last modification : 2010-10-13 Version : 1.01c History: 1.01c: 2010-10-13 - [GJ] Alignment algorithm simplification and fix. 1.01b: 2010-10-11 - Fixed internal alignment algorithm. 1.01a: 2010-09-28 - Assumes that memory allocations are 4-aligned. 8-alignment is implemented internally. 1.01: 2010-02-18 - Reversed head and tail because they were used illogically. 1.0: 2010-02-10 - Initial implementation, based on the TOmniBaseQueue from the OmniThreadLibrary. The following code requires at least Pentium 4 processor because SSE2 instructions are used in the Move64 function. defined to not use SSE2-specific stuff - apparently there's a lot of AMD CPUs without SSE2 support out there

---

## Структуры (классы)
### Class: TGpLockFreeQueue

**Ссылка:** [[GpLockFreeQueue.TGpLockFreeQueue|TGpLockFreeQueue]]
**Наследник:** TObject

**TGpLockFreeQueue** — класс реализует динамически выделяемую, потокобезопасную очередь без блокировок (lock-free) с гарантированной O(1) производительностью операций enqueue и dequeue. Класс обеспечивает микроблокировку через атомарные операции CAS, позволяя безопасно использовать очередь в многопоточной среде без традиционных мьютексов. Основная ответственность класса — обеспечение быстрой и эффективной организации очереди для передачи данных между потоками с минимальными задержками и отсутствием блокировок.


## Типы


## Переменные уровня unit


---
*Сгенерировано из: src/GpLockFreeQueue.pas*
