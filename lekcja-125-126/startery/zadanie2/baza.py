import sqlite3
from pathlib import Path
from contextlib import contextmanager

@contextmanager
def polacz():
    raise NotImplementedError('Uzupełnij rozwiązanie według polecenia.')

def inicjalizuj():
    raise NotImplementedError('Uzupełnij rozwiązanie według polecenia.')

def wszystkie():
    raise NotImplementedError('Uzupełnij rozwiązanie według polecenia.')

def znajdz(identyfikator):
    raise NotImplementedError('Uzupełnij rozwiązanie według polecenia.')

def dodaj(tytul, pobrania):
    raise NotImplementedError('Uzupełnij rozwiązanie według polecenia.')

def zmien(identyfikator, tytul, pobrania):
    raise NotImplementedError('Uzupełnij rozwiązanie według polecenia.')

def usun(identyfikator):
    raise NotImplementedError('Uzupełnij rozwiązanie według polecenia.')
