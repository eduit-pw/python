# Temat 16. Metody specjalne

## Składnia pod ręką

| Zapis | Do czego służy | Wynik lub ważna reguła |
| --- | --- | --- |
| `str(obj), print(obj)` | Czytelny opis obiektu | Korzysta z __str__, z rezerwowym __repr__. |
| `repr(obj), f"{obj!r}"` | Reprezentacja diagnostyczna | Korzysta z __repr__. |
| `print([obj])` | Wydruk listy obiektów | Lista używa repr swoich elementów. |
| `def __str__(self):` | Własny opis dla użytkownika | Zwraca str, samo print w metodzie nie wystarcza. |
| `def __repr__(self):` | Własna reprezentacja | Też musi zwrócić str. |
| `def __len__(self):` | Obsługa len(obj) | Zwraca nieujemną liczbę całkowitą. |
| `def __eq__(self, other):` | Obsługa porównania == | Dla nieobsługiwanego typu można zwrócić NotImplemented. |
| `a is b` | Tożsamość obiektów | Sprawdza, czy to ten sam obiekt. |

## Krótki wzorzec

```python
class Kolor:
    def __init__(self, nazwa):
        self.nazwa = nazwa

    def __str__(self):
        return self.nazwa

    def __repr__(self):
        return f"Kolor({self.nazwa!r})"

x = Kolor("zielony")
print(x)     # zielony
print([x])   # [Kolor('zielony')]
```

NotImplemented jest specjalną wartością, a NotImplementedError wyjątkiem. Bez __bool__ wynik __len__ równy 0 daje bool(obj) równy False.

[Dokumentacja](https://docs.python.org/3.13/reference/datamodel.html) · [Zadania lekcji](README.md)
