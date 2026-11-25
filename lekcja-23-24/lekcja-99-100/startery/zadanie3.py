"""Temat 50, zadanie 3. Najpierw zaprojektuj formularz zgodnie z README."""

import sys
from pathlib import Path

from PyQt6 import uic
from PyQt6.QtWidgets import QApplication
from PyQt6.QtWidgets import QMessageBox, QTableWidgetItem

import baza


def main():
    app = QApplication(sys.argv)
    sciezka = Path(__file__).with_name("zadanie3.ui")
    if not sciezka.is_file():
        print(f"Zapisz plik {sciezka.name} z Qt Designer obok tego skryptu.", file=sys.stderr)
        return 1

    okno = uic.loadUi(str(sciezka))
    baza.SCIEZKA = Path(__file__).with_name("zadanie3.db")
    # TODO: Przenieś dodawanie i wyświetlanie z zadania 2.
    # TODO: Zainicjalizuj bazę i podłącz zmienButton oraz usunButton.
    okno.show()
    return app.exec()


if __name__ == "__main__":
    sys.exit(main())
