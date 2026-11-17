# Temat 49. Zadanie 4. Dla chętnych: Liczby i pusta tabela
# Starter do uzupełnienia, bez rozwiązania.
# Pełne polecenie: README lekcji.
# TODO: Dodaj tabelę z kolumną Liczba i wartościami 2, 10, 1 jako DisplayRole typu int.
# TODO: Włącz sortowanie rosnące. Następnie ustaw liczbę wierszy na 0.
# TODO: Sprawdź obsługę przycisku odczytu, gdy tabela jest pusta.

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
        self.liczby = QTableWidget(3, 1)

    def pokaz_id(self):
        raise NotImplementedError('Uzupełnij rozwiązanie według polecenia.')

    def oproznij(self):
        raise NotImplementedError('Uzupełnij rozwiązanie według polecenia.')
if __name__ == '__main__':
    app = QApplication(sys.argv)
    okno = Okno()
    okno.resize(600, 400)
    okno.show()
    sys.exit(app.exec())
