# Temat 31. Zadanie 4. Dla chętnych: Okno główne
# Starter do uzupełnienia, bez rozwiązania.
# Pełne polecenie: README lekcji.
# TODO: Utwórz osobny program oparty na QMainWindow.
# TODO: Ustaw QLabel „Obszar centralny” przez setCentralWidget.
# TODO: Zwiększ rozmiar okna. Porównaj zachowanie z etykietą ustawioną przez move.

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

