# Ćwiczenia: Wyszukiwanie minimum i maksimum w parach oraz algorytmy sortowania danych (bąbelkowe, przez wstawianie, wybór)

**Temat 45 | Lekcje 89-90**

## Przygotowanie

Środowisko i polecenia uruchamiania opisano w [instrukcji głównej](../README.md#uruchamianie). Wystarcza biblioteka standardowa Pythona.

Utwórz pliki wskazane w zadaniach wewnątrz bieżącego folderu lekcji. Kod uruchamiaj w terminalu z tego folderu. Każde zadanie ma osobny starter. Zadania rozwijające aplikację wykonuj na kopii poprzedniego etapu, zgodnie z instrukcją startera.

## Kontrakty sortowania

Nie używaj `sorted`, `list.sort`, `min` ani `max` do implementacji ćwiczonych algorytmów. Bubble sort zamienia sąsiadów w złej kolejności. Insertion sort przesuwa większe elementy w prawo i wstawia zapamiętaną wartość. Oba modyfikują listę rosnąco; nie usuwają powtórzeń. `Sortowanie` przechowuje 10 liczb; `_indeks_maksimum(start)` zwraca indeks największej wartości w części od start do końca. `sortuj()` kolejno zamienia maksimum z pierwszą pozycją jeszcze nieuporządkowanej części, dając porządek malejący.

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

**Podczas pracy:** korzystaj z [tabel składni i krótkich wzorców](KONSTRUKCJE.md). W [starterach](startery/README.md) znajdziesz punkty wyjścia. Pełne polecenia i nazwy docelowych plików są poniżej.

## Zadanie 1. Min/max parami

**Punkt wyjścia:** [starter zadania 1](startery/zadanie1.py).

- Napisz min_max(dane), zwracającą parę minimum i maksimum dla niepustej listy.
- Porównuj kolejne elementy parami. Obsłuż pozostały pojedynczy element.
- Sprawdź `[7, 2, 9, 4, 1]`, `[7, 2, 9, 4]`, `[5]` oraz `[]`. Dla [] zgłoś ValueError.

**Wynik kontrolny:** (1,9), (2,9), (5,5).

## Zadanie 2. Bubble sort

**Punkt wyjścia:** [starter zadania 2](startery/zadanie2.py).

- Zaimplementuj sortowanie bąbelkowe rosnąco. Wypisz listę przed i po zmianie.
- Sprawdź `[5, 2, 4, 1]`, `[2, 2, 1]`, `[]` oraz `[3]`.
- W pierwszym przykładzie wypisz listę po każdym pełnym przebiegu. Adaptacja INF.04-02-23.06-SG, I: własne dane testowe.

**Wynik kontrolny:** `[1, 2, 4, 5]`, `[1, 2, 2]`, `[]`, `[3]`.

## Zadanie 3. Insertion sort

**Punkt wyjścia:** [starter zadania 3](startery/zadanie3.py).

- Utwórz funkcję wstawianie(dane), modyfikującą listę rosnąco.
- Zapamiętaj wstawianą liczbę i przesuwaj większe elementy do następnych pozycji.
- Sprawdź `[3, 1, 3, 2]` oraz uporządkowaną listę `[1, 2, 3]`.

**Wynik kontrolny:** `[1, 2, 3, 3]` oraz `[1, 2, 3]`.

## Zadanie 4. Dla chętnych: Selection sort w klasie

**Punkt wyjścia:** [starter zadania 4](startery/zadanie4.py).

- Wczytaj 10 liczb z klawiatury do obiektu klasy Sortowanie.
- Zaimplementuj _indeks_maksimum(start) i sortuj() bez sorted oraz list.sort.
- Dane kontrolne: 4,1,7,2,7,0,9,3,5,6. Wypisz wynik malejąco. Adaptacja INF.04-01-21.06-SG, I: własny zestaw kontrolny.

**Wynik kontrolny:** `[9, 7, 7, 6, 5, 4, 3, 2, 1, 0]`.

## Diagnoza i praca domowa

Otwórz [zadanie naprawcze](diagnoza/README.md). Ma własny kontrakt i celowo błędny kod. Wykonaj je na zajęciach lub dokończ w domu zgodnie z ustaleniem prowadzącego.

## Oddanie pracy

Zachowaj źródła i niezbędne pliki danych. W `testy.md` opisz rzeczywiście wykonane próby: dane, oczekiwany wynik, wynik otrzymany i wniosek. Własną instrukcję uruchomienia zapisz w `URUCHOMIENIE.md`, aby zachować treść zadań w tym README. Dołącz dokumentację wskazaną w poleceniu. Zadania oznaczone jako dodatkowe są dla chętnych.

[Spis lekcji](../README.md)

## Utrwalanie Git w ramach tego bloku

Przed zmianą sprawdź `git status`, a po działającej poprawce obejrzyj `git diff`. Zapisz mały commit z opisem wykonanej zmiany. Czynność zajmuje 2–3 minuty przewidziane na sprawdzenie pracy.
