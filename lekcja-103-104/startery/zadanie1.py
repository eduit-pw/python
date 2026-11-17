# Temat 52. Zadanie 1. Paczka onedir
# Starter do uzupełnienia, bez rozwiązania.
# Pełne polecenie: README lekcji.
# TODO: Sprawdź działanie main.py, potem zbuduj --onedir z widoczną konsolą.
# TODO: Skopiuj cały dist/main do nowego folderu testowego.
# TODO: Uruchom plik wynikowy z tego folderu. Zanotuj brakujące zasoby lub błędy.

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

