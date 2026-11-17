# Temat 48. Zadanie 2. Pasek narzędzi
# Starter do uzupełnienia, bez rozwiązania.
# Pełne polecenie: README lekcji.
# TODO: Dodaj do zadania 1 QToolBar i tę samą akcję „Wyczyść”.
# TODO: Dodaj „O programie”, pokazującą information z tekstem „Edytor 1.0”.
# TODO: Sprawdź działanie po kilku użyciach. Nie twórz ponownych połączeń.

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
if __name__ == '__main__':
    app = QApplication(sys.argv)
    okno = Edytor()
    okno.resize(600, 400)
    okno.show()
    sys.exit(app.exec())
