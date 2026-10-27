# Temat 39. Wyjaśnienia do praktyki

## QApplication

QApplication zarządza aplikacją graficzną i zdarzeniami. Utwórz jedną instancję w procesie przed kontrolkami. Program konsolowy i okienkowy mają inny sposób oczekiwania na użytkownika.

## Okno i show

QWidget jest podstawową kontrolką i może być oknem. resize ustawia rozmiar, setWindowTitle tytuł, show pokazuje okno. Samo utworzenie obiektu nie gwarantuje jego wyświetlenia.

## Pętla zdarzeń

app.exec uruchamia obsługę zdarzeń do zamknięcia aplikacji. Nie wykonuj długiej blokującej pracy w obsłudze kliknięcia, bo okno przestanie reagować.

## Rodzic kontrolki

QLabel(tekst, rodzic) wiąże etykietę z oknem. Pozycja jest liczona względem rodzica. Referencja do okna musi istnieć podczas działania programu.

## QMainWindow

QMainWindow ma miejsca na menu, pasek narzędzi i centralny widget. Treść główną ustaw przez setCentralWidget. Nie ustawiaj zwykłego layoutu bezpośrednio na QMainWindow.

[Zadania i wyniki kontrolne](README.md)

To uzupełnienie przykładów z prezentacji. Definicje i kontrakty zadań czytaj łącznie. Szczegółowe przykłady są również w tekście prezentacji dołączonym do paczki.
