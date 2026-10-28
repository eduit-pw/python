# Temat 40. Qt Designer i pliki .ui

## Składnia pod ręką

| Zapis | Do czego służy | Wynik lub ważna reguła |
| --- | --- | --- |
| `objectName` | Nazwa kontrolki w pliku .ui | Nie jest tym samym co tekst widoczny na przycisku. |
| `from PyQt6 import uic` | Narzędzia obsługi .ui | Plik .ui przechowuje opis interfejsu. |
| `uic.loadUi(sciezka, self)` | Wczytanie interfejsu do obiektu | Typ bazowy okna musi pasować do .ui. |
| `uic.loadUi(sciezka)` | Wczytanie jako nowy obiekt okna | Zachowaj zwrócony obiekt. |
| `pyuic6 okno.ui -o ui_okno.py` | Generowanie pliku Python | Polecenie terminalu. |
| `self.setupUi(self)` | Inicjalizacja w typowym wzorcu dziedziczenia z Ui_* | Wariant z kodem wygenerowanym. |
| `Path(__file__).resolve().parent / "okno.ui"` | Ścieżka względem skryptu | Przekaż str(sciezka) do loadUi. |

## Krótki wzorzec

```python
from pathlib import Path
from PyQt6 import uic
from PyQt6.QtWidgets import QMainWindow

class Okno(QMainWindow):
    def __init__(self):
        super().__init__()
        plik = Path(__file__).resolve().parent / "okno.ui"
        uic.loadUi(str(plik), self)
```

Fragment zakłada okno QMainWindow zapisane w okno.ui oraz standardowy start QApplication z poprzedniego tematu. Logikę trzymaj poza plikiem generowanym, bo ponowne generowanie nadpisze zmiany.

[Dokumentacja](https://www.riverbankcomputing.com/static/Docs/PyQt6/designer.html) · [Zadania lekcji](README.md)
