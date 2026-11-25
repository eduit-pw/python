# Temat 34. Sygnały i sloty

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
| `przycisk.clicked.connect(obsluga)` | Połączenie sygnału z funkcją | Podaj funkcję bez nawiasów. |
| `def obsluga():` | Zwykła funkcja jako slot | Wykona się po emisji połączonego sygnału. |
| `pole.textChanged.connect(obsluga)` | Reakcja na zmianę tekstu | Może reagować także na setText z kodu. |
| `spin.valueChanged.connect(obsluga)` | Reakcja na zmianę liczby | Sygnał przekazuje nową wartość. |
| `sygnal.disconnect(obsluga)` | Usunięcie połączenia | Brak połączenia może spowodować TypeError. |
| `lambda checked=False: f(x)` | Przekazanie dodatkowego argumentu | clicked może przekazać bool checked. |
| `Powtórne connect` | Drugie połączenie tej samej obsługi | Może dać wielokrotne wykonanie. |

## Krótki wzorzec

```python
from PyQt6.QtWidgets import QPushButton

# Po utworzeniu QApplication:
przycisk = QPushButton("Pokaż")
def obsluga():
    print("Kliknięto")

przycisk.clicked.connect(obsluga)
przycisk.click()  # Kliknięto
```

connect(obsluga()) wywołałoby funkcję od razu i przekazało do connect jej wynik. Stan aplikacji przechowuj w danych, a etykietę aktualizuj na jego podstawie.

[Dokumentacja](https://doc.qt.io/qt-6/signalsandslots.html) · [Zadania lekcji](README.md)
