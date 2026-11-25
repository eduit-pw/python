"""Temat 33, zadanie 3. Najpierw zaprojektuj formularz zgodnie z README."""

import sys
from pathlib import Path

from PyQt6 import uic
from PyQt6.QtWidgets import QApplication
from PyQt6.QtWidgets import QButtonGroup


def main():
    app = QApplication(sys.argv)
    sciezka = Path(__file__).with_name("zadanie3.ui")
    if not sciezka.is_file():
        print(f"Zapisz plik {sciezka.name} z Qt Designer obok tego skryptu.", file=sys.stderr)
        return 1

    okno = uic.loadUi(str(sciezka))
    # TODO: Utwórz QButtonGroup dla trzech przycisków radiowych.
    # TODO: Połącz cenaButton z odczytem wyboru i wyświetleniem ceny.
    okno.show()
    return app.exec()


if __name__ == "__main__":
    sys.exit(main())
