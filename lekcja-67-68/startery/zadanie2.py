# Temat 34. Zadanie 2. Liczba znaków na żywo
# Starter do uzupełnienia, bez rozwiązania.
# Pełne polecenie: README lekcji.
# TODO: Połącz QLineEdit.textChanged z metodą pokazującą długość tekstu.
# TODO: Licz wszystkie znaki, także spacje. Pusty napis ma długość 0.
# TODO: Sprawdź „abc”, „a b” oraz wyczyszczenie pola.

import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QLineEdit, QSlider

class Okno(QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle('Uzupełnij zadanie')
        # TODO: umieść kontrolki w oknie i połącz właściwe sygnały.
        self.tekst = QLineEdit()
        self.dlugosc = QLabel('0')
if __name__ == '__main__':
    app = QApplication(sys.argv)
    okno = Okno()
    okno.resize(600, 400)
    okno.show()
    sys.exit(app.exec())
