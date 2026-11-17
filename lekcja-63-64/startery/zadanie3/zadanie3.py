import sys
from PyQt6.QtWidgets import QApplication, QWidget
from ui_okno import Ui_Form

class Okno(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        # TODO: dodaj obsługę przycisku. Nie zmieniaj wygenerowanego pliku.

if __name__ == "__main__":
    app = QApplication(sys.argv)
    okno = Okno()
    okno.show()
    sys.exit(app.exec())
