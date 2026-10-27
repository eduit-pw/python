# Temat 10. Wyjaśnienia do praktyki

## Klucz i wartość

Słownik wiąże unikalny klucz z wartością. Przypisanie pod istniejącym kluczem zastępuje wartość. Klucz musi być hashowalny, np. napis lub krotka z hashowalnych elementów.

## Odczyt i brak klucza

d[klucz] zgłasza KeyError, gdy klucza nie ma. d.get(klucz, domyslna) zwraca wartość domyślną bez dodawania klucza. Nie myl braku klucza z wartością równą 0.

## Przeglądanie rekordów

for klucz in d przechodzi po kluczach. d.items() udostępnia pary klucz-wartość, values same wartości. Do raportu alfabetycznego użyj sorted(d).

## Zliczanie wystąpień

Dla każdego elementu odczytaj dotychczasowy licznik lub 0 i zwiększ go o 1. Licznik wystąpień i suma ilości są różnymi obliczeniami, gdy rekord ma pole ilosc.

## Zagnieżdżone dane

d[kod]["ilosc"] najpierw wybiera rekord, potem jego pole. Sprawdź obecność rekordu przed zapisem. Puste wejście powinno dawać pusty wynik albo sumę 0 zgodnie z umową.

[Zadania i wyniki kontrolne](README.md)

To uzupełnienie przykładów z prezentacji. Definicje i kontrakty zadań czytaj łącznie. Szczegółowe przykłady są również w tekście prezentacji dołączonym do paczki.
