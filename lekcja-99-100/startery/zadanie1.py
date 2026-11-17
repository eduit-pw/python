# Temat 50. Zadanie 1. Utwórz i odczytaj bazę.
import sqlite3
from pathlib import Path

sciezka = Path(__file__).with_name("albumy.db")
db = sqlite3.connect(sciezka)
try:
    with db:
        # TODO: utwórz tabelę i dodaj rekordy parametrami SQL.
        pass
    # TODO: wykonaj odczyt uporządkowany według ID i wyświetl wyniki.
finally:
    db.close()
