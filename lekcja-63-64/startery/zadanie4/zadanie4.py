"""Wariant dodatkowy. Wygeneruj ui_okno.py przed uruchomieniem."""

import sys

from PyQt6.QtWidgets import QApplication, QWidget
from ui_okno import Ui_Form


class Okno(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        # TODO: Połącz przycisk z obsługą powitania znaną z zadania 2.


if __name__ == "__main__":
    app = QApplication(sys.argv)
    okno = Okno()
    okno.show()
    sys.exit(app.exec())
