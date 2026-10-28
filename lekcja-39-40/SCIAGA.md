# Temat 20. Iteratory i generatory

## Składnia pod ręką

| Zapis | Do czego służy | Wynik lub ważna reguła |
| --- | --- | --- |
| `iter(dane)` | Pobranie iteratora | Iterator przechowuje stan przejścia. |
| `next(it)` | Pobranie kolejnej wartości | Po wyczerpaniu zgłasza StopIteration. |
| `next(it, domyslna)` | Odczyt z wartością zastępczą | Zwraca domyslna po wyczerpaniu. |
| `__iter__(self)` | Obsługa iter(obj) | Zwraca iterator, iterator zwykle zwraca self. |
| `__next__(self)` | Obsługa next(obj) | Zwraca wartość albo zgłasza StopIteration. |
| `yield wartość` | Oddanie wartości i zawieszenie funkcji | Funkcja z yield tworzy generator. |
| `return w generatorze` | Koniec generatora | Nie oddaje kolejnego elementu. |
| `(f(x) for x in dane)` | Wyrażenie generatorowe | Przetwarza elementy na żądanie. |

## Krótki wzorzec

```python
def odliczaj(n):
    while n > 0:
        yield n
        n -= 1

g = odliczaj(3)
print(next(g))  # 3
print(list(g))  # [2, 1]
print(list(g))  # []
```

Generator jest jednorazowym iteratorem. Samo len(g) nie działa. list(g) zużywa generator i przechowuje wszystkie uzyskane elementy w pamięci.

[Dokumentacja](https://docs.python.org/3.13/tutorial/classes.html#generators) · [Zadania lekcji](README.md)
