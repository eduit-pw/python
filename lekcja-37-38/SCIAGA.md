# Temat 19. Polimorfizm i abstrakcja

## Składnia pod ręką

| Zapis | Do czego służy | Wynik lub ważna reguła |
| --- | --- | --- |
| `obj.metoda()` | Wywołanie zgodnie z typem obiektu | Różne klasy mogą realizować ten sam interfejs. |
| `Duck typing` | Wymaganie konkretnej operacji | Klasy nie muszą mieć wspólnej klasy bazowej. |
| `from abc import ABC, abstractmethod` | Import narzędzi abstrakcji | Moduł standardowy. |
| `class Baza(ABC):` | Klasa mogąca definiować kontrakt | Sama obecność ABC nie wymusza metod abstrakcyjnych. |
| `@abstractmethod` | Oznaczenie wymaganej metody | Niepełnej klasy abstrakcyjnej nie utworzysz. |
| `Wspólna sygnatura i znaczenie wyniku` | Zastępowalność obiektów | Sama taka sama nazwa metody nie wystarcza. |

## Krótki wzorzec

```python
from abc import ABC, abstractmethod

class Eksport(ABC):
    @abstractmethod
    def opis(self):
        pass

class Tekst(Eksport):
    def opis(self):
        return "TXT"

print(Tekst().opis())  # TXT
```

Próba Eksport() w tym przykładzie spowoduje TypeError. Klasa pochodna musi zaimplementować wymagane metody, aby dało się utworzyć jej instancję.

[Dokumentacja](https://docs.python.org/3.13/library/abc.html) · [Zadania lekcji](README.md)
