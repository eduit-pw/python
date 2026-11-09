from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QLineEdit, QVBoxLayout, QMainWindow, QTableWidget, QTableWidgetItem, QSpinBox
app = QApplication.instance() or QApplication([])
tabela = QTableWidget(2, 1)
tabela.setItem(0, 0, QTableWidgetItem("A"))
tabela.setItem(1, 0, QTableWidgetItem("B"))
def usun():
    tabela.removeRow(0)
