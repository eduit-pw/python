from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QLineEdit, QVBoxLayout, QMainWindow, QTableWidget, QTableWidgetItem, QSpinBox
app = QApplication.instance() or QApplication([])
okno = QWidget()
przycisk = QPushButton("Powitaj", okno)
wynik = QLabel("", okno)
def powitaj():
    wynik.setText("Cześć!")
przycisk.clicked.connect(powitaj())
