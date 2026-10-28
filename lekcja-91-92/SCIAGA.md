# Temat 45. Listy i tabele PyQt6

## Składnia pod ręką

| Zapis | Do czego służy | Wynik lub ważna reguła |
| --- | --- | --- |
| `QListWidget.addItem(tekst)` | Dodanie elementu listy | Można też przekazać QListWidgetItem. |
| `lista.currentItem()` | Aktualnie wskazany element | Może zwrócić None. |
| `tabela.setRowCount(n), setColumnCount(n)` | Rozmiar tabeli | Nie tworzy automatycznie zawartości komórek. |
| `tabela.setHorizontalHeaderLabels(nazwy)` | Nagłówki kolumn | Lista napisów. |
| `tabela.setItem(wiersz, kolumna, QTableWidgetItem(tekst))` | Zawartość komórki | Indeksy zaczynają się od 0. |
| `tabela.item(wiersz, kolumna)` | Pobranie komórki | Może zwrócić None. |
| `item.setData(Qt.ItemDataRole.UserRole, id)` | Ukryte ID rekordu | ID pozostaje przy elemencie po sortowaniu. |
| `tabela.currentRow()` | Indeks aktualnego wiersza | -1 przy braku wyboru. |

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
