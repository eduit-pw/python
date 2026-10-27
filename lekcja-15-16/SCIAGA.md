# Temat 8. Wyjaśnienia do praktyki

## Lista i mutacja

Lista zachowuje kolejność i pozwala zmieniać elementy. a = [1, 2] tworzy listę, b = a daje drugą nazwę tego samego obiektu. Dopisanie przez b będzie widoczne przez a.

## append, extend i insert

append(x) dodaje jeden element x. extend(iterowalne) dodaje kolejne elementy argumentu. insert(i, x) wstawia x przed pozycją i. Te metody zmieniają listę i zwracają None.

## Usuwanie i wyszukiwanie

pop(i) usuwa i zwraca element, domyślnie ostatni. remove(x) usuwa pierwszą równą wartość. index(x) podaje pierwszy indeks. Przy braku wartości remove/index zgłaszają ValueError.

## Kopia i sortowanie

copy tworzy nową listę z tymi samymi elementami. Dla zagnieżdżonych list jest to kopia płytka. sorted zwraca nową listę, sort zmienia istniejącą i zwraca None.

## Usuwanie podczas pętli

Usunięcie elementu przesuwa kolejne indeksy i może pominąć rekord. Filtrowanie do nowej listy zachowuje prostą kontrolę przebiegu. Gdy masz modyfikować w miejscu, świadomie steruj indeksem.

[Zadania i wyniki kontrolne](README.md)

To uzupełnienie przykładów z prezentacji. Definicje i kontrakty zadań czytaj łącznie. Szczegółowe przykłady są również w tekście prezentacji dołączonym do paczki.
