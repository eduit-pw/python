# Temat 57. FastAPI: CRUD

## Składnia pod ręką

| Zapis | Do czego służy | Wynik lub ważna reguła |
| --- | --- | --- |
| `@app.get("/rekordy")` | Pobranie kolekcji | Określ strukturę odpowiedzi. |
| `@app.get("/rekordy/{id}")` | Pobranie rekordu | Zwykle 404, jeśli nie istnieje. |
| `@app.post("/rekordy", status_code=201)` | Utworzenie rekordu | Nadaj trwałe, unikalne ID. |
| `@app.put("/rekordy/{id}")` | Zastąpienie danych rekordu | Od częściowej aktualizacji odróżniaj PATCH. |
| `@app.delete("/rekordy/{id}", status_code=204)` | Usunięcie bez treści odpowiedzi | Nie zwracaj JSON przy 204. |
| `Response(status_code=204)` | Pusta odpowiedź | Import Response z fastapi. |
| `HTTPException(status_code=404, detail="Brak")` | Informacja o braku rekordu | Zgłaszaj przez raise. |
| `Walidacja przed modyfikacją` | Zachowanie stanu przy błędzie | Nie zapisuj częściowo sprawdzonego rekordu. |

## Krótki wzorzec

```python
from fastapi import FastAPI, HTTPException

app = FastAPI()
rekordy = {10: {"id": 10, "nazwa": "zielony"}}

@app.get("/rekordy/{id}")
def odczytaj(id: int):
    if id not in rekordy:
        raise HTTPException(status_code=404, detail="Brak")
    return rekordy[id]
```

Słownik przechowuje dane tylko w procesie. Restart je usuwa, a wiele procesów ma oddzielne kopie. len(rekordy) + 1 może powtórzyć wcześniej użyte ID.

[Dokumentacja](https://fastapi.tiangolo.com/tutorial/response-status-code/) · [Zadania lekcji](README.md)
