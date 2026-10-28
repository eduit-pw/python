# Temat 63. requests i zewnętrzne API

## Składnia pod ręką

| Zapis | Do czego służy | Wynik lub ważna reguła |
| --- | --- | --- |
| `requests.get(url, timeout=5)` | Żądanie GET | Podawaj limit czasu oczekiwania. |
| `params={"q": "tekst"}` | Parametry query | Biblioteka koduje je w URL. |
| `headers={"Authorization": f"Bearer {token}"}` | Nagłówek tokenu | Token wczytuj z konfiguracji. |
| `requests.post(url, json=dane, timeout=5)` | Wysłanie JSON | Nie myl z data=, które ma inne zastosowanie. |
| `r.status_code, r.headers` | Status i nagłówki odpowiedzi | Dostępne po odebraniu odpowiedzi. |
| `r.raise_for_status()` | Zgłoszenie błędu dla statusu 4xx/5xx | Może zgłosić HTTPError. |
| `r.json()` | Parsowanie body JSON | Może zawieść także przy statusie 200. |
| `requests.RequestException` | Wspólna baza błędów requests | Nie zastępuje walidacji schematu danych. |

## Krótki wzorzec

```python
import requests

zadanie = requests.Request(
    "GET", "http://127.0.0.1:8000/szukaj",
    params={"q": "zielony kolor"}
).prepare()
print(zadanie.url)
# http://127.0.0.1:8000/szukaj?q=zielony+kolor
```

Przykład tylko przygotowuje żądanie, bez połączenia z siecią. timeout nie jest ścisłym limitem łącznego czasu całego pobierania. Nie zapisuj tokenów w kodzie ani logach.

[Dokumentacja](https://requests.readthedocs.io/en/latest/user/quickstart/) · [Zadania lekcji](README.md)
