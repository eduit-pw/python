# Temat 58. Swagger UI i próby API

## Składnia pod ręką

| Zapis | Do czego służy | Wynik lub ważna reguła |
| --- | --- | --- |
| `/openapi.json` | Schemat OpenAPI | Opisuje ścieżki, modele i odpowiedzi. |
| `/docs` | Domyślny Swagger UI | Interfejs do przeglądania i wywoływania API. |
| `Try it out / Execute` | Rzeczywiste wywołanie endpointu | Operacja może zmienić dane. |
| `Metoda + URL + nagłówki + body` | Opis żądania | Zachowaj wszystkie istotne elementy w raporcie błędu. |
| `Status + nagłówki + body` | Opis odpowiedzi | Sam status 200 nie dowodzi poprawnej treści. |
| `POST, GET, PUT, GET, DELETE, GET` | Przykładowy cykl CRUD | Ostatni GET usuniętego rekordu powinien sprawdzić brak. |
| `Próba negatywna` | Błędne dane lub nieistniejące ID | Sprawdź też, czy stan pozostał poprawny. |

## Krótki wzorzec

```http
GET /rekordy/999
Accept: application/json

# Oczekiwany status przy braku rekordu: 404
# Przykładowe body: {"detail": "Brak"}
```

To zapis żądania, nie kod Pythona. W Postmanie lub Swagger UI wybierz GET, wpisz pełny URL działającego lokalnego API i porównaj status oraz body.

[Dokumentacja](https://fastapi.tiangolo.com/tutorial/first-steps/) · [Zadania lekcji](README.md)
