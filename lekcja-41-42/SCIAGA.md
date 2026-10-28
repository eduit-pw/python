# Temat 21. Obsługa wyjątków

## Składnia pod ręką

| Zapis | Do czego służy | Wynik lub ważna reguła |
| --- | --- | --- |
| `try:` | Blok kodu, który może zgłosić wyjątek | Ogranicz go do operacji wymagających obsługi. |
| `except ValueError as blad:` | Obsługa konkretnego typu błędu | blad przechowuje obiekt wyjątku. |
| `except (TypeError, ValueError):` | Wspólna obsługa kilku typów | Nawiasy zawierają krotkę typów. |
| `else: po except` | Kod po udanym try | Wykonuje się, gdy try nie zgłosi wyjątku. |
| `finally:` | Sprzątanie przy opuszczaniu try | Zwykle także po wyjątku lub return. |
| `raise` | Ponowne zgłoszenie aktualnego wyjątku | Użycie wewnątrz jego obsługi. |
| `ValueError, TypeError` | Zła wartość i nieodpowiedni typ | Np. int("abc") oraz 1 + "a". |
| `IndexError, KeyError` | Brak indeksu i brak klucza | Np. [][0] oraz {}["x"]. |

## Krótki wzorzec

```python
tekst = "12a"
try:
    liczba = int(tekst)
except ValueError:
    print("Niepoprawna liczba")
else:
    print(liczba * 2)
```

Bardziej szczegółowe except zapisuj przed ogólnymi. Unikaj pustego except, które ukrywa przyczynę błędu.

[Dokumentacja](https://docs.python.org/3.13/tutorial/errors.html) · [Zadania lekcji](README.md)
