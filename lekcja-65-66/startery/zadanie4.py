# Temat 33. Zadanie 4. Dla chętnych: Kod i zatwierdzenie
# Starter do uzupełnienia, bez rozwiązania.
# Pełne polecenie: README lekcji.
# TODO: Do zadania 3 dodaj QLineEdit kodu oraz przycisk „Zatwierdź”.
# TODO: Za krótki lub długi kod: „Wymagane 5 znaków”. Obcy znak: „Wymagane cyfry”.
# TODO: Poprawny kod: „Dane poprawne”. Sprawdź 12345, 1234, 12a45 i 12-345. Adaptacja INF.04-01-23.06-SG, II: uproszczone komunikaty.

import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QSpinBox, QPushButton, QLabel, QCheckBox, QRadioButton, QButtonGroup

class Poczta(QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle('Uzupełnij zadanie')
        # TODO: umieść kontrolki w oknie i połącz właściwe sygnały.
        self.grupa = QButtonGroup(self)
        self.cena = QLabel('Cena:')
        self.rodzaj = QLabel()

    def sprawdz_cene(self):
        raise NotImplementedError('Uzupełnij rozwiązanie według polecenia.')

    def zatwierdz(self):
        raise NotImplementedError('Uzupełnij rozwiązanie według polecenia.')
if __name__ == '__main__':
    app = QApplication(sys.argv)
    okno = Poczta()
    okno.resize(600, 400)
    okno.show()
    sys.exit(app.exec())
