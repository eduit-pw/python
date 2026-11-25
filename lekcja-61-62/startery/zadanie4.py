"""Temat 31. Zadanie 4. Obszar centralny okna głównego."""

import sys

from PyQt6.QtWidgets import QApplication, QLabel, QMainWindow


def zbuduj_okno():
    okno = QMainWindow()
    okno.resize(500, 300)
    # TODO: ustaw tytuł zgodnie z podglądem.
    # TODO: utwórz etykietę i ustaw ją jako centralną kontrolkę okna.
    return okno


if __name__ == "__main__":
    app = QApplication(sys.argv)
    okno = zbuduj_okno()
    okno.show()
    sys.exit(app.exec())
