# Temat 5. Wyjaśnienia do praktyki

## Indeksy i wycinki

Indeks 0 oznacza pierwszy znak, -1 ostatni. tekst[start:stop] pomija stop. Wycinek może być pusty bez błędu, ale odczyt nieistniejącego pojedynczego indeksu zgłasza IndexError.

## Niemutowalny napis

Nie przypiszesz tekst[0] = "A". Metody str zwracają nowe napisy. Zapis tekst.lower() bez zachowania wyniku nie zmienia tekstu wskazanego przez nazwę tekst.

## strip, split i join

strip usuwa białe znaki ze skrajów. split() dzieli według białych znaków i pomija puste pola. separator.join(fragmenty) skleja napisy podanym separatorem i zwraca str.

## Wielkość liter i zamiana

lower i upper zwracają nowe napisy. replace(stare, nowe) zastępuje fragmenty. Nie usuwaj spacji i interpunkcji, jeśli specyfikacja każe je zachować.

## Cyfry i kody

isdigit akceptuje więcej znaków Unicode niż cyfry ASCII. Gdy wymagane są znaki 0-9, sprawdź każdy znak w tym zakresie. Najpierw długość i format, potem odczyt indeksu.

[Zadania i wyniki kontrolne](README.md)

To uzupełnienie przykładów z prezentacji. Definicje i kontrakty zadań czytaj łącznie. Szczegółowe przykłady są również w tekście prezentacji dołączonym do paczki.
