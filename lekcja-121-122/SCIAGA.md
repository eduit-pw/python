# Temat 59. FastAPI i trwałość SQLite

## Składnia pod ręką

| Zapis | Do czego służy | Wynik lub ważna reguła |
| --- | --- | --- |
| `Warstwa endpointów` | HTTP, modele wejścia i statusy | Nie powinna duplikować wszystkich zapytań SQL. |
| `Warstwa repozytorium` | Operacje na bazie | Zwraca dane albo informację o braku. |
| `@asynccontextmanager` | Kontekst używany w lifespan | Kod przed yield przygotowuje, po yield sprząta. |
| `FastAPI(lifespan=lifespan)` | Cykl życia aplikacji | Służy np. do przygotowania struktury bazy. |
| `with sqlite3.connect(...) as db:` | Transakcja | Osobno zadbaj o zamknięcie połączenia. |
| `db.execute("... VALUES (?)", (wartosc,))` | Parametryzowany zapis | Chroni przed wstawianiem wartości do tekstu SQL. |
| `sqlite3.IntegrityError` | Naruszenie ograniczeń | Zmapuj znany konflikt na świadomą odpowiedź HTTP. |
| `Plik bazy na dysku` | Dane zachowane po restarcie | W kontenerze wymaga trwałego wolumenu. |

## Krótki wzorzec

```python
from contextlib import asynccontextmanager
from fastapi import FastAPI

@asynccontextmanager
async def lifespan(app: FastAPI):
    app.state.gotowa = True
    try:
        yield
    finally:
        app.state.gotowa = False

app = FastAPI(lifespan=lifespan)
```

Przykład pokazuje składnię lifespan. Zamiast flagi wstawiasz przygotowanie i zwolnienie rzeczywistych zasobów. Nie współdziel przypadkowo jednego połączenia SQLite między różnymi wątkami.

[Dokumentacja](https://fastapi.tiangolo.com/advanced/events/) · [Zadania lekcji](README.md)
