from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QLineEdit, QVBoxLayout, QMainWindow, QTableWidget, QTableWidgetItem, QSpinBox
app = QApplication.instance() or QApplication([])
okno = QMainWindow()
uklad = QVBoxLayout()
uklad.addWidget(QLabel("Treść"))
okno.setLayout(uklad)
