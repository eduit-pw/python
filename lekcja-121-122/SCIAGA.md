# Temat 59. Wyjaśnienia do praktyki

## Warstwa danych

Endpoint obsługuje HTTP, a moduł baza wykonuje SQL. Funkcje warstwy danych zwracają rekord albo informację o braku. Nie mieszaj obiektu odpowiedzi HTTP z wynikiem execute.

## Trwałość SQLite

Plik bazy zachowuje rekordy po restarcie. CREATE TABLE IF NOT EXISTS przygotowuje brakującą tabelę bez kasowania danych. Dane przykładowe nie powinny być dopisywane przy każdym starcie.

## Lifespan

Kontekst lifespan wykonuje przygotowanie przy starcie aplikacji i sprzątanie przy końcu. Utwórz tabelę przed obsługą żądań. Nie traktuj importu modułu jako zamiennika całego cyklu aplikacji.

## Parametry i ograniczenia

Parametry SQL oddzielają wartości od składni. CHECK(pobrania>=0) wspiera spójność zapisu. Apostrof w tytule powinien przejść jako zwykła dana.

## Błędy i transakcje

Brak rekordu przekłada się na 404 zgodnie z API. Błąd drugiego zapisu w transakcji wycofuje również pierwszy. Próbę wycofania wykonuj w osobnej bazie testowej.

[Zadania i wyniki kontrolne](README.md)

To uzupełnienie przykładów z prezentacji. Definicje i kontrakty zadań czytaj łącznie. Szczegółowe przykłady są również w tekście prezentacji dołączonym do paczki.
