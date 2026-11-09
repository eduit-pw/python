# Temat 22. Własne wyjątki i walidacja

## Składnia pod ręką

| Zapis | Do czego służy | Wynik lub ważna reguła |
| --- | --- | --- |
| `raise ValueError("opis")` | Zgłoszenie niedozwolonej wartości | Przerywa zwykły przebieg funkcji. |
| `raise TypeError("opis")` | Zgłoszenie nieodpowiedniego typu | Pozwala odróżnić błąd typu od wartości. |
| `class Blad(ValueError):` | Własna klasa wyjątku | Można obsłużyć Blad lub jego klasę bazową. |
| `super().__init__(komunikat)` | Komunikat wyjątku w klasie pochodnej | str(blad) wyświetli komunikat. |
| `isinstance(x, int)` | Sprawdzenie typu wraz z podklasami | True jest też instancją int. |
| `type(x) is int` | Wymaganie dokładnego typu int | Odrzuca bool i podklasy int. |
| `Walidacja przed przypisaniem` | Ochrona poprawnego stanu | Sprawdź wszystkie reguły przed zmianą pól. |

## Krótki wzorzec

```python
class BladZakresu(ValueError):
    pass

def ustaw_poziom(x):
    if type(x) is not int:
        raise TypeError("Oczekiwano int")
    if not 0 <= x <= 10:
        raise BladZakresu("Dozwolony zakres: 0..10")
    return x

print(ustaw_poziom(4))  # 4
```

Własny wyjątek może przechowywać dane, np. odrzuconą wartość. Nie zastępuj każdego wyjątku ogólnym Exception.

[Dokumentacja](https://docs.python.org/3.13/tutorial/errors.html#user-defined-exceptions) · [Zadania lekcji](README.md)
