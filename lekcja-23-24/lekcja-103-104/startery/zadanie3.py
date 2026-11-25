"""Temat 52, zadanie 3. Najpierw zaprojektuj formularz zgodnie z README."""

import sys
from pathlib import Path

from PyQt6 import uic
from PyQt6.QtWidgets import QApplication
from PyQt6.QtCore import QStandardPaths


def main():
    app = QApplication(sys.argv)
    sciezka = Path(__file__).with_name("okno.ui")
    if not sciezka.is_file():
        print(f"Zapisz plik {sciezka.name} z Qt Designer obok tego skryptu.", file=sys.stderr)
        return 1

    okno = uic.loadUi(str(sciezka))
    # TODO: Wyznacz QStandardPaths.AppDataLocation, utwórz katalog i połącz z nim bazę.
    # TODO: Podepnij zapis i odczyt tytułów.
    okno.show()
    return app.exec()


if __name__ == "__main__":
    sys.exit(main())
