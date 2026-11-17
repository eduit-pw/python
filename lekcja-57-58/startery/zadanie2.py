# Temat 29. Zadanie 2. Kopia tekstów
# Starter do uzupełnienia, bez rozwiązania.
# Pełne polecenie: README lekcji.
# TODO: Dodaj do danych foto.png jako dowolny plik i podfolder inne/c.txt.
# TODO: Skopiuj tylko zwykłe pliki *.txt z danych do cwiczenia/kopie.
# TODO: Pomiń plik docelowy, jeśli już istnieje, i wypisz komunikat.

from pathlib import Path
from shutil import copy2
BAZA = Path(__file__).resolve().parent

def inwentaryzacja(folder):
    raise NotImplementedError('Uzupełnij rozwiązanie według polecenia.')

def kopiuj_teksty(zrodlo, cel):
    raise NotImplementedError('Uzupełnij rozwiązanie według polecenia.')
