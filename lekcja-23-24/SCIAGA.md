# Temat 12. Wyjaśnienia do praktyki

## lambda i klucz

lambda p: p[1] tworzy funkcję zwracającą drugie pole rekordu. W sorted(..., key=...) klucz służy do porównań i nie zmienia rekordu. Równe klucze zachowują wcześniejszą kolejność.

## map i filter

map(f, dane) przekształca elementy, filter(f, dane) wybiera te z prawdziwym wynikiem predykatu. W Pythonie 3 zwracają iteratory. list(...) zapisuje ich wyniki w liście.

## math

Najpierw import math. math.sqrt(x) daje pierwiastek, pi stałą do wzorów koła, floor i ceil zaokrąglają w dół i górę. Zaokrąglaj wynik przy prezentacji, nie stałą pi przed obliczeniem.

## random i granice

randint(a, b) dopuszcza oba końce. randrange(a, b) pomija b. choice wybiera element niepustej sekwencji, a sample wybiera pozycje bez powtórnego wyboru tej samej pozycji.

## Testy losowania

Nie oczekuj stałej sekwencji. Sprawdź długość, typ, zakres i ewentualną unikalność. Raport zliczania testuj dodatkowo na stałych, ręcznie sprawdzalnych danych.

[Zadania i wyniki kontrolne](README.md)

To uzupełnienie przykładów z prezentacji. Definicje i kontrakty zadań czytaj łącznie. Szczegółowe przykłady są również w tekście prezentacji dołączonym do paczki.
