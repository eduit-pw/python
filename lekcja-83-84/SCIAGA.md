# Temat 41. Kontrolki i formularze PyQt6

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
