# Temat 48. Zadanie 4. Dla chętnych: Otwieranie pliku
# Starter do uzupełnienia, bez rozwiązania.
# Pełne polecenie: README lekcji.
# TODO: Dodaj akcję „Otwórz”, getOpenFileName i odczyt UTF-8.
# TODO: Po sukcesie wstaw odczytany tekst przez setPlainText.
# TODO: Sprawdź plik z zadania 3, anulowanie i niedostępny plik.

import sys
from pathlib import Path
from PyQt6.QtGui import QAction
from PyQt6.QtWidgets import QApplication, QMainWindow, QTextEdit, QToolBar, QFileDialog, QMessageBox

class Edytor(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle('Uzupełnij zadanie')
        # TODO: umieść kontrolki w oknie i połącz właściwe sygnały.
        self.tekst = QTextEdit()

    def zapisz(self):
        raise NotImplementedError('Uzupełnij rozwiązanie według polecenia.')

    def otworz(self):
        raise NotImplementedError('Uzupełnij rozwiązanie według polecenia.')
if __name__ == '__main__':
    app = QApplication(sys.argv)
    okno = Edytor()
    okno.resize(600, 400)
    okno.show()
    sys.exit(app.exec())
