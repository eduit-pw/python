import sys
import sqlite3
from pathlib import Path
from PyQt6.QtCore import QStandardPaths
from PyQt6.QtWidgets import QApplication,QWidget,QVBoxLayout,QLineEdit,QLabel,QPushButton

app=QApplication(sys.argv)
app.setOrganizationName("Technikum")
app.setApplicationName("AlbumyTemat52Zadanie1")
folder=Path(QStandardPaths.writableLocation(QStandardPaths.StandardLocation.AppDataLocation))
folder.mkdir(parents=True,exist_ok=True)
sciezka=folder/"albumy.db"

def wykonaj(sql,parametry=()):
    db=sqlite3.connect(sciezka)
    try:
        with db:
            return db.execute(sql,parametry).fetchall()
    finally:db.close()

wykonaj("CREATE TABLE IF NOT EXISTS albumy(id INTEGER PRIMARY KEY,tytul TEXT NOT NULL)")
okno=QWidget()
okno.setWindowTitle("Katalog albumów")
okno.resize(570, 270)
uklad=QVBoxLayout(okno)
tytul=QLineEdit()
tytul.setPlaceholderText("Tytuł albumu")
wynik=QLabel()
przycisk=QPushButton("Zapisz album")

def odswiez():
    dane=wykonaj("SELECT id,tytul FROM albumy ORDER BY id")
    wynik.setText("\n".join(f"{i}: {t}" for i,t in dane)+f"\nBaza: {sciezka}")

def dodaj():
    tekst=tytul.text().strip()
    if not tekst:return
    wykonaj("INSERT INTO albumy(tytul) VALUES(?)",(tekst,))
    odswiez()
    tytul.clear()

przycisk.clicked.connect(dodaj)
for w in (tytul,przycisk,wynik):uklad.addWidget(w)
odswiez()
okno.show()
sys.exit(app.exec())
