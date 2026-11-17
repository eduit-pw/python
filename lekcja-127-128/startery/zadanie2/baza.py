import sqlite3
from pathlib import Path
from contextlib import contextmanager
SCIEZKA=Path(__file__).resolve().parent/"albumy.db"
@contextmanager
def polacz():
    db=sqlite3.connect(SCIEZKA)
    db.row_factory=sqlite3.Row
    try:
        with db:yield db
    finally:db.close()
def inicjalizuj():
    with polacz() as db:
        db.execute("CREATE TABLE IF NOT EXISTS albumy(id INTEGER PRIMARY KEY AUTOINCREMENT,tytul TEXT NOT NULL,pobrania INTEGER NOT NULL CHECK(pobrania>=0))")
def wszystkie():
    with polacz() as db:
        return [dict(w) for w in db.execute("SELECT id,tytul,pobrania FROM albumy ORDER BY id")]
def znajdz(identyfikator):
    with polacz() as db:
        w=db.execute("SELECT id,tytul,pobrania FROM albumy WHERE id=?",(identyfikator,)).fetchone()
        return dict(w) if w else None
def dodaj(tytul,pobrania):
    with polacz() as db:
        i=db.execute("INSERT INTO albumy(tytul,pobrania) VALUES(?,?)",(tytul,pobrania)).lastrowid
        return {"id":i,"tytul":tytul,"pobrania":pobrania}
def zmien(identyfikator,tytul,pobrania):
    with polacz() as db:
        return db.execute("UPDATE albumy SET tytul=?,pobrania=? WHERE id=?",(tytul,pobrania,identyfikator)).rowcount
def usun(identyfikator):
    with polacz() as db:
        return db.execute("DELETE FROM albumy WHERE id=?",(identyfikator,)).rowcount
