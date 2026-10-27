# Temat 33. Wyjaśnienia do praktyki

## Liczba pierwsza

Pierwsza ma dokładnie dwa dodatnie dzielniki i jest >=2. Wartości 0 i 1 nie są pierwsze. Wystarczy sprawdzać dzielniki d, dopóki d*d <= n.

## Sito Eratostenesa

Tablica logiczna opisuje kandydatów od 0 do granicy. Oznacz 0 i 1 jako niepierwsze. Dla pierwszego p wykreślaj wielokrotności od p*p, ponieważ mniejsze miały już mniejszy dzielnik.

## Modyfikacja tablicy

Funkcja wypełniająca sito może zmieniać przekazaną listę i zwracać None. Nie oczekuj nowej tablicy, jeśli umowa mówi o zmianie argumentu.

## Czynniki pierwsze

Dziel przez bieżący dzielnik tak długo, jak liczba jest podzielna. Każde wystąpienie dopisz, także powtórzenia. Na końcu pozostała liczba >1 jest ostatnim czynnikiem.

## NWD

Odejmowanie mniejszej dodatniej liczby od większej zachowuje NWD. Zakończ przy równości. Wersja modulo jest szybsza dla niektórych danych, ale nie zastępuje algorytmu narzuconego poleceniem.

[Zadania i wyniki kontrolne](README.md)

To uzupełnienie przykładów z prezentacji. Definicje i kontrakty zadań czytaj łącznie. Szczegółowe przykłady są również w tekście prezentacji dołączonym do paczki.
