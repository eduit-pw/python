# Temat 28. pathlib i ścieżki

## Składnia pod ręką

| Zapis | Do czego służy | Wynik lub ważna reguła |
| --- | --- | --- |
| `from pathlib import Path` | Klasa ścieżek | Sam Path nie tworzy pliku. |
| `Path("dane") / "plik.txt"` | Złożenie ścieżki | Operator / dodaje składnik ścieżki. |
| `Path.cwd()` | Bieżący folder procesu | Może zależeć od sposobu uruchomienia. |
| `Path(__file__).resolve().parent` | Folder bieżącego skryptu | __file__ nie występuje w każdej konsoli interaktywnej. |
| `p.exists(), p.is_file(), p.is_dir()` | Sprawdzenie zasobu | Wynik bool. |
| `p.mkdir(parents=True, exist_ok=True)` | Utworzenie folderu z rodzicami | Nie zgłasza błędu dla istniejącego katalogu. |
| `p.iterdir(), p.glob("*.txt")` | Przegląd katalogu i dopasowania | Zwracają iteratory ścieżek. |
| `p.name, p.stem, p.suffix, p.parent` | Składowe ścieżki | Np. dane.txt, dane, .txt i katalog nadrzędny. |
| `p.read_text(encoding="utf-8")` | Odczyt całego pliku | Zwraca str, zamyka plik. |

## Krótki wzorzec

```python
from pathlib import Path

p = Path("dane") / "pomiary.csv"
print(p.name)    # pomiary.csv
print(p.stem)    # pomiary
print(p.suffix)  # .csv
```

Istnienie pliku sprawdzone przed open nie gwarantuje, że operacja później się powiedzie. Błędy odczytu nadal wymagają obsługi.

[Dokumentacja](https://docs.python.org/3.13/library/pathlib.html) · [Zadania lekcji](README.md)
