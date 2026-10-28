# Ćwiczenia: Algorytmy na tekstach i listach: badanie palindromów, anagramów oraz Algorytm Wyszukiwania Lidera

**Temat 34 | Lekcje 69-70**

## Przygotowanie

Środowisko i polecenia uruchamiania opisano w [instrukcji głównej](../README.md#uruchamianie). Wystarcza biblioteka standardowa Pythona.

Utwórz pliki wskazane w zadaniach wewnątrz bieżącego folderu lekcji. Kod uruchamiaj w terminalu z tego folderu. Zadania wprowadzają kolejne zmiany; zachowuj wcześniejsze wersje w podfolderach, jeśli wymaga tego polecenie.

## Reguły funkcji

`palindrom(tekst)` porównuje znaki od obu końców i zwraca bool, bez zmiany tekstu. Dla pustego napisu zwraca True zgodnie z umową tego zadania. `anagram(a, b)` porównuje liczności wszystkich znaków, z rozróżnianiem wielkości liter. `lider(dane)` zwraca element występujący **więcej niż połowę** razy albo None. W pierwszym przebiegu wyznacz kandydata przez parowanie różnych wartości, w drugim potwierdź jego liczność. Zachowaj wejścia. W zadaniu 4 normalizację wykonaj przed wywołaniem palindrom.

## Sposób pracy podczas bloku

| Etap | Czas | Co robisz |
| --- | ---: | --- |
| Wyjaśnienia i demonstracja | 0-25 min | Czytasz przykład, przewidujesz wynik i zadajesz pytania. |
| Zadanie 1 z prowadzącym | 25-35 min | Uruchamiasz pierwszy wariant i objaśniasz kluczowy zapis. |
| Zadanie 2 wspólnie | 35-50 min | Proponujesz kolejne kroki, sam zapisujesz kod. |
| Zadanie 3 samodzielnie | 50-70 min | Realizujesz kontrakt i wykonujesz próby. |
| Zadanie 4 lub diagnoza błędu | 70-85 min | Sprawdzasz przypadki graniczne i poprawiasz program. |
| Zakończenie | 85-90 min | Zapisujesz kod, jeden wniosek i wykonane próby. |

Tempo ustala nauczyciel. Jeśli zadanie 4 jest większe, stanowi kontynuację na kolejnych zajęciach lub zastępuje dodatkową diagnozę. Zadania dodatkowe nie są warunkiem ukończenia podstawowego bloku.

**Podczas pracy:** korzystaj z [tabel składni i krótkich wzorców](SCIAGA.md). W [starterach](startery/README.md) znajdziesz punkty wyjścia. Pełne polecenia i nazwy docelowych plików są poniżej.

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

## Diagnoza i praca domowa

Otwórz [zadanie naprawcze](diagnoza/README.md). Ma własny kontrakt i celowo błędny kod. Wykonaj je na zajęciach lub dokończ w domu zgodnie z ustaleniem prowadzącego.

## Oddanie pracy

Zachowaj źródła i niezbędne pliki danych. W `testy.md` opisz rzeczywiście wykonane próby: dane, oczekiwany wynik, wynik otrzymany i wniosek. Własną instrukcję uruchomienia zapisz w `URUCHOMIENIE.md`, aby zachować treść zadań w tym README. Dołącz dokumentację wskazaną w poleceniu. Zadania oznaczone jako dodatkowe są dla chętnych.

[Spis lekcji](../README.md)
