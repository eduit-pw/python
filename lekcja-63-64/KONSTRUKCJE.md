# Temat 32. Qt Designer i PyQt6

| Zapis lub właściwość | Działanie |
| --- | --- |
| `objectName` | Nazwa kontrolki używana w Pythonie. |
| `text` | Napis widoczny dla użytkownika. |
| `Path(__file__).with_name("okno.ui")` | Szuka formularza obok pliku skryptu. |
| `uic.loadUi(str(sciezka))` | Tworzy obiekt okna i wczytuje kontrolki przy uruchomieniu. |
| `okno.powitajButton.clicked.connect(powitaj)` | Przekazuje funkcję do wywołania po kliknięciu. |
| `uic.loadUi(str(sciezka), self)` | Wypełnia własny obiekt okna. Klasa bazowa musi odpowiadać rodzajowi formularza. |

Wariant dodatkowy: `python -m PyQt6.uic.pyuic okno.ui -o ui_okno.py`. Klasa dla głównego obiektu `Form` to `Ui_Form`. Własną logikę trzymaj w osobnym pliku, bo polecenie nadpisuje wygenerowany moduł.
