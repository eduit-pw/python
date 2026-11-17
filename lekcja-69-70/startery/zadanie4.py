# Temat 35. Zadanie 4. Układ kontrolek
# Starter do uzupełnienia, bez rozwiązania.
# Pełne polecenie: README lekcji.

import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QWidget, QMainWindow, QVBoxLayout, QLineEdit, QPushButton, QLabel, QSlider, QHBoxLayout

if __name__ == "__main__":
    app = QApplication(sys.argv)
    okno = QMainWindow()
    centralny = QWidget()
    okno.setCentralWidget(centralny)
    uklad = QVBoxLayout(centralny)
    # TODO: uzupełnij układ, kontrolki i ustawienia według tego zadania.
    okno.show()
    sys.exit(app.exec())
