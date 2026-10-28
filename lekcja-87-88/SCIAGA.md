# Temat 43. Układy kontrolek

## Składnia pod ręką

| Zapis | Do czego służy | Wynik lub ważna reguła |
| --- | --- | --- |
| `QVBoxLayout()` | Układ pionowy | Kolejne kontrolki od góry do dołu. |
| `QHBoxLayout()` | Układ poziomy | Kolejne kontrolki obok siebie. |
| `QFormLayout()` | Układ etykieta i pole | addRow("Opis", pole). |
| `QGridLayout()` | Siatka wierszy i kolumn | addWidget(widget, wiersz, kolumna). |
| `layout.addWidget(widget)` | Dodanie kontrolki | Układ zarządza jej geometrią. |
| `layout.addLayout(inny)` | Zagnieżdżenie układu | Łączy np. pionową sekcję z poziomym rzędem. |
| `layout.addStretch()` | Elastyczne wolne miejsce | Rozsuwa inne elementy. |
| `widget.setLayout(layout)` | Przypisanie układu | Zwykły QWidget ma jeden główny layout. |

## Krótki wzorzec

```python
from PyQt6.QtWidgets import QWidget, QFormLayout, QLineEdit

# Po utworzeniu QApplication:
panel = QWidget()
uklad = QFormLayout(panel)
uklad.addRow("Miasto:", QLineEdit())
uklad.addRow("Ulica:", QLineEdit())
```

Fragment po utworzeniu QApplication. W QMainWindow ustaw układ na centralnym QWidget. Ręczna geometria kontrolek koliduje z zarządzaniem ich pozycją przez layout.

[Dokumentacja](https://doc.qt.io/qt-6/layout.html) · [Zadania lekcji](README.md)
