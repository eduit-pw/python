# Temat 52. Zadanie 3. Trwała baza
# Starter do uzupełnienia, bez rozwiązania.
# Pełne polecenie: README lekcji.
# TODO: W projekcie albumów umieść bazę w AppDataLocation, także przed pakowaniem.
# TODO: Dodaj rekord, zamknij program i uruchom go ponownie.
# TODO: Zbuduj onefile i powtórz test. Wypisz w URUCHOMIENIE.md faktyczne miejsce bazy.

import sys
import sqlite3
from pathlib import Path
from PyQt6.QtCore import QStandardPaths
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout

def zbuduj_okno():
    okno = QWidget()
    uklad = QVBoxLayout(okno)
    # TODO: wyznacz AppDataLocation i utwórz tam folder trwałej bazy.
    # TODO: wykorzystaj tutaj własny kod albumów z poprzedniego tematu.
    return okno

if __name__ == "__main__":
    app = QApplication(sys.argv)
    okno = zbuduj_okno()
    okno.show()
    sys.exit(app.exec())

