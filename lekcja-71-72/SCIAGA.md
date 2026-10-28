# Temat 35. Wyszukiwanie i bisekcja

## Składnia pod ręką

| Zapis | Do czego służy | Wynik lub ważna reguła |
| --- | --- | --- |
| `x in dane` | Sprawdzenie obecności | Dla listy zwykle wyszukiwanie liniowe. |
| `enumerate(dane)` | Przegląd wartości wraz z indeksem | Pomaga zwrócić pozycję wyniku. |
| `lewy, prawy = 0, len(dane) - 1` | Przedział indeksów domknięty | Pusta lista daje prawy równy -1. |
| `srodek = (lewy + prawy) // 2` | Środek przedziału | Dzielenie całkowite daje indeks. |
| `lewy = srodek + 1` | Odrzucenie lewej części | Dla posortowanej listy, gdy szukana wartość jest większa. |
| `prawy = srodek - 1` | Odrzucenie prawej części | Gdy szukana wartość jest mniejsza. |
| `O(n), O(log n)` | Typowy koszt wyszukiwania liniowego i binarnego | Binarne wymaga uporządkowanych danych. |
| `f(a) * f(b) < 0` | Przeciwne znaki końców | Dla ciągłej funkcji gwarantuje miejsce zerowe wewnątrz. |

## Krótki wzorzec

```python
from bisect import bisect_left

dane = [2, 5, 8, 11]
x = 8
i = bisect_left(dane, x)
znaleziono = i < len(dane) and dane[i] == x
print(i, znaleziono)  # 2 True
```

bisect_left zwraca miejsce wstawienia, nie potwierdzenie obecności. Własne wyszukiwanie zaimplementuj, gdy tego wymaga polecenie. W bisekcji funkcji osobno sprawdź zera na końcach.

[Dokumentacja](https://docs.python.org/3.13/library/bisect.html) · [Zadania lekcji](README.md)
