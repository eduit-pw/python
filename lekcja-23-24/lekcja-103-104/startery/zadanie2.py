"""Temat 52. Zadanie 2: interfejs odczytany z pliku .ui przy starcie."""

import sys
from pathlib import Path

from PyQt6 import uic
from PyQt6.QtWidgets import QApplication


def main():
    app = QApplication(sys.argv)
    sciezka = Path(__file__).with_name("okno.ui")
    okno = uic.loadUi(str(sciezka))

    def powitaj():
        imie = okno.imieEdit.text().strip()
        okno.wynikLabel.setText(f"Witaj, {imie}" if imie else "Podaj imię")

    okno.powitajButton.clicked.connect(powitaj)
    okno.show()
    return app.exec()


if __name__ == "__main__":
    sys.exit(main())
