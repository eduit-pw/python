"""Temat 50. Zadanie 4. Sprawdź wycofanie transakcji w SQLite."""

import sqlite3
from contextlib import closing


def main():
    with closing(sqlite3.connect(":memory:")) as db:
        # TODO: utwórz tabelę albumy z ograniczeniem CHECK dla roku.
        # Zatwierdź utworzenie tabeli przed rozpoczęciem próby.
        # TODO: w jednej transakcji dodaj ("Dobry", 2024) i ("Błędny", 1800).
        # TODO: obsłuż sqlite3.IntegrityError poza blokiem transakcji.
        # TODO: odczytaj tabelę i sprawdź, ile rekordów pozostało.
        pass


if __name__ == "__main__":
    main()
