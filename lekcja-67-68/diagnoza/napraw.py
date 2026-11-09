from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QLineEdit, QVBoxLayout, QMainWindow, QTableWidget, QTableWidgetItem, QSpinBox
app = QApplication.instance() or QApplication([])
przycisk = QPushButton("Dodaj")
stan = {"licznik": 0}
def dodaj():
    stan["licznik"] += 1
przycisk.clicked.connect(dodaj)
przycisk.clicked.connect(dodaj)
