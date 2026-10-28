# Temat 08. Listy

## Składnia pod ręką

| Zapis | Do czego służy | Wynik lub ważna reguła |
| --- | --- | --- |
| `a.append(x)` | Dodanie jednego obiektu | Modyfikuje a, zwraca None. |
| `a.extend(dane)` | Dodanie kolejnych elementów | extend([2, 3]) dodaje dwa elementy. |
| `a.insert(i, x)` | Wstawienie przed indeksem i | Pozostałe elementy przesuwają się. |
| `a.pop(i), a.pop()` | Usunięcie i zwrot elementu | Bez i usuwa ostatni, pusta lista daje IndexError. |
| `a.remove(x)` | Usunięcie pierwszej wartości x | ValueError, jeśli jej nie ma. |
| `del a[i]` | Usunięcie elementu | Nie zwraca wartości. |
| `a.index(x), a.count(x)` | Pierwszy indeks i liczba wystąpień | index zgłasza ValueError przy braku x. |
| `a.copy(), a[:]` | Płytka kopia listy | Zagnieżdżone obiekty nadal mogą być wspólne. |
| `a.sort(), sorted(a)` | Sortowanie w miejscu i nowa lista | sort zwraca None. |

## Krótki wzorzec

```python
oryginal = [6, 2, 4]
kopia = oryginal.copy()
kopia.append(1)
print(sorted(kopia))  # [1, 2, 4, 6]
print(oryginal)       # [6, 2, 4]
```

b = a tworzy drugą nazwę tej samej listy. Unikaj usuwania z listy podczas przechodzenia po niej zwykłą pętlą for.

[Dokumentacja](https://docs.python.org/3.13/tutorial/datastructures.html) · [Zadania lekcji](README.md)
