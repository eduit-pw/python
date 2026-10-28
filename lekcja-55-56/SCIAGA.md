# Temat 27. Pliki tekstowe

## Składnia pod ręką

| Zapis | Do czego służy | Wynik lub ważna reguła |
| --- | --- | --- |
| `open(sciezka, "r", encoding="utf-8")` | Otwarcie do odczytu | Brak pliku powoduje FileNotFoundError. |
| `open(sciezka, "w", encoding="utf-8")` | Otwarcie do zapisu | Istniejąca treść zostaje usunięta przy otwarciu. |
| `open(sciezka, "a", encoding="utf-8")` | Dopisywanie na końcu | Tworzy plik, jeśli go nie ma. |
| `with open(...) as plik:` | Automatyczne zamknięcie | Także przy wyjątku w bloku. |
| `plik.read()` | Odczyt od bieżącej pozycji do końca | Zwraca str w trybie tekstowym. |
| `for wiersz in plik:` | Czytanie kolejnych wierszy | Wiersz zwykle zawiera końcowe \n. |
| `plik.write(tekst)` | Zapis napisu | Nie dodaje znaku nowej linii, zwraca liczbę zapisanych znaków. |
| `plik.seek(0)` | Powrót do początku | Kolejny read zacznie od początku. |

## Krótki wzorzec

```python
from tempfile import TemporaryDirectory
from pathlib import Path

with TemporaryDirectory() as folder:
    sciezka = Path(folder) / "pokaz.txt"
    with open(sciezka, "w", encoding="utf-8") as plik:
        plik.write("Pierwszy\nDrugi\n")
    with open(sciezka, encoding="utf-8") as plik:
        print(plik.readline().rstrip("\n"))  # Pierwszy
```

Ścieżka względna jest liczona od folderu roboczego procesu. rstrip("\n") usuwa końce wierszy, strip() może usunąć również znaczące spacje.

[Dokumentacja](https://docs.python.org/3.13/tutorial/inputoutput.html#reading-and-writing-files) · [Zadania lekcji](README.md)
