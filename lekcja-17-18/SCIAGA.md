# Temat 09. Krotki i zbiory

## Składnia pod ręką

| Zapis | Do czego służy | Wynik lub ważna reguła |
| --- | --- | --- |
| `(x,), tuple(dane)` | Krotka jednoelementowa i konwersja | To przecinek tworzy krotkę, (x) to samo x. |
| `a, b = para` | Rozpakowanie sekwencji | Liczba wartości musi pasować do liczby nazw. |
| `pierwszy, *reszta = dane` | Rozpakowanie z resztą | reszta będzie listą. |
| `set(), {1, 2}` | Pusty i niepusty zbiór | {} tworzy słownik. |
| `s.add(x), s.update(dane)` | Dodanie jednej lub wielu wartości | Zbiór przechowuje wartości unikalne. |
| `s.discard(x), s.remove(x)` | Usunięcie wartości | remove zgłasza KeyError przy braku, discard nie. |
| `a \| b, a & b` | Suma i część wspólna | Operacje zwracają zbiory. |
| `a - b, a ^ b` | Różnica i różnica symetryczna | Różnica zależy od kolejności argumentów. |
| `sorted(s)` | Uporządkowana lista elementów zbioru | Elementy muszą dać się porównać. |

## Krótki wzorzec

```python
a = {2, 4, 6}
b = {4, 5, 6}
print(sorted(a & b))  # [4, 6]
print(sorted(a - b))  # [2]
```

Zbiór nie ma indeksów ani gwarantowanej kolejności. Jego elementy muszą być hashowalne. Krotka może zawierać listę, ale wtedy sama nie nadaje się na element zbioru.

[Dokumentacja](https://docs.python.org/3.13/tutorial/datastructures.html) · [Zadania lekcji](README.md)
