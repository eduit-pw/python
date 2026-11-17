# Temat 49. Zadanie 1. Lista albumów
# Starter do uzupełnienia, bez rozwiązania.
# Pełne polecenie: README lekcji.
# TODO: Dodaj QListWidget z tytułami „Poranek”, „Wieczór” i „Noc”.
# TODO: Po kliknięciu przycisku „Pokaż” wypisz bieżący tytuł w QLabel.
# TODO: Bez zaznaczenia pokaż „Wybierz album”.

import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QListWidget, QLabel, QPushButton, QTableWidget, QTableWidgetItem, QAbstractItemView

class Okno(QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle('Uzupełnij zadanie')
        # TODO: umieść kontrolki w oknie i połącz właściwe sygnały.
        self.lista = QListWidget()
        self.wynik = QLabel()

    def pokaz_tytul(self):
        raise NotImplementedError('Uzupełnij rozwiązanie według polecenia.')
if __name__ == '__main__':
    app = QApplication(sys.argv)
    okno = Okno()
    okno.resize(600, 400)
    okno.show()
    sys.exit(app.exec())
