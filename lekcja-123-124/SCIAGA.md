# Temat 60. Wyjaśnienia do praktyki

## TestClient

TestClient wywołuje aplikację w teście bez osobnego serwera Uvicorn. Otrzymujesz odpowiedź ze status_code, json i content. Wymagane zależności testowe muszą być zainstalowane.

## Start aplikacji w teście

with TestClient(app) uruchamia cykl lifespan. Samo utworzenie obiektu klienta poza kontekstem nie jest równoważnym sprawdzeniem startu aplikacji.

## Baza tymczasowa

W setUp utwórz osobną ścieżkę i zachowaj poprzednią konfigurację. W tearDown zamknij klienta, przywróć konfigurację i usuń katalog. Nie testuj usuwania na bazie użytkownika.

## Asercje odpowiedzi

Sprawdź status, pola i wartości. Dla DELETE 204 sprawdź puste content. Po błędnym POST odczytaj listę, aby wykryć ewentualny częściowy zapis.

## Wykrywanie regresji

Celowo zmień jeden status w kopii i zobacz nieudany test. Przywróć poprawną implementację i uruchom pełny zestaw. Przejście kilku testów nie dowodzi pokrycia wszystkich możliwych danych.

[Zadania i wyniki kontrolne](README.md)

To uzupełnienie przykładów z prezentacji. Definicje i kontrakty zadań czytaj łącznie. Szczegółowe przykłady są również w tekście prezentacji dołączonym do paczki.
