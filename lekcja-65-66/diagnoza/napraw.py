from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QLineEdit, QVBoxLayout, QMainWindow, QTableWidget, QTableWidgetItem, QSpinBox
app = QApplication.instance() or QApplication([])
pole = QLineEdit()
wynik = QLabel()
def zatwierdz():
    imie = pole.text()
    wynik.setText("OK" if imie else "Podaj imię")
