# Temat 33. Zadanie 1. Formularz ucznia
# Starter do uzupełnienia, bez rozwiązania.
# Pełne polecenie: README lekcji.
# TODO: Zbuduj QLineEdit „Imię”, QSpinBox 1-5 „Klasa” i przycisk „Pokaż”.
# TODO: Po kliknięciu wypisz w QLabel: „Anna, klasa 4” dla danych Anna i 4.
# TODO: Puste imię po strip ma dawać „Podaj imię”.

import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QSpinBox, QPushButton, QLabel, QCheckBox, QRadioButton, QButtonGroup

class Uczen(QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle('Uzupełnij zadanie')
        # TODO: umieść kontrolki w oknie i połącz właściwe sygnały.
        self.imie = QLineEdit()
        self.klasa = QSpinBox()
        self.wynik = QLabel()

    def pokaz(self):
        raise NotImplementedError('Uzupełnij rozwiązanie według polecenia.')
if __name__ == '__main__':
    app = QApplication(sys.argv)
    okno = Uczen()
    okno.resize(600, 400)
    okno.show()
    sys.exit(app.exec())
