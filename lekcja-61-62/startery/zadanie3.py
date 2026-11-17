# Temat 31. Zadanie 3. Klasa okna
# Starter do uzupełnienia, bez rozwiązania.
# Pełne polecenie: README lekcji.
# TODO: Przenieś budowę QWidget do klasy Okno i konstruktora __init__.
# TODO: Wywołaj konstruktor klasy bazowej i zachowaj QLabel w self.napis.
# TODO: W programie głównym utwórz QApplication, obiekt Okno i uruchom pętlę.

import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QMainWindow

class Okno(QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle('Uzupełnij zadanie')
        # TODO: umieść kontrolki w oknie i połącz właściwe sygnały.
        self.napis = QLabel('Imię: Anna', self)
        self.grupa = QLabel('Grupa: 4TI', self)
if __name__ == '__main__':
    app = QApplication(sys.argv)
    okno = Okno()
    okno.resize(600, 400)
    okno.show()
    sys.exit(app.exec())
