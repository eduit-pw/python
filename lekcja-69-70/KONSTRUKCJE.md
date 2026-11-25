# Temat 35. Układy kontrolek

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
