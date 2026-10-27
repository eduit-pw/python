# Temat 57. Wyjaśnienia do praktyki

## CRUD i metoda

GET odczytuje, POST tworzy, PUT w tej umowie zastępuje dane istniejącego rekordu, DELETE usuwa. Każda operacja ma określony adres, status i format odpowiedzi.

## ID niezależne od pozycji

Identyfikator pozostaje z rekordem po usunięciu innych danych. Nie wyliczaj nowego ID jako długość listy +1, jeśli grozi to powtórzeniem istniejącego numeru.

## Walidacja przed zmianą

Błędny schemat daje 422 bez modyfikowania stanu. Nieistniejący rekord daje 404. Po odrzuconym PUT wcześniejsze dane muszą pozostać.

## DELETE bez JSON

Status 204 oznacza brak treści. Nie zwracaj słownika ani nie próbuj odczytywać JSON z takiej odpowiedzi. Drugie usunięcie tego samego brakującego ID daje 404 według umowy.

## Pamięć procesu

Lista w module nie jest trwałą bazą. Restart lub przeładowanie może usunąć dane. Testową sekwencję wykonuj bez zmiany kodu, gdy chcesz obserwować ciągłość tego samego stanu.

[Zadania i wyniki kontrolne](README.md)

To uzupełnienie przykładów z prezentacji. Definicje i kontrakty zadań czytaj łącznie. Szczegółowe przykłady są również w tekście prezentacji dołączonym do paczki.
