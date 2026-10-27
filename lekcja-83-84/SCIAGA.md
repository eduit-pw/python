# Temat 41. Wyjaśnienia do praktyki

## Pola wejściowe

QLineEdit.text() zwraca str. QSpinBox.value() int w ustawionym zakresie. Walidację pola tekstowego wykonaj przed budowaniem raportu. Same spacje nie są poprawnym imieniem.

## Checkbox i radio

QCheckBox pozwala na niezależne wybory. Radio w jednej grupie wybiera jeden wariant. QButtonGroup jawnie łączy przyciski i może nadawać im identyfikatory.

## Odczyt stanu

isChecked daje bool. Wczytaj aktualny stan po kliknięciu właściwego przycisku. Nie przechowuj nieaktualnej kopii wyboru z konstruktora.

## Wynik w etykiecie

setText ustawia tekst QLabel. Jeśli dane użytkownika mają być dosłowne, ustaw format PlainText. Nie pozwalaj przypadkiem traktować zawartości jako rich text.

## Kolejność walidacji

Najpierw sprawdź wymagany rozmiar kodu, potem dozwolone znaki. Wyświetl jeden komunikat odpowiadający ustalonej regule. Nie wyliczaj ceny lub zapisu po nieudanej walidacji.

[Zadania i wyniki kontrolne](README.md)

To uzupełnienie przykładów z prezentacji. Definicje i kontrakty zadań czytaj łącznie. Szczegółowe przykłady są również w tekście prezentacji dołączonym do paczki.
