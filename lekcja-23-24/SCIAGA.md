# Temat 12. lambda, map, filter, math i random

## Składnia pod ręką

| Zapis | Do czego służy | Wynik lub ważna reguła |
| --- | --- | --- |
| `lambda x: wyrażenie` | Mała funkcja z jednym wyrażeniem | Wynik wyrażenia jest wynikiem funkcji. |
| `sorted(dane, key=lambda x: ...)` | Sortowanie według wybranej cechy | Zwraca nową listę. |
| `map(f, dane)` | Zastosowanie f do elementów | Wynik jest iteratorem. |
| `filter(f, dane)` | Pozostawienie elementów spełniających f | Wynik jest iteratorem. |
| `math.sqrt(x), math.isqrt(n)` | Pierwiastek i całkowita część pierwiastka | isqrt przyjmuje nieujemne int. |
| `math.gcd(a, b)` | Największy wspólny dzielnik | Wynik jest nieujemną liczbą całkowitą. |
| `random.randint(a, b)` | Losowy int od a do b włącznie | Obie granice należą do zakresu. |
| `random.randrange(a, b)` | Losowy int w zakresie range(a, b) | b jest pomijane. |
| `random.choice(dane), random.shuffle(lista)` | Wybór elementu i przetasowanie | shuffle zmienia listę, zwraca None. |

## Krótki wzorzec

```python
import math

pary = [("a", 8), ("b", 3)]
print(sorted(pary, key=lambda para: para[1]))
# [('b', 3), ('a', 8)]
print(math.gcd(42, 30))  # 6
```

Iterator map lub filter zużywa się podczas odczytu. random służy do symulacji i losowania w ćwiczeniach. Do tokenów używa się secrets.

[Dokumentacja](https://docs.python.org/3.13/library/random.html) · [Zadania lekcji](README.md)
