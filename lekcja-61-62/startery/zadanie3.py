"""Temat 31. Zadanie 3. Przenieś okno z zadania 2 do klasy."""

import sys

from PyQt6.QtWidgets import QApplication, QLabel, QWidget


class Okno(QWidget):
    def __init__(self):
        super().__init__()
        # TODO: odtwórz tytuł, wymiary i etykiety z zadania 2.
        # Zachowaj kontrolki jako atrybuty obiektu, np. self.napis.


if __name__ == "__main__":
    app = QApplication(sys.argv)
    okno = Okno()
    okno.show()
    sys.exit(app.exec())
