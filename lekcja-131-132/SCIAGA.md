# Temat 63. Wyjaśnienia do praktyki

## requests i odpowiedź

requests.get(url, params=..., timeout=...) zwraca Response. status_code opisuje status, text treść jako napis, json() próbuje odczytać JSON. Samo udane połączenie nie dowodzi sukcesu HTTP.

## raise_for_status

raise_for_status zgłasza błąd dla odpowiedzi HTTP 4xx/5xx. Błąd HTTP, timeout, połączenie i niepoprawny JSON wymagają odróżnienia. Nie zastępuj ich pustą poprawną listą.

## Query i nagłówki

params koduje parametry adresu. headers przekazuje nagłówki, json= buduje ciało JSON. Nie sklejaj ręcznie query z tekstem, jeśli API udostępnia params.

## Token

Token pobierz ze środowiska i przekaż w wymaganym nagłówku. Nie wypisuj go w logu ani nie zapisuj do repozytorium. Lokalny token demonstracyjny nie jest kontem rzeczywistego dostawcy.

## Schemat danych

Sprawdź typ kolekcji i wymagane pola odpowiedzi przed obliczeniem. Błędne dane dostawcy są innym problemem niż brak odpowiedzi sieci. Ustal zachowanie dla pustej listy.

[Zadania i wyniki kontrolne](README.md)

To uzupełnienie przykładów z prezentacji. Definicje i kontrakty zadań czytaj łącznie. Szczegółowe przykłady są również w tekście prezentacji dołączonym do paczki.
