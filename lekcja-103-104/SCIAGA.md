# Temat 50. HTTP i klient API

## Składnia pod ręką

| Zapis | Do czego służy | Wynik lub ważna reguła |
| --- | --- | --- |
| `GET, POST, PUT, DELETE` | Odczyt, utworzenie, zastąpienie i usunięcie | Znaczenie szczegółowe określa umowa API. |
| `URL i query, np. ?limit=5` | Adres zasobu i parametry | Parametry query są częścią URL. |
| `Content-Type: application/json` | Deklaracja typu treści | Nie zastępuje walidacji danych. |
| `200, 201, 204` | Sukces, utworzenie, brak treści | Przy 204 nie oczekuj JSON w odpowiedzi. |
| `400, 404, 422, 500` | Wybrane kody błędów | Odpowiednio błędne żądanie, brak zasobu, błąd walidacji, błąd serwera. |
| `urlopen(url, timeout=5)` | Żądanie z biblioteki standardowej | Wynikiem jest obiekt odpowiedzi. |
| `odpowiedz.read().decode("utf-8")` | Bajty na napis | Kodowanie powinno pasować do treści. |
| `json.loads(tekst)` | Napis JSON na obiekt Python | Nie jest to żądanie HTTP. |

## Krótki wzorzec

```python
from urllib.request import Request

zadanie = Request("http://127.0.0.1:8000/status",
                  headers={"Accept": "application/json"}, method="GET")
print(zadanie.get_method())  # GET
print(zadanie.full_url)     # http://127.0.0.1:8000/status
```

Utworzenie Request nie wysyła żądania. Dopiero urlopen je wykonuje. Odpowiedź 404 oznacza kontakt z serwerem, a nie brak połączenia.

[Dokumentacja](https://docs.python.org/3.13/library/urllib.request.html) · [Zadania lekcji](README.md)
