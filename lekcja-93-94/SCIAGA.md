# Temat 46. SQLite i GUI

## Składnia pod ręką

| Zapis | Do czego służy | Wynik lub ważna reguła |
| --- | --- | --- |
| `sqlite3.connect(sciezka)` | Otwarcie połączenia | ":memory:" tworzy bazę w pamięci. |
| `db.execute(sql, parametry)` | Wykonanie instrukcji | Wartości przekazuj przez placeholdery ?. |
| `db.execute("... WHERE id = ?", (id,))` | Parametr jednoelementowy | Przecinek tworzy krotkę. |
| `kursor.fetchall(), kursor.fetchone()` | Wszystkie wiersze lub jeden | fetchone zwraca None przy braku danych. |
| `db.commit(), db.rollback()` | Zatwierdzenie i cofnięcie transakcji | Nie zamykają połączenia. |
| `with db:` | Kontekst transakcji | Zatwierdza lub cofa otwartą transakcję, nie zamyka połączenia. |
| `db.close()` | Zamknięcie połączenia | Zadbaj o nie także przy błędzie. |
| `sqlite3.IntegrityError` | Naruszenie ograniczeń | Np. UNIQUE lub NOT NULL. |

## Krótki wzorzec

```python
import sqlite3
from contextlib import closing

with closing(sqlite3.connect(":memory:")) as db:
    db.execute("CREATE TABLE kolory (id INTEGER PRIMARY KEY, nazwa TEXT)")
    with db:
        db.execute("INSERT INTO kolory (nazwa) VALUES (?)", ("zielony",))
    print(db.execute("SELECT nazwa FROM kolory").fetchone())
    # ('zielony',)
```

Po udanym zapisie odśwież widok GUI. Placeholdery służą do wartości, a nazw tabel i kolumn nie przekazuj jako parametrów SQL.

[Dokumentacja](https://docs.python.org/3.13/library/sqlite3.html) · [Zadania lekcji](README.md)
