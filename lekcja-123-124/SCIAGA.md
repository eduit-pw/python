# Temat 60. Testy API

## Składnia pod ręką

| Zapis | Do czego służy | Wynik lub ważna reguła |
| --- | --- | --- |
| `from fastapi.testclient import TestClient` | Lokalny klient testowy | Nie wymaga uruchomionego Uvicorn. |
| `with TestClient(app) as klient:` | Klient wraz z lifespan | Start i zakończenie aplikacji obejmują blok. |
| `klient.get("/adres")` | Żądanie GET | Zwraca odpowiedź testową. |
| `klient.post("/adres", json=dane)` | Żądanie z JSON | Automatycznie koduje body. |
| `odpowiedz.status_code` | Kod odpowiedzi | Sprawdzaj konkretną oczekiwaną liczbę. |
| `odpowiedz.json()` | Body jako obiekt Python | Nie wywołuj dla pustej odpowiedzi 204. |
| `TemporaryDirectory()` | Tymczasowy katalog | Może zawierać osobną bazę każdego testu. |
| `Osobna baza i stan` | Izolacja testów | Wynik nie zależy od danych z ręcznego uruchomienia. |

## Krótki wzorzec

```python
from fastapi import FastAPI
from fastapi.testclient import TestClient

app = FastAPI()

@app.get("/status")
def status():
    return {"ok": True}

with TestClient(app) as klient:
    r = klient.get("/status")
    assert r.status_code == 200
    assert r.json() == {"ok": True}
```

Po POST lub PUT sprawdzaj także późniejszy GET i rzeczywiście zapisane dane. Przy 204 sprawdź brak treści zamiast próbować odczytać JSON.

[Dokumentacja](https://fastapi.tiangolo.com/advanced/testing-events/) · [Zadania lekcji](README.md)
