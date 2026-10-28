# Temat 56. Pydantic 2 i walidacja

## Składnia pod ręką

| Zapis | Do czego służy | Wynik lub ważna reguła |
| --- | --- | --- |
| `class Dane(BaseModel):` | Model danych | Import BaseModel z pydantic. |
| `nazwa: str` | Wymagane pole | Brak wartości domyślnej oznacza obowiązek podania. |
| `Field(min_length=1, max_length=40)` | Ograniczenie długości | Dotyczy długości napisu. |
| `Field(ge=0, le=10), Field(gt=0)` | Granice liczb | ge/le włącznie, gt wyłącznie. |
| `Field(default_factory=list)` | Nowa domyślna lista | Funkcja zostanie użyta przy tworzeniu modelu. |
| `@field_validator("nazwa")` | Własna walidacja pola | Validator zwraca poprawną wartość albo zgłasza błąd. |
| `model.model_dump()` | Model na słownik | API Pydantic 2. |
| `Model.model_validate(dane)` | Utworzenie i walidacja modelu | Błędne dane powodują ValidationError. |

## Krótki wzorzec

```python
from pydantic import BaseModel, Field

class Kolor(BaseModel):
    nazwa: str = Field(min_length=1, max_length=40)
    jasnosc: int = Field(ge=0, le=100)

kolor = Kolor(nazwa="zielony", jasnosc=70)
print(kolor.model_dump())
# {'nazwa': 'zielony', 'jasnosc': 70}
```

Domyślnie część danych może być konwertowana, np. napis na liczbę. Samo min_length=1 nie odrzuca napisu ze spacjami. Do tego potrzebne jest strip i odpowiednia walidacja.

[Dokumentacja](https://docs.pydantic.dev/latest/concepts/fields/) · [Zadania lekcji](README.md)
