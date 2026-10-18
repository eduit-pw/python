# Ćwiczenia: Wyszukiwanie minimum i maksimum w parach oraz algorytmy sortowania danych (bąbelkowe, przez wstawianie, wybór)

**Temat 36 | Lekcje 73-74**

## Przygotowanie

Środowisko i polecenia uruchamiania opisano w [instrukcji głównej](../README.md#uruchamianie). Wystarcza biblioteka standardowa Pythona.

Utwórz pliki wskazane w zadaniach wewnątrz bieżącego folderu lekcji. Kod uruchamiaj w terminalu z tego folderu. Zadania wprowadzają kolejne zmiany; zachowuj wcześniejsze wersje w podfolderach, jeśli wymaga tego polecenie.

## Kontrakty sortowania

Nie używaj `sorted`, `list.sort`, `min` ani `max` do implementacji ćwiczonych algorytmów. Bubble sort zamienia sąsiadów w złej kolejności. Insertion sort przesuwa większe elementy w prawo i wstawia zapamiętaną wartość. Oba modyfikują listę rosnąco; nie usuwają powtórzeń. `Sortowanie` przechowuje 10 liczb; `_indeks_maksimum(start)` zwraca indeks największej wartości w części od start do końca. `sortuj()` kolejno zamienia maksimum z pierwszą pozycją jeszcze nieuporządkowanej części, dając porządek malejący.

## Zadanie 1. Min/max parami

- Napisz min_max(dane), zwracającą parę minimum i maksimum dla niepustej listy.
- Porównuj kolejne elementy parami. Obsłuż pozostały pojedynczy element.
- Sprawdź,, [5] oraz []. Dla [] zgłoś ValueError.

**Wynik kontrolny:** (1,9), (2,9), (5,5).

## Zadanie 2. Bubble sort

- Zaimplementuj sortowanie bąbelkowe rosnąco. Wypisz listę przed i po zmianie.
- Sprawdź,, [] oraz [3].
- W pierwszym przykładzie wypisz listę po każdym pełnym przebiegu. Adaptacja INF.04-02-23.06-SG, I: własne dane testowe.

**Wynik kontrolny:**,, [], [3].

## Zadanie 3. Insertion sort

- Utwórz funkcję wstawianie(dane), modyfikującą listę rosnąco.
- Zapamiętaj wstawianą liczbę i przesuwaj większe elementy do następnych pozycji.
- Sprawdź oraz listę już uporządkowaną.

**Wynik kontrolny:** oraz.

## Zadanie 4. Selection sort w klasie

- Wczytaj 10 liczb z klawiatury do obiektu klasy Sortowanie.
- Zaimplementuj _indeks_maksimum(start) i sortuj() bez sorted oraz list.sort.
- Dane kontrolne: 4,1,7,2,7,0,9,3,5,6. Wypisz wynik malejąco. Adaptacja INF.04-01-21.06-SG, I: własny zestaw kontrolny.

**Wynik kontrolny:**.

## Oddanie pracy

Zachowaj źródła i niezbędne pliki danych. W `testy.md` opisz rzeczywiście wykonane próby: dane, oczekiwany wynik, wynik otrzymany i wniosek. Własną instrukcję uruchomienia zapisz w `URUCHOMIENIE.md`, aby zachować treść zadań w tym README. Dołącz dokumentację wskazaną w poleceniu. Zadania oznaczone jako dodatkowe są dla chętnych.

[Spis lekcji](../README.md)
