# Temat 23. unittest i asercje

## Składnia pod ręką

| Zapis | Do czego służy | Wynik lub ważna reguła |
| --- | --- | --- |
| `class TestX(unittest.TestCase):` | Klasa testów | Testy są metodami instancji. |
| `def test_przypadek(self):` | Metoda wykrywana jako test | Domyślna nazwa zaczyna się od test. |
| `self.assertEqual(a, b)` | Porównanie wartości | Niezgodność oznacza FAIL. |
| `self.assertTrue(warunek)` | Sprawdzenie prawdziwości | Dodaj konkretny warunek. |
| `self.assertIsNone(wynik)` | Sprawdzenie None | Nie myli z False ani 0. |
| `with self.assertRaises(ValueError):` | Oczekiwanie wyjątku | Brak wyjątku oznacza FAIL. |
| `python -m unittest -v test_modul` | Uruchomienie modułu testów | Polecenie terminalu, bez .py w nazwie modułu. |
| `python -m unittest discover -v` | Wyszukanie testów | Domyślnie pliki test*.py. |

## Krótki wzorzec

```python
import unittest

class TestNapis(unittest.TestCase):
    def test_wielkie_litery(self):
        self.assertEqual("kot".upper(), "KOT")

    def test_bledna_konwersja(self):
        with self.assertRaises(ValueError):
            int("kot")

if __name__ == "__main__":
    unittest.main()
```

FAIL oznacza niespełnioną asercję. ERROR oznacza inny nieobsłużony wyjątek. Zero znalezionych testów nie potwierdza poprawności programu.

[Dokumentacja](https://docs.python.org/3.13/library/unittest.html) · [Zadania lekcji](README.md)
