# Temat 43. Wyjaśnienia do praktyki

## Layout i geometria

Layout zarządza pozycją i rozmiarem dzieci. Gdy kontrolka należy do layoutu, ręczne move lub setGeometry nie jest właściwym sposobem jej stałego rozmieszczenia.

## QVBoxLayout i QHBoxLayout

Układ pionowy zachowuje kolejność od góry, poziomy od lewej. spacing ustawia odstęp, contentsMargins marginesy. Zagnieżdżaj układy dla formularza i przycisków.

## QFormLayout

Układ formularza łączy etykietę i pole w wierszu. Czytelne podpisy pomagają wskazać znaczenie danych. Sprawdź zachowanie przy wąskim oknie.

## QGridLayout

Podaj wiersz i kolumnę, a opcjonalnie rowSpan i columnSpan. Rozpiętość pozwala podglądowi zająć kilka kolumn. Nie myl numeru kolumny z jej liczbą.

## Dostępne miejsce

Stretch przejmuje wolną przestrzeń i pomaga wyrównać przyciski. Minimum size ogranicza najmniejszy użyteczny rozmiar. W QMainWindow layout umieść na centralnym QWidget.

[Zadania i wyniki kontrolne](README.md)

To uzupełnienie przykładów z prezentacji. Definicje i kontrakty zadań czytaj łącznie. Szczegółowe przykłady są również w tekście prezentacji dołączonym do paczki.
