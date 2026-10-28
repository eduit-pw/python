# Temat 66. argparse i konfiguracja

## Składnia pod ręką

| Zapis | Do czego służy | Wynik lub ważna reguła |
| --- | --- | --- |
| `argparse.ArgumentParser(description="opis")` | Parser opcji CLI | Udostępnia automatyczne --help. |
| `parser.add_argument("plik")` | Argument pozycyjny | Użycie np. python raport.py dane.csv. |
| `parser.add_argument("--limit", type=int, default=10)` | Opcja liczbowa | Niepoprawny int zostanie odrzucony przez parser. |
| `parser.add_argument("--pelny", action="store_true")` | Flaga logiczna | Bez flagi False, z flagą True. |
| `args = parser.parse_args()` | Odczyt argumentów procesu | Wyniki jako args.nazwa. |
| `parser.error("opis")` | Błąd danych CLI | Komunikat i kod zakończenia 2. |
| `load_dotenv()` | Wczytanie .env | Biblioteka python-dotenv, domyślnie nie nadpisuje istniejących zmiennych. |
| `os.getenv("NAZWA", "domyślna")` | Odczyt konfiguracji | Wynik str lub wartość domyślna. |
| `sys.exit(kod)` | Zakończenie programu | 0 oznacza sukces, niezerowy kod błąd. |

## Krótki wzorzec

```python
import argparse

parser = argparse.ArgumentParser(description="Pokaz opcji")
parser.add_argument("--limit", type=int, default=10)
parser.add_argument("--pelny", action="store_true")
args = parser.parse_args()
print(args.limit, args.pelny)
# python pokaz.py --limit 3 --pelny
# Wynik: 3 True
```

Ustal kolejność: opcja CLI, zmienna środowiskowa, wartość domyślna. .env.example może zawierać nazwy i puste przykłady, a rzeczywisty .env pozostaw poza Git.

[Dokumentacja](https://docs.python.org/3.13/library/argparse.html) · [Zadania lekcji](README.md)
