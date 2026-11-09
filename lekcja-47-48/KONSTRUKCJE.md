# Temat 24. Przygotowanie i izolacja testów

## Składnia pod ręką

| Zapis | Do czego służy | Wynik lub ważna reguła |
| --- | --- | --- |
| `setUp(self)` | Przygotowanie przed każdym testem | Ustawia świeży stan instancji testowej. |
| `tearDown(self)` | Sprzątanie po teście | Uruchamia się także po błędzie testu, jeśli setUp się powiodło. |
| `self.addCleanup(funkcja, ...)` | Rejestracja sprzątania | Wykona się także po nieudanym setUp, jeśli zarejestrowano ją wcześniej. |
| `with self.subTest(dane=x):` | Osobne raportowanie wariantów | Jeden błąd asercji nie przerywa pozostałych wariantów. |
| `io.StringIO()` | Tekstowy bufor w pamięci | Obsługuje m.in. write, read, seek, getvalue. |
| `bufor.seek(0)` | Przesunięcie odczytu na początek | Po zapisie kursor znajduje się dalej. |
| `bufor.getvalue()` | Pobranie całej treści | Nie wymaga seek(0). |
| `Przypadek graniczny` | Próba przy granicy kontraktu | Np. puste dane, zero, ostatni dozwolony indeks. |

## Krótki wzorzec

```python
import unittest
from io import StringIO

class TestBufor(unittest.TestCase):
    def setUp(self):
        self.bufor = StringIO()
        self.addCleanup(self.bufor.close)

    def test_odczyt(self):
        self.bufor.write("abc")
        self.bufor.seek(0)
        self.assertEqual(self.bufor.read(), "abc")

if __name__ == "__main__":
    unittest.main()
```

Każdy test powinien działać samodzielnie. Nie uzależniaj jego wyniku od kolejności uruchomienia innych testów.

[Dokumentacja](https://docs.python.org/3.13/library/unittest.html#organizing-test-code) · [Zadania lekcji](README.md)
