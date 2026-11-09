# Temat 14. Klasy, obiekty i __init__

## Składnia pod ręką

| Zapis | Do czego służy | Wynik lub ważna reguła |
| --- | --- | --- |
| `class Nazwa:` | Definicja klasy | Klasa opisuje dane i operacje obiektu. |
| `Nazwa(argumenty)` | Utworzenie instancji | Zwykle uruchamia jej __init__. |
| `def __init__(self, x):` | Inicjalizacja stanu | Metoda ma zwracać None. |
| `self.pole = x` | Pole konkretnego obiektu | Każda instancja może mieć inną wartość. |
| `def metoda(self):` | Metoda instancji | Przy obj.metoda() Python przekazuje obj jako self. |
| `obj.pole` | Odczyt pola | Brak pola powoduje AttributeError. |
| `obj.metoda()` | Wywołanie metody | Nawiasy rozpoczynają wykonanie. |
| `drugi = pierwszy` | Druga nazwa tego samego obiektu | Nie tworzy kopii instancji. |

## Krótki wzorzec

```python
class Lampa:
    def __init__(self, kolor):
        self.kolor = kolor
        self.wlaczona = False

    def wlacz(self):
        self.wlaczona = True

lampa = Lampa("biała")
lampa.wlacz()
print(lampa.wlaczona)  # True
```

self nie jest słowem kluczowym. To przyjęta nazwa parametru wskazującego bieżący obiekt.

[Dokumentacja](https://docs.python.org/3.13/tutorial/classes.html) · [Zadania lekcji](README.md)
