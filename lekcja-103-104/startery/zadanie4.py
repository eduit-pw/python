"""Temat 52, zadanie 4. Najpierw zaprojektuj formularz zgodnie z README."""

import sys
from pathlib import Path

from PyQt6 import uic
from PyQt6.QtWidgets import QApplication
from PyQt6.QtWidgets import QFileDialog


def main():
    app = QApplication(sys.argv)
    sciezka = Path(__file__).with_name("okno.ui")
    if not sciezka.is_file():
        print(f"Zapisz plik {sciezka.name} z Qt Designer obok tego skryptu.", file=sys.stderr)
        return 1

    okno = uic.loadUi(str(sciezka))
    # TODO: Przenieś trwały zapis z zadania 3. Dodaj dialog pliku i reakcję na anulowanie.
    # TODO: Zbuduj paczkę z plikiem okno.ui.
    okno.show()
    return app.exec()


if __name__ == "__main__":
    sys.exit(main())
