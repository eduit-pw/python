# Temat 46. Wyjaśnienia do praktyki

## Połączenie SQLite

sqlite3.connect otwiera bazę. Połączenie wymaga zamknięcia. with db zatwierdza albo wycofuje transakcję, ale samo nie zamyka połączenia.

## Parametry SQL

Wartości przekazuj osobno przez ?, np. execute(sql, (tytul, rok)). Krotka jednoelementowa potrzebuje przecinka. Apostrof w tytule jest wtedy daną, a nie częścią składni SQL.

## CRUD po ID

SELECT odczytuje, INSERT dodaje, UPDATE zmienia, DELETE usuwa. Zmiany filtruj po identyfikatorze, nie po numerze wiersza interfejsu. Sprawdź rowcount lub brak rekordu.

## Ograniczenia i transakcja

NOT NULL, CHECK i klucze wspierają spójność bazy. Jeśli druga operacja transakcji naruszy ograniczenie, wycofaj całość. Obsłuż IntegrityError poza blokiem transakcji.

## Odświeżenie widoku

Po udanym zapisie odczytaj dane ponownie i uaktualnij tabelę. Po odrzuconej operacji pozostaw dane i wyświetl komunikat. Inicjalizacja nie powinna dopisywać rekordów przy każdym starcie.

[Zadania i wyniki kontrolne](README.md)

To uzupełnienie przykładów z prezentacji. Definicje i kontrakty zadań czytaj łącznie. Szczegółowe przykłady są również w tekście prezentacji dołączonym do paczki.
