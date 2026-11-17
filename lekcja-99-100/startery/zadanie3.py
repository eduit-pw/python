# Temat 50. Zadanie 3. Zmiana i usunięcie po ID
# Starter do uzupełnienia, bez rozwiązania.
# Pełne polecenie: README lekcji.
# TODO: Dodaj obsługę zaznaczonego rekordu: zmień jego tytuł, potem usuń go.
# TODO: Wykonuj SQL po id, nie po numerze wiersza ani po tytule.
# TODO: Sprawdź próbę operacji bez zaznaczenia i po sortowaniu tabeli.

import sys
import sqlite3
import baza
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QSpinBox, QPushButton, QTableWidget, QTableWidgetItem, QMessageBox, QAbstractItemView

class Okno(QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle('Uzupełnij zadanie')
        # TODO: umieść kontrolki w oknie i połącz właściwe sygnały.
        self.tytul = QLineEdit()
        self.rok = QSpinBox()
        self.tabela = QTableWidget(0, 3)

    def id(self):
        raise NotImplementedError('Uzupełnij rozwiązanie według polecenia.')

    def odswiez(self):
        raise NotImplementedError('Uzupełnij rozwiązanie według polecenia.')

    def blad(self, tekst):
        raise NotImplementedError('Uzupełnij rozwiązanie według polecenia.')

    def dodaj(self):
        raise NotImplementedError('Uzupełnij rozwiązanie według polecenia.')

    def zmien(self):
        raise NotImplementedError('Uzupełnij rozwiązanie według polecenia.')

    def usun(self):
        raise NotImplementedError('Uzupełnij rozwiązanie według polecenia.')
if __name__ == '__main__':
    app = QApplication(sys.argv)
    okno = Okno()
    okno.resize(600, 400)
    okno.show()
    sys.exit(app.exec())
