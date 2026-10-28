# Temat 36. Minimum, maksimum i sortowanie

## Składnia pod ręką

| Zapis | Do czego służy | Wynik lub ważna reguła |
| --- | --- | --- |
| `min(dane), max(dane)` | Najmniejsza i największa wartość | Puste dane bez default powodują ValueError. |
| `sorted(dane)` | Nowa posortowana lista | Nie zmienia danych wejściowych. |
| `lista.sort()` | Sortowanie listy w miejscu | Zwraca None. |
| `reverse=True` | Porządek malejący | Opcja sorted i sort. |
| `key=lambda x: ...` | Wskazanie klucza sortowania | Porównywana jest obliczona cecha. |
| `a[i], a[j] = a[j], a[i]` | Zamiana elementów | Przydatna m.in. w bubble sort i selection sort. |
| `klucz = a[i]` | Zapamiętanie wartości przed przesuwaniem | Potrzebne w insertion sort. |
| `Stabilne sortowanie` | Zachowanie kolejności równych kluczy | Wbudowane sort i sorted są stabilne. |

## Krótki wzorzec

```python
dane = [("b", 2), ("a", 1), ("c", 2)]
wynik = sorted(dane, key=lambda para: para[1])
print(wynik)  # [('a', 1), ('b', 2), ('c', 2)]
print(min([4, -2, 7]), max([4, -2, 7]))  # -2 7
```

W zadaniu wymagającym bubble sort, insertion sort lub selection sort użyj wskazanego algorytmu. sorted wykorzystaj do porównania wyników.

[Dokumentacja](https://docs.python.org/3.13/howto/sorting.html) · [Zadania lekcji](README.md)
