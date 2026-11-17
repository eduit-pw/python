# Temat 35. Zadanie 2. Układ kontrolek
# Starter do uzupełnienia, bez rozwiązania.
# Pełne polecenie: README lekcji.

import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QWidget, QMainWindow, QFormLayout, QLineEdit, QPushButton, QLabel, QSlider, QHBoxLayout

if __name__ == "__main__":
    app = QApplication(sys.argv)
    okno = QWidget()
    uklad = QFormLayout(okno)
    # TODO: uzupełnij układ, kontrolki i ustawienia według tego zadania.
    okno.show()
    sys.exit(app.exec())
