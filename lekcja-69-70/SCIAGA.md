# Temat 34. Wyjaśnienia do praktyki

## Dokładne porównanie

Palindrom zależy od umowy normalizacji i pustego napisu. Porównywanie od obu końców działa bez kopiowania odwróconego tekstu. Niezgodność choć jednej pary wystarcza do False.

## Anagram i liczności

Anagramy mają takie same liczności wszystkich znaków. Ten sam zbiór znaków nie wystarcza: aab i abb mają różne powtórzenia. Najpierw możesz sprawdzić długość.

## Lider większościowy

Lider występuje więcej niż n/2 razy. Dokładnie połowa nie wystarcza. W pierwszym przebiegu paruj różne wartości i ustal kandydata, w drugim policz jego rzeczywiste wystąpienia.

## Kandydat a potwierdzenie

Algorytm wyboru kandydata może zwrócić wartość również przy braku lidera. Bez drugiego przebiegu odpowiedź może być błędna. Dla pustego wejścia zwróć None zgodnie z kontraktem.

## Normalizacja

Zastosuj tylko wymienione zmiany: np. lower i usunięcie zwykłych spacji. Nie zakładaj pomijania interpunkcji, jeśli nie ma tego w zadaniu. Zachowaj oryginał do porównania.

[Zadania i wyniki kontrolne](README.md)

To uzupełnienie przykładów z prezentacji. Definicje i kontrakty zadań czytaj łącznie. Szczegółowe przykłady są również w tekście prezentacji dołączonym do paczki.
