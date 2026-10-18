# Ćwiczenia: Algorytmy na tekstach i listach: badanie palindromów, anagramów oraz Algorytm Wyszukiwania Lidera

**Temat 34 | Lekcje 69-70**

## Przygotowanie

Środowisko i polecenia uruchamiania opisano w [instrukcji głównej](../README.md#uruchamianie). Wystarcza biblioteka standardowa Pythona.

Utwórz pliki wskazane w zadaniach wewnątrz bieżącego folderu lekcji. Kod uruchamiaj w terminalu z tego folderu. Zadania wprowadzają kolejne zmiany; zachowuj wcześniejsze wersje w podfolderach, jeśli wymaga tego polecenie.

## Reguły funkcji

`palindrom(tekst)` porównuje znaki od obu końców i zwraca bool, bez zmiany tekstu. Dla pustego napisu zwraca True zgodnie z umową tego zadania. `anagram(a, b)` porównuje liczności wszystkich znaków, z rozróżnianiem wielkości liter. `lider(dane)` zwraca element występujący **więcej niż połowę** razy albo None. W pierwszym przebiegu wyznacz kandydata przez parowanie różnych wartości, w drugim potwierdź jego liczność. Zachowaj wejścia. W zadaniu 4 normalizację wykonaj przed wywołaniem palindrom.

## Zadanie 1. Palindromy

- Zaimplementuj palindrom bez odwracania napisu przez slicing.
- Sprawdź: kajak, abba, kot, a oraz pusty napis.
- Zachowaj umowę: porównanie dokładne, pusty napis daje True.

**Wynik kontrolny:** True, True, False, True, True.

## Zadanie 2. Pary anagramów

- Sprawdź pary: (kot,kto), (aab,abb), (abcd,dcba), (abc,ab).
- Użyj funkcji zliczającej znaki. Wypisz tylko pary anagramów.
- Oblicz liczbę pasujących par. Porównanie ma być dokładne. Adaptacja wiązki „Anagramy” ze zbioru CKE: cztery własne pary.

**Wynik kontrolny:** (kot,kto) i (abcd,dcba), razem 2.

## Zadanie 3. Lider listy

- Napisz dwuprzebiegową funkcję lider(dane), zwracającą int albo None.
- Dane mają być listą liczb całkowitych. Sprawdź,, [].
- Nie używaj None jako elementu wejściowego.

**Wynik kontrolny:** 2, None, None.

## Zadanie 4. Zdanie i normalizacja

- Przed testem palindromu zamień litery na małe i usuń zwykłe spacje.
- Sprawdź „Kobyła ma mały bok” oraz „Ala ma kota”.
- Pozostałe znaki zachowaj. Wypisz także tekst po normalizacji.

**Wynik kontrolny:** „kobyłamamałybok”: True. „alamakota”: False.

## Oddanie pracy

Zachowaj źródła i niezbędne pliki danych. W `testy.md` opisz rzeczywiście wykonane próby: dane, oczekiwany wynik, wynik otrzymany i wniosek. Własną instrukcję uruchomienia zapisz w `URUCHOMIENIE.md`, aby zachować treść zadań w tym README. Dołącz dokumentację wskazaną w poleceniu. Zadania oznaczone jako dodatkowe są dla chętnych.

[Spis lekcji](../README.md)
