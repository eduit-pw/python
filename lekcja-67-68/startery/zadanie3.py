# Temat 34. Zadanie 3. Podgląd RGB
# Starter do uzupełnienia, bez rozwiązania.
# Pełne polecenie: README lekcji.
# TODO: Utwórz suwaki R, G, B 0-255, początkowo wszystkie ustawione na 255.
# TODO: Po każdej zmianie odśwież duży QLabel i napis z trzema wartościami.
# TODO: Sprawdź ustawienia (255,0,0), (0,255,0), (0,0,255). Adaptacja INF.04-01-25.06-SG, II: same suwaki i podgląd.

import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QLineEdit, QSlider

class Okno(QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle('Uzupełnij zadanie')
        # TODO: umieść kontrolki w oknie i połącz właściwe sygnały.
        self.podglad = QLabel()
        self.wartosci = QLabel()

    def rgb(self):
        raise NotImplementedError('Uzupełnij rozwiązanie według polecenia.')

    def odswiez(self):
        raise NotImplementedError('Uzupełnij rozwiązanie według polecenia.')
if __name__ == '__main__':
    app = QApplication(sys.argv)
    okno = Okno()
    okno.resize(600, 400)
    okno.show()
    sys.exit(app.exec())
