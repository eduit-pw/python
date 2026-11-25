"""Temat 32, zadanie 2. Najpierw zaprojektuj formularz zgodnie z README."""

import sys
from pathlib import Path

from PyQt6 import uic
from PyQt6.QtWidgets import QApplication


def main():
    app = QApplication(sys.argv)
    sciezka = Path(__file__).with_name("okno.ui")
    if not sciezka.is_file():
        print(f"Zapisz plik {sciezka.name} z Qt Designer obok tego skryptu.", file=sys.stderr)
        return 1

    okno = uic.loadUi(str(sciezka))
    # TODO: Uzupełnij obsługę kliknięcia powitajButton. Czytaj imię i ustaw wynikLabel.
    okno.show()
    return app.exec()


if __name__ == "__main__":
    sys.exit(main())
