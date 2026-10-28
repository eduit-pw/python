# Temat 55. FastAPI: endpointy

## Składnia pod ręką

| Zapis | Do czego służy | Wynik lub ważna reguła |
| --- | --- | --- |
| `app = FastAPI()` | Obiekt aplikacji | Import z fastapi. |
| `@app.get("/status")` | Powiązanie GET i ścieżki z funkcją | Dekorator umieszczasz nad funkcją. |
| `@app.get("/kolory/{id}")` | Parametr w ścieżce | Parametr funkcji id: int włącza walidację typu. |
| `limit: int = 10` | Typowy parametr query | Gdy nie jest parametrem ścieżki ani modelem ciała. |
| `return {"klucz": wartosc}` | Odpowiedź serializowana do JSON | Zwykle status 200. |
| `raise HTTPException(status_code=404, detail="Brak")` | Odpowiedź błędu | raise przerywa obsługę. |
| `python -m uvicorn main:app --reload` | Start lokalnego serwera | main to moduł main.py, app to obiekt aplikacji. |
| `/docs, /openapi.json` | Swagger UI i schemat API | Adresy domyślne. |

## Krótki wzorzec

```python
# main.py
from fastapi import FastAPI

app = FastAPI()

@app.get("/podwoj/{n}")
def podwoj(n: int):
    return {"wynik": n * 2}
```

Uruchom z folderu main.py. GET /podwoj/4 zwróci {"wynik": 8}, a niepoprawny parametr /podwoj/kot domyślnie odpowiedź walidacyjną 422.

[Dokumentacja](https://fastapi.tiangolo.com/tutorial/path-params/) · [Zadania lekcji](README.md)
