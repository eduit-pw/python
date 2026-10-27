# Temat 67. Wyjaśnienia do praktyki

## Korutyna

async def tworzy funkcję korutynową. Jej wywołanie daje obiekt korutyny, nie gotowy wynik. await czeka w sposób pozwalający innym zadaniom pętli działać przy odpowiedniej operacji.

## asyncio.run

asyncio.run(main()) uruchamia główną korutynę w zwykłym skrypcie i zarządza pętlą. Nie wywołuj go wewnątrz już działającej pętli. Zachowaj jeden punkt startu aplikacji.

## gather

asyncio.gather planuje przekazane operacje współbieżnie i zwraca wyniki w kolejności argumentów. Kolejność zakończenia nie musi być kolejnością listy wynikowej.

## Nieblokujące oczekiwanie

await asyncio.sleep oddaje sterowanie. time.sleep blokuje wątek i zatrzymuje postęp innych zadań tej pętli. Współbieżność I/O nie oznacza automatycznego przyspieszenia obliczeń CPU.

## Timeout

asyncio.timeout ogranicza czas bloku. TimeoutError obsłuż na zewnątrz tego bloku. Po obsłudze program może kontynuować. Zmierz rzeczywisty czas przez perf_counter i traktuj wynik jako przybliżony.

[Zadania i wyniki kontrolne](README.md)

To uzupełnienie przykładów z prezentacji. Definicje i kontrakty zadań czytaj łącznie. Szczegółowe przykłady są również w tekście prezentacji dołączonym do paczki.
