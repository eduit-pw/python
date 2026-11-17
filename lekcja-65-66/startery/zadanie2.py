# Temat 33. Zadanie 2. Opcje niezależne
# Starter do uzupełnienia, bez rozwiązania.
# Pełne polecenie: README lekcji.
# TODO: Dodaj QCheckBox „Python” i „SQL” oraz przycisk podsumowania.
# TODO: Wypisz wybrane nazwy w tej kolejności, rozdzielone przecinkiem.
# TODO: Gdy żadna nie jest wybrana, pokaż „Brak wyboru”.

import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QSpinBox, QPushButton, QLabel, QCheckBox, QRadioButton, QButtonGroup

class Opcje(QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle('Uzupełnij zadanie')
        # TODO: umieść kontrolki w oknie i połącz właściwe sygnały.
        self.python = QCheckBox('Python')
        self.sql = QCheckBox('SQL')
        self.wynik = QLabel()

    def pokaz(self):
        raise NotImplementedError('Uzupełnij rozwiązanie według polecenia.')
if __name__ == '__main__':
    app = QApplication(sys.argv)
    okno = Opcje()
    okno.resize(600, 400)
    okno.show()
    sys.exit(app.exec())
