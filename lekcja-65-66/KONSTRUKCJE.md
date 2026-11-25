# Temat 33. Kontrolki i formularze PyQt6

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
| `QLabel("tekst"), etykieta.setText(tekst)` | Etykieta i zmiana jej tekstu | setText przyjmuje str. |
| `QLineEdit(), pole.text()` | Jednowierszowe pole i odczyt | Wynik str, także dla wpisanych cyfr. |
| `pole.clear(), pole.setPlaceholderText("opis")` | Wyczyszczenie i podpowiedź | Placeholder nie jest wartością pola. |
| `QSpinBox(), pole.value()` | Całkowite pole liczbowe | value zwraca int. |
| `QDoubleSpinBox(), pole.value()` | Pole z częścią ułamkową | value zwraca float. |
| `pole.setRange(minimum, maksimum)` | Dopuszczalny zakres | Dotyczy kontrolek liczbowych. |
| `QCheckBox(), opcja.isChecked()` | Niezależna opcja | Odczyt bool. |
| `QRadioButton(), QButtonGroup` | Wybór jednej opcji z grupy | Grupę zdefiniuj jawnie przy bardziej złożonym układzie. |

## Krótki wzorzec

```python
from PyQt6.QtWidgets import QLineEdit, QSpinBox

# Po utworzeniu QApplication:
tekst = QLineEdit()
tekst.setText("  kot  ")
ilosc = QSpinBox()
ilosc.setRange(1, 20)
ilosc.setValue(4)
print(tekst.text().strip(), ilosc.value())  # kot 4
```

To fragment do uruchomienia po utworzeniu QApplication. Wartości odczytuj w chwili obsługi akcji, żeby korzystać z aktualnego stanu formularza.

[Dokumentacja](https://doc.qt.io/qt-6/qlineedit.html) · [Zadania lekcji](README.md)
