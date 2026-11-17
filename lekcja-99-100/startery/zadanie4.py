# Temat 50. Zadanie 4. Dla chętnych: Wycofanie transakcji
# Starter do uzupełnienia, bez rozwiązania.
# Pełne polecenie: README lekcji.
# TODO: W nowej testowej bazie wykonaj w jednym with db dwa INSERT.
# TODO: Pierwszy: (Dobry,2024). Drugi: (Błędny,1800), naruszający CHECK.
# TODO: Przechwyć IntegrityError poza with db i odczytaj tabelę.

import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout

def zbuduj_okno():
    okno = QWidget()
    uklad = QVBoxLayout(okno)
    # TODO: dodaj kontrolki i układy opisane w tym zadaniu.
    return okno

if __name__ == "__main__":
    app = QApplication(sys.argv)
    okno = zbuduj_okno()
    okno.show()
    sys.exit(app.exec())

