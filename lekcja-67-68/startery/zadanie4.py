# Temat 34. Zadanie 4. Dla chętnych: Zapamiętanie próbki
# Starter do uzupełnienia, bez rozwiązania.
# Pełne polecenie: README lekcji.
# TODO: Do zadania 3 dodaj „Pobierz” oraz osobny QLabel małej próbki i zapisanych wartości.
# TODO: Na początku próbka jest biała, (255,255,255). Zapisuj ją tylko przyciskiem.
# TODO: Pobierz czerwony, potem ustaw niebieski bez kliknięcia przycisku. Adaptacja INF.04-01-25.06-SG, II: własny układ okna.

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
        self.probka = QLabel()

    def rgb(self):
        raise NotImplementedError('Uzupełnij rozwiązanie według polecenia.')

    def odswiez(self):
        raise NotImplementedError('Uzupełnij rozwiązanie według polecenia.')

    def pobierz(self):
        raise NotImplementedError('Uzupełnij rozwiązanie według polecenia.')
if __name__ == '__main__':
    app = QApplication(sys.argv)
    okno = Okno()
    okno.resize(600, 400)
    okno.show()
    sys.exit(app.exec())
