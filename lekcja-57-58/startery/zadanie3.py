# Temat 29. Zadanie 3. Raport niezależny od cwd
# Starter do uzupełnienia, bez rozwiązania.
# Pełne polecenie: README lekcji.
# TODO: W folderze skryptu utwórz dane/liczby.txt z liczbami 4, 7, -2.
# TODO: Zbuduj ścieżkę do tego pliku na podstawie __file__. Oblicz sumę.
# TODO: Uruchom skrypt z jego folderu oraz z folderu nadrzędnego.

from pathlib import Path
from shutil import copy2
BAZA = Path(__file__).resolve().parent
