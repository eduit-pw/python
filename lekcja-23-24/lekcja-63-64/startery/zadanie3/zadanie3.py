"""Temat 32, zadanie 3. Najpierw zaprojektuj formularz zgodnie z README."""

import sys
from pathlib import Path

from PyQt6 import uic
from PyQt6.QtWidgets import QApplication


def main():
    app = QApplication(sys.argv)
    sciezka = Path(__file__).with_name("okno_zadanie3.ui")
    if not sciezka.is_file():
        print(f"Zapisz plik {sciezka.name} z Qt Designer obok tego skryptu.", file=sys.stderr)
        return 1

    okno = uic.loadUi(str(sciezka))
    # TODO: Przenieś własną obsługę kliknięcia z zadania 2.
    okno.show()
    return app.exec()


if __name__ == "__main__":
    sys.exit(main())
