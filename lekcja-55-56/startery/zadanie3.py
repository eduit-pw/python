# Temat 28. Zadanie 3. Albumy z pliku
# Starter do uzupełnienia, bez rozwiązania.
# Pełne polecenie: README lekcji.
# TODO: Utwórz dane.txt: Zespół Północ, Poranek, 8, 2024, 120 w osobnych wierszach.
# TODO: Dodaj drugi blok: Anna Nowak, Wieczór, 10, 2023, 80.
# TODO: Wczytaj rekordy do obiektów Album z pięcioma polami i wypisz ich dane.
# TODO: Jeżeli liczba wierszy nie jest wielokrotnością 5, zgłoś niepełny rekord. Adaptacja INF.04-02-24.06-SG, I: własne dane i kontrola kompletności.

from pathlib import Path
from dataclasses import dataclass
BAZA = Path(__file__).resolve().parent

@dataclass
class Album:
    artysta: str
    tytul: str
    utwory: int
    rok: int
    pobrania: int

def odczytaj_albumy(sciezka):
    raise NotImplementedError('Uzupełnij rozwiązanie według polecenia.')
