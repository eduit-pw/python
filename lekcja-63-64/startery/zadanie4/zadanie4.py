import sys
from pathlib import Path
from PyQt6 import uic
from PyQt6.QtWidgets import QApplication

if __name__ == "__main__":
    app = QApplication(sys.argv)
    okno = uic.loadUi(str(Path(__file__).with_name("okno.ui")))
    # TODO: połącz przycisk z własną funkcją obsługi, korzystając z objectName.
    okno.show()
    sys.exit(app.exec())
