# Temat 52. Zadanie 2. Interfejs .ui
# Starter do uzupełnienia, bez rozwiązania.
# Pełne polecenie: README lekcji.
# TODO: Spakuj formularz z tematu 32, używający loadUi.
# TODO: Dołącz okno.ui przez --add-data i odczytuj ścieżkę względem __file__.
# TODO: Sprawdź uruchomienie paczki z folderu o innej ścieżce.

import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout

def zbuduj_okno():
    okno = QWidget()
    uklad = QVBoxLayout(okno)
    # TODO: dodaj kontrolki i układy opisane w tym zadaniu.
    return okno

if __name__ == "__main__":
    app = QApplication(sys.argv)
    okno = zbuduj_okno()
    okno.show()
    sys.exit(app.exec())

