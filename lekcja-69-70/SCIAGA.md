# Temat 34. Palindromy, anagramy i lider

## Składnia pod ręką

| Zapis | Do czego służy | Wynik lub ważna reguła |
| --- | --- | --- |
| `s == s[::-1]` | Test palindromu | Porównuje dokładny tekst. |
| `s.lower(), s.casefold()` | Ujednolicenie wielkości liter | casefold jest silniejszą normalizacją Unicode. |
| `znak.isalnum()` | Litera lub cyfra | Uwzględnia Unicode. |
| `sorted(a) == sorted(b)` | Test anagramu po normalizacji | Zachowuje liczności znaków. |
| `liczniki.get(znak, 0) + 1` | Kolejna liczność znaku | Sam zbiór znaków gubi powtórzenia. |
| `liczby.count(kandydat)` | Zliczenie kandydata | Jeden pełny przebieg po liście. |
| `licznosc > len(dane) // 2` | Ścisła większość | Dokładnie połowa nie wystarcza. |
| `Drugi przebieg algorytmu lidera` | Potwierdzenie kandydata | Samo wskazanie kandydata nie dowodzi większości. |

## Krótki wzorzec

```python
tekst = "Kajak"
normalny = tekst.lower()
print(normalny == normalny[::-1])  # True
print(sorted("rama") == sorted("mara"))  # True
print(set("aab") == set("abb"))  # True, lecz to nie anagramy
```

Normalizację dobierz do polecenia. Nie usuwaj spacji ani nie zmieniaj liter, jeżeli zadanie wymaga porównania dokładnego zapisu.

[Dokumentacja](https://docs.python.org/3.13/library/stdtypes.html#str.casefold) · [Zadania lekcji](README.md)
