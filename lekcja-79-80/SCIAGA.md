# Temat 39. PyQt6: start okna

## Składnia pod ręką

| Zapis | Do czego służy | Wynik lub ważna reguła |
| --- | --- | --- |
| `from PyQt6.QtWidgets import QApplication, QWidget` | Import klas GUI | Wymaga zainstalowanego PyQt6. |
| `app = QApplication(sys.argv)` | Obiekt aplikacji | Zwykle jeden na proces, przed tworzeniem kontrolek. |
| `okno = QWidget()` | Proste okno lub kontrolka | Samo utworzenie nie pokazuje go na ekranie. |
| `okno.setWindowTitle("Tytuł")` | Tytuł okna | Argument str. |
| `okno.resize(szerokosc, wysokosc)` | Początkowy rozmiar | Nie zastępuje elastycznego układu kontrolek. |
| `okno.show()` | Pokazanie okna | Pętla zdarzeń musi jeszcze działać. |
| `app.exec()` | Start pętli zdarzeń | Zwraca kod zakończenia po zamknięciu aplikacji. |
| `QMainWindow.setCentralWidget(widget)` | Centralna zawartość okna głównego | QMainWindow ma też miejsca na menu i pasek stanu. |

## Krótki wzorzec

```python
import sys
from PyQt6.QtWidgets import QApplication, QWidget

app = QApplication(sys.argv)
okno = QWidget()
okno.setWindowTitle("Przykład")
okno.resize(320, 160)
okno.show()
sys.exit(app.exec())
```

Uruchamiaj jako osobny skrypt w środowisku graficznym. Długa operacja w głównym wątku blokuje reagowanie okna.

[Dokumentacja](https://doc.qt.io/qt-6/qapplication.html) · [Zadania lekcji](README.md)
