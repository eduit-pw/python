# Temat 49. Zadanie 3. ID po sortowaniu
# Starter do uzupełnienia, bez rozwiązania.
# Pełne polecenie: README lekcji.
# TODO: W tabeli zadania 2 włącz sortowanie po tytule.
# TODO: Przyciskiem „Pokaż ID” odczytaj ID aktualnie wybranego rekordu.
# TODO: Sprawdź oba rekordy przed sortowaniem i po odwróceniu kierunku.

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

    def pokaz_id(self):
        raise NotImplementedError('Uzupełnij rozwiązanie według polecenia.')
if __name__ == '__main__':
    app = QApplication(sys.argv)
    okno = Okno()
    okno.resize(600, 400)
    okno.show()
    sys.exit(app.exec())
