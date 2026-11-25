import sqlite3
from pathlib import Path
from contextlib import contextmanager

SCIEZKA = Path(__file__).with_name("albumy.db")

# Skrypty okienkowe ustawiają SCIEZKA przed pierwszym połączeniem.
# W polacz() użyj tej wartości, aby otworzyć bazę danego zadania.

@contextmanager
def polacz():
    raise NotImplementedError('Uzupełnij rozwiązanie według polecenia.')

def inicjalizuj():
    raise NotImplementedError('Uzupełnij rozwiązanie według polecenia.')

def odczytaj():
    raise NotImplementedError('Uzupełnij rozwiązanie według polecenia.')

def dodaj(tytul, rok):
    raise NotImplementedError('Uzupełnij rozwiązanie według polecenia.')

def zmien(identyfikator, tytul, rok):
    raise NotImplementedError('Uzupełnij rozwiązanie według polecenia.')

def usun(identyfikator):
    raise NotImplementedError('Uzupełnij rozwiązanie według polecenia.')
