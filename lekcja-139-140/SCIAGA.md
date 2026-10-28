# Temat 67. asyncio

## Składnia pod ręką

| Zapis | Do czego służy | Wynik lub ważna reguła |
| --- | --- | --- |
| `async def f():` | Definicja funkcji korutynowej | Samo wywołanie f() tworzy obiekt korutyny. |
| `await operacja` | Oczekiwanie wewnątrz korutyny | Pozwala oddać sterowanie przy operacji zawieszającej. |
| `asyncio.run(main())` | Start głównej korutyny | Zwykły punkt wejścia skryptu, bez innej działającej pętli. |
| `asyncio.create_task(f())` | Zaplanowanie korutyny | Wymaga działającej pętli. |
| `await asyncio.gather(a(), b())` | Współbieżne operacje i lista wyników | Wyniki w kolejności argumentów. |
| `await asyncio.sleep(sekundy)` | Nieblokujące oczekiwanie | time.sleep blokowałoby wątek pętli. |
| `async with asyncio.timeout(limit):` | Ograniczenie czasu bloku | TimeoutError obsłuż poza blokiem. |
| `await asyncio.to_thread(funkcja, argument)` | Blokujące I/O w osobnym wątku | Anulowanie await nie zatrzymuje automatycznie wątku. |

## Krótki wzorzec

```python
import asyncio

async def pomiar(nazwa, opoznienie):
    await asyncio.sleep(opoznienie)
    return nazwa

async def main():
    wyniki = await asyncio.gather(pomiar("A", 0.02), pomiar("B", 0.01))
    print(wyniki)  # ['A', 'B']

asyncio.run(main())
```

B kończy się wcześniej, ale wyniki są w kolejności A, B. asyncio usprawnia oczekiwanie na I/O, nie przyspiesza automatycznie obliczeń CPU.

[Dokumentacja](https://docs.python.org/3.13/library/asyncio-task.html) · [Zadania lekcji](README.md)
