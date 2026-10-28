# Temat 44. Menu, akcje i dialogi

## Składnia pod ręką

| Zapis | Do czego służy | Wynik lub ważna reguła |
| --- | --- | --- |
| `QAction("Zapisz", self)` | Wspólna akcja | Import QAction z PyQt6.QtGui. |
| `akcja.triggered.connect(obsluga)` | Obsługa wykonania akcji | Jedna akcja może być w menu i pasku narzędzi. |
| `akcja.setShortcut("Ctrl+S")` | Skrót klawiaturowy | Wywołuje tę samą akcję. |
| `self.menuBar().addMenu("Plik")` | Menu w QMainWindow | menu.addAction(akcja) dodaje pozycję. |
| `QFileDialog.getOpenFileName(...)` | Wybór pliku do odczytu | Wynik: (ścieżka, filtr). |
| `QFileDialog.getSaveFileName(...)` | Wybór miejsca zapisu | Sam dialog nie zapisuje danych. |
| `if sciezka:` | Sprawdzenie wyboru | Po anulowaniu ścieżka jest pusta. |
| `QMessageBox.information(...), warning(...)` | Komunikat informacyjny i ostrzeżenie | question służy do pytania o decyzję. |

## Krótki wzorzec

```python
from PyQt6.QtGui import QAction

# W metodzie okna QMainWindow:
def dodaj_menu(self):
    akcja = QAction("Zakończ", self)
    akcja.setShortcut("Ctrl+Q")
    akcja.triggered.connect(self.close)
    self.menuBar().addMenu("Plik").addAction(akcja)
```

Fragment dodaj_menu wywołaj na instancji QMainWindow po utworzeniu QApplication. Dialog wyboru ścieżki i operacja na pliku to dwa osobne kroki.

[Dokumentacja](https://doc.qt.io/qt-6/qfiledialog.html) · [Zadania lekcji](README.md)
