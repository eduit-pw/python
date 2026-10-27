# Temat 44. Wyjaśnienia do praktyki

## QAction

QAction reprezentuje jedną akcję: tekst, skrót i sygnał triggered. W PyQt6 importuj ją z QtGui. Ta sama akcja może być jednocześnie w menu i pasku narzędzi.

## Dialog wyboru pliku

getOpenFileName i getSaveFileName zwracają ścieżkę oraz wybrany filtr. Pusta ścieżka oznacza anulowanie. Najpierw sprawdź wynik, potem otwieraj plik.

## Odczyt i zapis

QTextEdit.toPlainText pobiera zwykły tekst, setPlainText ustawia go bez interpretacji HTML. Plik zapisuj jako UTF-8. Przy błędzie odczytu zachowaj poprzedni tekst.

## Komunikaty

QMessageBox.information pokazuje informację, warning problem, question pytanie o decyzję. Nie traktuj zamknięcia dialogu jako potwierdzenia usunięcia.

## Połączenia i skróty

Połącz akcję raz podczas budowy okna. Dodawanie connect po każdym kliknięciu może wywołać tę samą operację wielokrotnie. Sprawdź menu, pasek i skrót.

[Zadania i wyniki kontrolne](README.md)

To uzupełnienie przykładów z prezentacji. Definicje i kontrakty zadań czytaj łącznie. Szczegółowe przykłady są również w tekście prezentacji dołączonym do paczki.
