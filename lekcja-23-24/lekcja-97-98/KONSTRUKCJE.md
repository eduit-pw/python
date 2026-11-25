# Temat 49. Listy i tabele PyQt6

## Formularz z Qt Designer

W zadaniach okienkowych od tematu 32 układ kontrolek przygotowujemy w Designerze. Nazwij kontrolki w polu `objectName`. Ich właściwości odczytu i obsługi pozostają takie same po wczytaniu `.ui`.

```python
from pathlib import Path
from PyQt6 import uic

# Po utworzeniu QApplication:
sciezka = Path(__file__).with_name("zadanie2.ui")  # Użyj nazwy z zadania.
okno = uic.loadUi(str(sciezka))
```

Wzorce tworzenia kontrolek lub layoutów w kodzie pomagają zrozumieć API Qt. Gdy formularz już zawiera kontrolkę, używaj jej pod nazwą z Designera.


## Składnia pod ręką

| Zapis | Do czego służy | Wynik lub ważna reguła |
| --- | --- | --- |
| `QListWidget.addItem(tekst)` | Dodanie elementu listy | Można też przekazać QListWidgetItem. |
| `lista.selectedItems()` | Zaznaczone elementy | Pusta lista oznacza brak zaznaczenia. |
| `tabela.setRowCount(n), setColumnCount(n)` | Rozmiar tabeli | Nie tworzy automatycznie zawartości komórek. |
| `tabela.setHorizontalHeaderLabels(nazwy)` | Nagłówki kolumn | Lista napisów. |
| `tabela.setItem(wiersz, kolumna, QTableWidgetItem(tekst))` | Zawartość komórki | Indeksy zaczynają się od 0. |
| `tabela.item(wiersz, kolumna)` | Pobranie komórki | Może zwrócić None. |
| `item.setData(Qt.ItemDataRole.UserRole, id)` | Ukryte ID rekordu | ID pozostaje przy elemencie po sortowaniu. |
| `tabela.selectionModel().selectedRows()` | Faktycznie zaznaczone wiersze | Pusta lista oznacza brak wyboru. Numer pierwszego wiersza odczytasz przez `wynik[0].row()`. |

## Krótki wzorzec

```python
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QTableWidgetItem

element = QTableWidgetItem("Niebieski")
element.setData(Qt.ItemDataRole.UserRole, 42)
print(element.data(Qt.ItemDataRole.UserRole))  # 42
```

Po sortowaniu numer wiersza nie jest identyfikatorem rekordu. Liczby zapisane jako napisy mogą sortować się leksykograficznie, np. "10" przed "2".

[Dokumentacja](https://doc.qt.io/qt-6/qtablewidget.html) · [Zadania lekcji](README.md)

## Utrwalanie Git w ramach tego bloku

Przed zmianą sprawdź `git status`, a po działającej poprawce obejrzyj `git diff`. Zapisz mały commit z opisem wykonanej zmiany. Czynność zajmuje 2–3 minuty przewidziane na sprawdzenie pracy.
