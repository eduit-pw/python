# Temat 11. Wyrażenia składane, enumerate i zip

## Składnia pod ręką

| Zapis | Do czego służy | Wynik lub ważna reguła |
| --- | --- | --- |
| `[f(x) for x in dane]` | Nowa lista z przekształconych elementów | Np. [x * 2 for x in dane]. |
| `[x for x in dane if warunek]` | Filtrowanie elementów | if na końcu decyduje, czy dodać element. |
| `[a if warunek else b for x in dane]` | Wybór wartości dla każdego elementu | Nie zmniejsza liczby elementów. |
| `{klucz: wartosc for x in dane}` | Nowy słownik | Powtórzony klucz zastępuje wcześniejszą wartość. |
| `enumerate(dane)` | Pary indeks i element | Domyślnie indeksowanie od 0. |
| `enumerate(dane, start=1)` | Pary numer i element | Zmienia numerowanie, nie indeksy oryginalnej listy. |
| `zip(a, b)` | Pary odpowiadających elementów | Domyślnie kończy się wraz z najkrótszym wejściem. |
| `list(zip(a, b))` | Utrwalenie par w liście | zip sam zwraca iterator. |

## Krótki wzorzec

```python
liczby = [-2, 3, 0, 5]
print([x * 2 for x in liczby if x > 0])  # [6, 10]
print(list(enumerate(["a", "b"], start=1)))
# [(1, 'a'), (2, 'b')]
```

Gdy długości danych muszą być równe, zip(a, b, strict=True) zgłosi ValueError przy rozbieżności podczas iterowania.

[Dokumentacja](https://docs.python.org/3.13/library/functions.html#zip) · [Zadania lekcji](README.md)
