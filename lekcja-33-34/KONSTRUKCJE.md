# Temat 17. Hermetyzacja i property

## Składnia pod ręką

| Zapis | Do czego służy | Wynik lub ważna reguła |
| --- | --- | --- |
| `self._x` | Umownie wewnętrzne pole | Podkreślnik nie blokuje dostępu. |
| `self.__x` | Nazwa podlegająca przekształceniu w klasie | Nie zapewnia ochrony sekretów. |
| `@property` | Getter właściwości | Użycie: obj.x bez nawiasów. |
| `@x.setter` | Setter właściwości x | Użycie: obj.x = wartość. |
| `self._x w getterze` | Odczyt pola przechowującego dane | self.x w getterze x wywołałoby go ponownie. |
| `self.x = wartość w __init__` | Inicjalizacja przez setter | Wykorzystuje tę samą walidację. |
| `raise ValueError("opis")` | Odrzucenie niedozwolonej wartości | Sprawdź dane przed zmianą stanu. |
| `property bez settera` | Właściwość tylko do odczytu | Przypisanie do niej powoduje AttributeError. |

## Krótki wzorzec

```python
class Skala:
    def __init__(self, wartosc):
        self.wartosc = wartosc

    @property
    def wartosc(self):
        return self._wartosc

    @wartosc.setter
    def wartosc(self, nowa):
        if nowa < 0:
            raise ValueError("Wartość ujemna")
        self._wartosc = nowa

print(Skala(3).wartosc)  # 3
```

Getter i setter w zwykłym zapisie dekoratorowym powinny mieć tę samą nazwę właściwości. Błędna wartość ma pozostawić poprzedni stan.

[Dokumentacja](https://docs.python.org/3.13/library/functions.html#property) · [Zadania lekcji](README.md)
