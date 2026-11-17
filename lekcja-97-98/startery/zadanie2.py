# Temat 49. Zadanie 2. Tabela rekordów
# Starter do uzupełnienia, bez rozwiązania.
# Pełne polecenie: README lekcji.
# TODO: Utwórz kolumny ID, Tytuł, Rok i rekordy (7,Poranek,2024), (12,Wieczór,2023).
# TODO: Wypełnij wszystkie komórki i ustaw zaznaczanie pojedynczego wiersza.
# TODO: Zablokuj edycję komórek bezpośrednio w tabeli.

import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QListWidget, QLabel, QPushButton, QTableWidget, QTableWidgetItem, QAbstractItemView

class Okno(QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle('Uzupełnij zadanie')
        # TODO: umieść kontrolki w oknie i połącz właściwe sygnały.
        self.wynik = QLabel()
        self.tabela = QTableWidget(2, 3)
if __name__ == '__main__':
    app = QApplication(sys.argv)
    okno = Okno()
    okno.resize(600, 400)
    okno.show()
    sys.exit(app.exec())
