# Temat 36. Wyjaśnienia do praktyki

## Minimum i maksimum parami

Porównaj dwa elementy między sobą, potem mniejszy z minimum, większy z maksimum. Obsłuż nieparzystą długość i pojedynczy element. Puste wejście wymaga określonej reakcji.

## Bubble sort

Porównuj sąsiadów i zamieniaj te w złej kolejności. Po pełnym przebiegu największy element trafia na koniec rozpatrywanej części. Nie gub powtórzeń.

## Insertion sort

Zachowaj wstawianą wartość, przesuń większe elementy uporządkowanej części w prawo i wpisz wartość w zwolnione miejsce. Nie nadpisuj jej przed zapamiętaniem.

## Selection sort

W nieuporządkowanej części znajdź indeks ekstremum, a potem zamień raz z pozycją początkową tej części. Wybór maksimum daje łatwy porządek malejący.

## Zmiana a nowa lista

Własne sortowanie może modyfikować argument i zwracać None. Wyraźnie ustal kontrakt. Do sprawdzenia użyj niezależnej kopii i wyniku oczekiwanego, także dla [] i listy jednoelementowej.

[Zadania i wyniki kontrolne](README.md)

To uzupełnienie przykładów z prezentacji. Definicje i kontrakty zadań czytaj łącznie. Szczegółowe przykłady są również w tekście prezentacji dołączonym do paczki.
