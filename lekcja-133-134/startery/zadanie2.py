# Temat 67. Zadanie 2. Eksport CSV
# Starter do uzupełnienia, bez rozwiązania.
# Pełne polecenie: README lekcji.
# TODO: Zapisz odczytane dane do albumy.csv przez csv.DictWriter, separator ;.
# TODO: Kolumny: id, tytul, pobrania. Użyj UTF-8 i newline="".
# TODO: Wczytaj zapisany plik ponownie i sprawdź wiersze.

import csv
from pathlib import Path
from bs4 import BeautifulSoup
BAZA = Path(__file__).resolve().parent

def odczytaj(tekst):
    raise NotImplementedError('Uzupełnij rozwiązanie według polecenia.')
