# Ćwiczenia: Funkcje wywołujące same siebie (rekurencja), sortowanie szybkie oraz kolejki i stosy

**Temat 37 | Lekcje 75-76**

## Przygotowanie

Środowisko i polecenia uruchamiania opisano w [instrukcji głównej](../README.md#uruchamianie). Wystarcza biblioteka standardowa Pythona.

Utwórz pliki wskazane w zadaniach wewnątrz bieżącego folderu lekcji. Kod uruchamiaj w terminalu z tego folderu. Zadania wprowadzają kolejne zmiany; zachowuj wcześniejsze wersje w podfolderach, jeśli wymaga tego polecenie.

## Wymagania implementacji

`silnia(n)` przyjmuje int: n < 0 zgłasza ValueError, n=0 zwraca 1, dla n>0 używa wywołania rekurencyjnego. `quicksort(dane)` wybiera pivot, dzieli dane na mniejsze, równe i większe, rekurencyjnie sortuje części i zwraca nową listę. Przypadek bazowy to długość <=1. Nie używaj `sorted` ani `list.sort`. Stos realizuj listą, kolejkę przez `collections.deque`.

## Zadanie 1. Ślad rekurencji

- Dodaj do silnia komunikat przed wywołaniem rekurencyjnym i przed return.
- Uruchom silnia(3), silnia(0) i silnia(-1).
- Rozróżnij kolejność wejścia do funkcji i powrotu z funkcji.

**Wynik kontrolny:** 6, 1 oraz ValueError.

## Zadanie 2. Quicksort z powtórzeniami

- Napisz quicksort(dane), zwracającą nową listę.
- Sprawdź,, [] oraz [8].
- Nie zmieniaj listy wejściowej i nie usuwaj duplikatów.

**Wynik kontrolny:**,, [], [8].

## Zadanie 3. Historia zmian

- Dodaj na stos napisy „start”, „zmiana A”, „zmiana B”.
- Pobierz wszystkie elementy przez pop, wypisując kolejność.
- Po opróżnieniu wypisz „Brak historii”, zamiast wywoływać kolejne pop.

**Wynik kontrolny:** zmiana B, zmiana A, start, Brak historii.

## Zadanie 4. Obsługa zgłoszeń

- Użyj deque. Dodaj zgłoszenia „Z1”, „Z2”, „Z3” i obsłuż dwa pierwsze.
- Dodaj „Z4”, a potem obsłuż resztę przez popleft.
- Na każdym etapie wypisz obsługiwany identyfikator.

**Wynik kontrolny:** Z1, Z2, Z3, Z4. Kolejka jest pusta.

## Oddanie pracy

Zachowaj źródła i niezbędne pliki danych. W `testy.md` opisz rzeczywiście wykonane próby: dane, oczekiwany wynik, wynik otrzymany i wniosek. Własną instrukcję uruchomienia zapisz w `URUCHOMIENIE.md`, aby zachować treść zadań w tym README. Dołącz dokumentację wskazaną w poleceniu. Zadania oznaczone jako dodatkowe są dla chętnych.

[Spis lekcji](../README.md)
