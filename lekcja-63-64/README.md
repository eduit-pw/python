# Ćwiczenia: Zamiana liczb między systemami dwójkowym, ósemkowym, dziesiętnym i szesnastkowym oraz Schemat Hornera

**Temat 31 | Lekcje 63-64**

## Przygotowanie

Środowisko i polecenia uruchamiania opisano w [instrukcji głównej](../README.md#uruchamianie). Wystarcza biblioteka standardowa Pythona.

Utwórz pliki wskazane w zadaniach wewnątrz bieżącego folderu lekcji. Kod uruchamiaj w terminalu z tego folderu. Zadania wprowadzają kolejne zmiany; zachowuj wcześniejsze wersje w podfolderach, jeśli wymaga tego polecenie.

## Wymagane funkcje

Zapisz zadania jako `zadanie1.py` itd. W zadaniu 2 utwórz `z_binarnego(tekst)`: zaczynasz od wyniku 0, dla każdej cyfry aktualizujesz `wynik = wynik * 2 + cyfra`. W zadaniu 4 `horner(wspolczynniki, x)` przyjmuje współczynniki od najwyższej potęgi; aktualizacja to `wynik = wynik * x + wspolczynnik`. Brakująca potęga wymaga współczynnika 0. Zwracaj wyniki, a wypisywanie umieść w programie głównym.

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

**Przed praktyką:** przeczytaj [ściągę](SCIAGA.md). W [starterach](startery/README.md) znajdziesz punkty wyjścia. Pełne polecenia i nazwy docelowych plików są poniżej.

## Zadanie 1. Konwersje kontrolne

- Przelicz 45 na zapis binarny, ósemkowy i szesnastkowy.
- Wypisz wyniki bez prefiksów, z wielkimi literami w hex.
- Przelicz każdy z otrzymanych napisów z powrotem na int.

**Wynik kontrolny:** 101101, 55, 2D. Każdy powrót daje 45.

## Zadanie 2. Horner i walidacja

- Rozbuduj z_binarnego: odrzucaj pusty napis i znaki inne niż 0 lub 1.
- Wypisz wartości po przetworzeniu kolejnych cyfr napisu 1101.
- Porównaj końcowy wynik z int("1101", 2).

**Wynik kontrolny:** 1, 3, 6, 13. Dla „102” i „” występuje ValueError.

## Zadanie 3. Własny zapis binarny

- Napisz funkcję do_binarnego(n) dla int >= 0, używając dzielenia i reszt.
- Zwróć napis. Nie używaj bin ani format do obliczeń.
- Sprawdź n = 0, 1, 13 oraz odrzuć wartości ujemne.

**Wynik kontrolny:** „0”, „1”, „1101”.

## Zadanie 4. Wielomian z brakującą potęgą

- Zapisz listę współczynników dla 3x³ - 2x + 4.
- Oblicz wartość dla x = 2 za pomocą schematu Hornera.
- Sprawdź x = 0 i x = -1. Wypisz wyniki. Adaptacja zbioru CKE „Schemat Hornera”: własny wielomian.

**Wynik kontrolny:** [3, 0, -2, 4]. Wyniki: 24, 4, 3.

## Diagnoza i praca domowa

Otwórz [zadanie naprawcze](diagnoza/README.md). Ma własny kontrakt i celowo błędny kod. Wykonaj je na zajęciach lub dokończ w domu zgodnie z ustaleniem prowadzącego.

## Oddanie pracy

Zachowaj źródła i niezbędne pliki danych. W `testy.md` opisz rzeczywiście wykonane próby: dane, oczekiwany wynik, wynik otrzymany i wniosek. Własną instrukcję uruchomienia zapisz w `URUCHOMIENIE.md`, aby zachować treść zadań w tym README. Dołącz dokumentację wskazaną w poleceniu. Zadania oznaczone jako dodatkowe są dla chętnych.

[Spis lekcji](../README.md)
