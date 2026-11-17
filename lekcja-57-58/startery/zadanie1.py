# Temat 29. Zadanie 1. Inwentaryzacja folderu
# Starter do uzupełnienia, bez rozwiązania.
# Pełne polecenie: README lekcji.
# TODO: Utwórz cwiczenia/dane: a.txt z „ABC”, b.txt z „DE” (oba bez końcowej nowej linii) oraz pusty folder inne.
# TODO: Wypisz nazwy zwykłych plików, ich rozszerzenia i rozmiary w bajtach.
# TODO: Użyj stat().st_size. Posortuj wynik według nazw.

from pathlib import Path
from shutil import copy2
BAZA = Path(__file__).resolve().parent

def inwentaryzacja(folder):
    raise NotImplementedError('Uzupełnij rozwiązanie według polecenia.')
