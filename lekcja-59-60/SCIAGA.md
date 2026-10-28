# Temat 29. CSV i JSON

## Składnia pod ręką

| Zapis | Do czego służy | Wynik lub ważna reguła |
| --- | --- | --- |
| `csv.reader(plik, delimiter=";")` | Odczyt wierszy CSV | Zwykle lista napisów w każdym wierszu. |
| `csv.DictReader(plik, delimiter=";")` | Odczyt według nagłówków | Wartości pól zwykle pozostają str. |
| `csv.writer(plik).writerow(dane)` | Zapis jednego wiersza | Obsługuje cytowanie separatorów. |
| `csv.DictWriter(plik, fieldnames=...)` | Zapis słowników | writeheader() zapisuje nagłówek. |
| `open(..., newline="", encoding="utf-8")` | Plik dla modułu csv | Pozwala csv obsłużyć końce wierszy. |
| `json.load(plik), json.dump(dane, plik)` | JSON w pliku | Odczyt obiektu i zapis. |
| `json.loads(tekst), json.dumps(dane)` | JSON w napisie | loads odczytuje, dumps zwraca str. |
| `ensure_ascii=False, indent=2` | Opcje zapisu JSON | Czytelne znaki Unicode i wcięcia. |

## Krótki wzorzec

```python
import csv
import json
from io import StringIO

plik = StringIO("nazwa;sztuki\nzeszyt;3\n")
wiersz = next(csv.DictReader(plik, delimiter=";"))
wiersz["sztuki"] = int(wiersz["sztuki"])
print(json.dumps(wiersz, ensure_ascii=False))
# {"nazwa": "zeszyt", "sztuki": 3}
```

Poprawna składnia JSON nie dowodzi zgodności ze schematem. Sprawdź wymagane klucze, typy i zakresy wartości.

[Dokumentacja](https://docs.python.org/3.13/library/csv.html) · [Zadania lekcji](README.md)
