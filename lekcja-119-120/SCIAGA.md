# Temat 58. Wyjaśnienia do praktyki

## OpenAPI i Swagger UI

/openapi.json opisuje operacje i schematy maszynowo. /docs prezentuje ten opis w interfejsie. Dokumentacja nie zastępuje sprawdzenia rzeczywistego zachowania.

## Scenariusz testowy

Zapisz metodę, adres, body i oczekiwany status przed żądaniem. ID z POST wykorzystaj w dalszych krokach zamiast zakładać stałą wartość z innego uruchomienia.

## Pełen cykl

Utwórz rekord, odczytaj, zmień, sprawdź zmianę, usuń i odczytaj brak. Po nieudanym zapisie sprawdź, że liczba rekordów i poprzednie dane są niezmienione.

## Próby negatywne

Oddziel brak pola, zły zakres, dodatkowe pole, brak zasobu i nieobsługiwaną metodę. Status i ciało błędu mają odpowiadać umowie.

## Raport usterki

Podaj kroki odtworzenia, dane, wynik oczekiwany i rzeczywisty. Zmiana statusu 201 na 200 może być błędem umowy mimo poprawnego JSON. Po naprawie powtórz próbę.

[Zadania i wyniki kontrolne](README.md)

To uzupełnienie przykładów z prezentacji. Definicje i kontrakty zadań czytaj łącznie. Szczegółowe przykłady są również w tekście prezentacji dołączonym do paczki.
