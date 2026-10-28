# Ćwiczenia: Funkcje wywołujące same siebie (rekurencja), sortowanie szybkie oraz kolejki i stosy

**Temat 37 | Lekcje 75-76**

## Przygotowanie

Środowisko i polecenia uruchamiania opisano w [instrukcji głównej](../README.md#uruchamianie). Wystarcza biblioteka standardowa Pythona.

Utwórz pliki wskazane w zadaniach wewnątrz bieżącego folderu lekcji. Kod uruchamiaj w terminalu z tego folderu. Zadania wprowadzają kolejne zmiany; zachowuj wcześniejsze wersje w podfolderach, jeśli wymaga tego polecenie.

## Wymagania implementacji

`silnia(n)` przyjmuje int: n < 0 zgłasza ValueError, n=0 zwraca 1, dla n>0 używa wywołania rekurencyjnego. `quicksort(dane)` wybiera pivot, dzieli dane na mniejsze, równe i większe, rekurencyjnie sortuje części i zwraca nową listę. Przypadek bazowy to długość <=1. Nie używaj `sorted` ani `list.sort`. Stos realizuj listą, kolejkę przez `collections.deque`.

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

## Diagnoza i praca domowa

Otwórz [zadanie naprawcze](diagnoza/README.md). Ma własny kontrakt i celowo błędny kod. Wykonaj je na zajęciach lub dokończ w domu zgodnie z ustaleniem prowadzącego.

## Oddanie pracy

Zachowaj źródła i niezbędne pliki danych. W `testy.md` opisz rzeczywiście wykonane próby: dane, oczekiwany wynik, wynik otrzymany i wniosek. Własną instrukcję uruchomienia zapisz w `URUCHOMIENIE.md`, aby zachować treść zadań w tym README. Dołącz dokumentację wskazaną w poleceniu. Zadania oznaczone jako dodatkowe są dla chętnych.

[Spis lekcji](../README.md)
