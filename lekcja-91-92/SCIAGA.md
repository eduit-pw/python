# Temat 45. Wyjaśnienia do praktyki

## QListWidget

Lista przechowuje elementy do wyboru. currentItem może być None przy braku zaznaczenia. Sprawdź ten przypadek przed wywołaniem text.

## QTableWidget

Ustal liczbę kolumn, nagłówki i wiersze. Każda komórka zawiera QTableWidgetItem. Pusta lub nieutworzona komórka może dać None przy odczycie.

## Identyfikator rekordu

Numer wiersza zmienia się po sortowaniu. ID rekordu pozostaje jego tożsamością. Przechowuj ID w danych elementu lub odpowiedniej kolumnie, nie odtwarzaj go z pozycji.

## Sortowanie liczb

Tekstowe 10 może znaleźć się przed 2. W DisplayRole zapisz int, aby tabela porównywała liczby. Podczas wypełniania wyłącz sortowanie do czasu zakończenia zapisu komórek.

## Zaznaczanie i edycja

SingleSelection oraz SelectRows upraszczają wybór jednego rekordu. Wyłącz edycję komórek, jeśli zmiany mają przechodzić przez formularz. Obsłuż pustą tabelę.

[Zadania i wyniki kontrolne](README.md)

To uzupełnienie przykładów z prezentacji. Definicje i kontrakty zadań czytaj łącznie. Szczegółowe przykłady są również w tekście prezentacji dołączonym do paczki.
