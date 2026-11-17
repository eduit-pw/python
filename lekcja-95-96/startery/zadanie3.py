# Temat 48. Zadanie 3. Zapis i anulowanie
# Starter do uzupełnienia, bez rozwiązania.
# Pełne polecenie: README lekcji.
# TODO: Dodaj akcję „Zapisz” z Ctrl+S oraz dialog zapisu.
# TODO: Zapisz tekst „Zażółć gęślą jaźń” jako wynik.txt w UTF-8.
# TODO: Powtórz akcję i anuluj dialog. Obsłuż błąd zapisu przez warning.

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
if __name__ == '__main__':
    app = QApplication(sys.argv)
    okno = Edytor()
    okno.resize(600, 400)
    okno.show()
    sys.exit(app.exec())
