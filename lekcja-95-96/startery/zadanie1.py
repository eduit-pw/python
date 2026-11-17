# Temat 48. Zadanie 1. Menu i skrót
# Starter do uzupełnienia, bez rozwiązania.
# Pełne polecenie: README lekcji.
# TODO: Utwórz QMainWindow z QTextEdit w obszarze centralnym.
# TODO: Dodaj akcję „Wyczyść”, menu „Edycja” i skrót Ctrl+L.
# TODO: Obsługa ma wyczyścić tekst. Sprawdź zarówno menu, jak i skrót.

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
