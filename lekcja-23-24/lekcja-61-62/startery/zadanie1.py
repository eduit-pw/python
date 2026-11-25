# Temat 31. Zadanie 1. Uruchom i zamknij
# Starter do uzupełnienia, bez rozwiązania.
# Pełne polecenie: README lekcji.

import sys
from PyQt6.QtWidgets import QApplication, QWidget

if __name__ == "__main__":
    app = QApplication(sys.argv)
    okno = QWidget()
    # TODO: ustaw tytuł i rozmiar wskazane w poleceniu.
    okno.show()
    sys.exit(app.exec())
