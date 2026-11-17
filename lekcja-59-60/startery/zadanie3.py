# Temat 30. Zadanie 3. Raport braków
# Starter do uzupełnienia, bez rozwiązania.
# Pełne polecenie: README lekcji.
# TODO: Utwórz CSV z nagłówkiem nazwa;ilosc i rekordami: Ołówek;0, Zeszyt;2, Gumka;0.
# TODO: Zapisz braki.csv: ten sam nagłówek, tylko produkty o ilości równej 0.
# TODO: Użyj DictWriter. Zachowaj kolejność rekordów.

import csv
import json
from pathlib import Path
BAZA = Path(__file__).resolve().parent
