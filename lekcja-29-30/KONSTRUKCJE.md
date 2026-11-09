# Temat 15. Pola i rodzaje metod

## Składnia pod ręką

| Zapis | Do czego służy | Wynik lub ważna reguła |
| --- | --- | --- |
| `self.x` | Pole instancji | Stan konkretnego obiektu. |
| `Klasa.x` | Pole klasy | Dane dostępne przez klasę. |
| `def metoda(self):` | Metoda instancji | Ma dostęp do konkretnego obiektu. |
| `@classmethod` | Dekorator metody klasowej | Pierwszy parametr cls wskazuje klasę. |
| `return cls(...)` | Utworzenie obiektu przez metodę klasową | Uwzględnia klasę, na której wywołano metodę. |
| `@staticmethod` | Dekorator metody statycznej | Nie dodaje automatycznie self ani cls. |
| `self.lista = [] w __init__` | Osobna lista każdej instancji | Lista w ciele klasy byłaby współdzielona. |
| `obj.x = wartość` | Przypisanie na instancji | Zwykle może przesłonić pole klasy o tej nazwie. |

## Krótki wzorzec

```python
class Pomiar:
    def __init__(self, wartosc):
        self.wartosc = wartosc

    @classmethod
    def z_tekstu(cls, tekst):
        return cls(float(tekst))

    @staticmethod
    def poprawny(x):
        return x >= 0

print(Pomiar.z_tekstu("2.5").wartosc)  # 2.5
```

Dla metody operującej na stanie instancji wybierz self. Metoda statyczna nie otrzymuje obiektu automatycznie.

[Dokumentacja](https://docs.python.org/3.13/library/functions.html#classmethod) · [Zadania lekcji](README.md)
