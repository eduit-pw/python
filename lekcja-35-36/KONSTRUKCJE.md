# Temat 18. Dziedziczenie i super

## Składnia pod ręką

| Zapis | Do czego służy | Wynik lub ważna reguła |
| --- | --- | --- |
| `class Dziecko(Baza):` | Klasa pochodna | Dziedziczy dostępne metody klasy bazowej. |
| `Brak własnego __init__` | Wyszukanie odziedziczonej inicjalizacji | Wywołanie musi pasować do jej parametrów. |
| `Własny __init__` | Zastąpienie odziedziczonej inicjalizacji | Bazowe __init__ nie uruchomi się automatycznie. |
| `super().__init__(...)` | Współpraca z inicjalizacją bazową | W prostym dziedziczeniu uruchamia inicjalizację rodzica. |
| `super().metoda(...)` | Rozszerzenie odziedziczonego zachowania | super korzysta z kolejności MRO. |
| `isinstance(obj, Baza)` | Sprawdzenie instancji klasy lub podklasy | Wynik bool. |
| `issubclass(Dziecko, Baza)` | Sprawdzenie relacji między klasami | Argumentami są klasy. |

## Krótki wzorzec

```python
class Pojazd:
    def __init__(self, marka):
        self.marka = marka

class Rower(Pojazd):
    def __init__(self, marka, biegi):
        super().__init__(marka)
        self.biegi = biegi

rower = Rower("Miejski", 7)
print(rower.marka, rower.biegi)  # Miejski 7
```

Dziedziczenie pasuje do relacji „jest rodzajem”. Relację „ma obiekt” zwykle modeluje pole z innym obiektem.

[Dokumentacja](https://docs.python.org/3.13/tutorial/classes.html#inheritance) · [Zadania lekcji](README.md)
