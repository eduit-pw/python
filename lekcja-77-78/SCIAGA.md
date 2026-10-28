# Temat 38. Daty i czas

## Składnia pod ręką

| Zapis | Do czego służy | Wynik lub ważna reguła |
| --- | --- | --- |
| `date(rok, miesiac, dzien)` | Data kalendarzowa | Nieistniejąca data powoduje ValueError. |
| `datetime(...)` | Data z godziną | Bez tzinfo jest pozbawiona informacji o strefie. |
| `date.fromisoformat("2026-10-27")` | Odczyt daty ISO | Wynik date. |
| `datetime.strptime(tekst, "%d.%m.%Y")` | Parsowanie według formatu | Niepasujący zapis powoduje ValueError. |
| `data.strftime("%Y-%m-%d")` | Formatowanie do napisu | Wynik str. |
| `koniec - poczatek` | Różnica dat lub czasu | Wynik timedelta. |
| `timedelta(days=1), roznica.total_seconds()` | Przedział i łączna liczba sekund | roznica.seconds pomija pełne dni. |
| `datetime.now(timezone.utc)` | Bieżący czas ze strefą UTC | Obiekt świadomy strefy. |

## Krótki wzorzec

```python
from datetime import date, timedelta

poczatek = date.fromisoformat("2026-10-27")
koniec = poczatek + timedelta(days=3)
print(koniec.isoformat())       # 2026-10-30
print((koniec - poczatek).days)  # 3
```

%m oznacza miesiąc, %M minuty. Porównuj daty, a nie napisy w przypadkowym formacie. Dla godzin ustal zasady stref czasowych.

[Dokumentacja](https://docs.python.org/3.13/library/datetime.html) · [Zadania lekcji](README.md)
