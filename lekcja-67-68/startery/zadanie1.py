# Temat 34. Zadanie 1. Licznik kliknięć
# Starter do uzupełnienia, bez rozwiązania.
# Pełne polecenie: README lekcji.
# TODO: Zbuduj etykietę wyniku, przyciski „+1” i „Reset”. Stan początkowy: 0.
# TODO: Pierwszy przycisk zwiększa pole self.licznik, drugi zeruje je.
# TODO: Kliknij +1 trzy razy, Reset i +1 jeden raz.

import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QLineEdit, QSlider

class Okno(QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle('Uzupełnij zadanie')
        # TODO: umieść kontrolki w oknie i połącz właściwe sygnały.
        self.licznik_wynik = QLabel('0')

    def zwieksz(self):
        raise NotImplementedError('Uzupełnij rozwiązanie według polecenia.')

    def reset(self):
        raise NotImplementedError('Uzupełnij rozwiązanie według polecenia.')
if __name__ == '__main__':
    app = QApplication(sys.argv)
    okno = Okno()
    okno.resize(600, 400)
    okno.show()
    sys.exit(app.exec())
