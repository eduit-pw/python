# Temat 27. Wyjaśnienia do praktyki

## open i with

open(plik, tryb, encoding="utf-8") otwiera plik. with zamyka zasób po bloku także przy wyjątku. Ścieżka względna zależy od bieżącego katalogu procesu.

## Tryby r, w i a

r czyta istniejący plik. w tworzy lub nadpisuje. a dopisuje na końcu. Otwarcie w może skasować poprzednią treść, więc najpierw zakończ walidację wejścia.

## read i iterowanie

read zwraca treść, readline pojedynczy wiersz, a pętla po pliku kolejne wiersze. Wiersz zwykle zawiera końcowe \n. Pusty wiersz i koniec pliku wymagają rozróżnienia.

## write i nowa linia

write(tekst) zapisuje str i zwraca liczbę zapisanych znaków. Nową linię dodajesz sam przez \n. Liczba znaków nie musi być liczbą bajtów pliku UTF-8.

## Rekord wielowierszowy

Kontroluj kompletność bloku przed tworzeniem obiektów. Pomijanie pustych wierszy jest poprawne tylko tam, gdzie zezwala na to format. Obsłuż brak pliku i błędną konwersję z numerem wiersza.

[Zadania i wyniki kontrolne](README.md)

To uzupełnienie przykładów z prezentacji. Definicje i kontrakty zadań czytaj łącznie. Szczegółowe przykłady są również w tekście prezentacji dołączonym do paczki.
