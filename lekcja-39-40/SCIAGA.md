# Temat 20. Wyjaśnienia do praktyki

## Iterable i iterator

iter(obiekt) pobiera iterator. next(iterator) zwraca następny element. Lista pozwala tworzyć nowe iteratory, a istniejący iterator pamięta bieżącą pozycję.

## Koniec iteracji

__next__ zgłasza StopIteration po wyczerpaniu. Pętla for obsługuje ten sygnał. next(it, domyslna) zwraca podaną wartość zamiast wyjątku, gdy iterator się skończył.

## Generator i yield

Wywołanie funkcji z yield tworzy generator. Kod zaczyna działać przy pobieraniu. yield oddaje wartość i wstrzymuje wykonanie z zachowaniem stanu. Kolejne pobranie wznawia kod za yield.

## Jednorazowość

Wyczerpany generator nie zaczyna od nowa. list(g) zużywa pozostałe elementy i przechowuje je w pamięci. sum(g), a potem kolejne przejście po g nie odczyta tych samych danych.

## Zużycie pamięci

Generator może uniknąć list wyników pośrednich. Nadal przechowuje swój stan i referencje do źródeł. Nie oznacza zerowego zużycia pamięci ani automatycznego zwolnienia całej listy wejściowej.

[Zadania i wyniki kontrolne](README.md)

To uzupełnienie przykładów z prezentacji. Definicje i kontrakty zadań czytaj łącznie. Szczegółowe przykłady są również w tekście prezentacji dołączonym do paczki.
