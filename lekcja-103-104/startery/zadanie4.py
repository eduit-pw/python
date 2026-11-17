# Temat 52. Zadanie 4. Dla chętnych: Przekazanie odbiorcy
# Starter do uzupełnienia, bez rozwiązania.
# Pełne polecenie: README lekcji.
# TODO: Przygotuj paczkę onedir lub onefile dla tego samego systemu i architektury.
# TODO: Sprawdź start, zapis, odczyt, anulowanie dialogu i brak zasobu.
# TODO: Dodaj krótką instrukcję uruchomienia oraz wersje użytych zależności.

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

