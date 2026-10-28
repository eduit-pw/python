# Temat 30. Wyrażenia regularne

## Składnia pod ręką

| Zapis | Do czego służy | Wynik lub ważna reguła |
| --- | --- | --- |
| `r"wzorzec"` | Surowy napis Pythona | Ułatwia zapis ukośników używanych przez re. |
| `re.fullmatch(wzorzec, tekst)` | Dopasowanie całego tekstu | Zwraca Match albo None. |
| `re.search(wzorzec, tekst)` | Szukanie pierwszego fragmentu | Nie wymaga dopasowania całego tekstu. |
| `re.findall(wzorzec, tekst)` | Lista dopasowań | Grupy przechwytujące wpływają na kształt wyniku. |
| `re.sub(wzorzec, zamiana, tekst)` | Zastąpienie dopasowań | Zwraca nowy napis. |
| `[A-Z], [0-9]` | Klasa znaków | W tych zapisach wyłącznie wskazane zakresy ASCII. |
| `\d, \w, \s` | Cyfra, znak słowa, biały znak | Domyślnie uwzględniają Unicode dla napisów. |
| `?, *, +, {m,n}` | Liczba powtórzeń | Odpowiednio 0..1, 0+, 1+, m..n. |
| `(...), m.group(1)` | Grupa i jej odczyt | Najpierw sprawdź, czy m nie jest None. |

## Krótki wzorzec

```python
import re

m = re.fullmatch(r"([A-Z]{2})-([0-9]{3})", "AB-123")
if m is not None:
    print(m.group(1), m.group(2))  # AB 123
```

Wzorzec daty może sprawdzić format, lecz nie musi sprawdzać istnienia daty w kalendarzu. Do reguł kalendarza użyj datetime.

[Dokumentacja](https://docs.python.org/3.13/library/re.html) · [Zadania lekcji](README.md)
