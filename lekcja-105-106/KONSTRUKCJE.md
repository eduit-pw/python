# Algorytm, pliki i testy: konstrukcje do powtórzenia

```python
def licz_dodatnie(dane):
    wynik = 0
    for liczba in dane:
        if liczba > 0:
            wynik += 1
    return wynik
```

`return` oddaje wynik. `None` może oznaczać brak wyniku. Porównuj je przez `is None`. Indeks 0 jest poprawną pozycją.

```python
import csv
import json

with open("dane.csv", encoding="utf-8", newline="") as plik:
    for rekord in csv.DictReader(plik, delimiter=";"):
        print(rekord)

with open("dane.json", "w", encoding="utf-8") as plik:
    json.dump({"gotowe": True}, plik, ensure_ascii=False, indent=2)
```

```python
import unittest

class TestPrzyklad(unittest.TestCase):
    def test_dodatnie(self):
        self.assertEqual(licz_dodatnie([-2, 0, 7]), 1)
```

Uruchomienie: `python -m unittest discover -v`. To fragmenty do powtórki. W pliku testowym zaimportuj badaną funkcję ze swojego modułu.
