# Temat 33. Zadanie 3. Rodzaj przesyłki i cena
# Starter do uzupełnienia, bez rozwiązania.
# Pełne polecenie: README lekcji.
# TODO: Utwórz trzy pola radio i QButtonGroup. Pocztówka wybrana na początku.
# TODO: Dodaj przycisk „Sprawdź cenę” i QLabel z początkowym tekstem „Cena:”.
# TODO: Wyświetl cenę z powyższego cennika. Obraz zastąp etykietą rodzaju przesyłki. Adaptacja INF.04-01-23.06-SG, II: etykieta zamiast obrazu.

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
