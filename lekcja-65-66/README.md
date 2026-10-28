# Ćwiczenia: Szyfrowanie danych: zamiana liter w tekście, szyfr Cezara oraz szyfr GADERYPOLUKI

**Temat 32 | Lekcje 65-66**

## Przygotowanie

Środowisko i polecenia uruchamiania opisano w [instrukcji głównej](../README.md#uruchamianie). Wystarcza biblioteka standardowa Pythona.

Utwórz pliki wskazane w zadaniach wewnątrz bieżącego folderu lekcji. Kod uruchamiaj w terminalu z tego folderu. Zadania wprowadzają kolejne zmiany; zachowuj wcześniejsze wersje w podfolderach, jeśli wymaga tego polecenie.

## Umowa szyfrów i przypadki testowe

Napisz `cezar(tekst, klucz)` dla małych liter a-z i spacji oraz dowolnego całkowitego klucza. Spacje zachowaj; litery przesuwaj z zawijaniem modulo 26. Szyfrowanie i odszyfrowanie różnią się znakiem klucza. Funkcja zwraca str i nie wykonuje input/print.

| Tekst | Klucz | Wynik |
| --- | ---: | --- |
| abc | 3 | def |
| xyz | 3 | abc |
| def | -3 | abc |
| abc | 29 | def |
| ab cd | 2 | cd ef |

GADERYPOLUKI zamienia w obie strony litery par `GA`, `DE`, `RY`, `PO`, `LU`, `KI`. W tej wersji zmieniasz wyłącznie wielkie litery; inne znaki pozostają bez zmian. Napisz własne funkcje, nie kopiuj implementacji z lekcji testowania.

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

## Zadanie 1. Funkcja Cezara

- Napisz cezar(tekst, klucz), zgodnie z umową powyżej.
- Wczytaj tekst i klucz w programie głównym. Wynik wypisz z etykietą.
- Sprawdź pięć przypadków z powyższej tabeli oraz pusty napis z kluczem 3. Adaptacja INF.04-02-25.06-SG, I: funkcja i program konsolowy.

**Wynik kontrolny:** wszystkie wyniki zgodne z tabelą, pusty napis daje „”.

## Zadanie 2. Testy jednostkowe

- Napisz pięć osobnych metod unittest dla tabeli przypadków Cezara.
- Nadaj nazwy opisujące przypadki. Użyj assertEqual.
- Uruchom python -m unittest -v. Dodaj osobny test klucza 0. Adaptacja INF.04-02-25.06-SG, III: dodatkowy test klucza 0.

**Wynik kontrolny:** 6 testów kończy się OK.

## Zadanie 3. Szyfr z par

- Napisz gaderypoluki(tekst) dla wielkich liter. Pozostałe znaki zachowaj.
- Zbuduj słownik par w kodzie i użyj go w pętli po tekście.
- Sprawdź tekst „KOT ALA!” oraz pusty napis.

**Wynik kontrolny:** „IPT GUG!” i „”.

## Zadanie 4. Sprawdzenie odwracalności

- Dla Cezara użyj „ala ma kota” i kluczy -29, 0, 3, 52.
- Zaszyfruj i odszyfruj każdy wynik, porównaj z oryginałem.
- Dwa razy zastosuj GADERYPOLUKI do „KOT ALA!”.

**Wynik kontrolny:** każdy tekst wraca do postaci wejściowej.

## Diagnoza i praca domowa

Otwórz [zadanie naprawcze](diagnoza/README.md). Ma własny kontrakt i celowo błędny kod. Wykonaj je na zajęciach lub dokończ w domu zgodnie z ustaleniem prowadzącego.

## Oddanie pracy

Zachowaj źródła i niezbędne pliki danych. W `testy.md` opisz rzeczywiście wykonane próby: dane, oczekiwany wynik, wynik otrzymany i wniosek. Własną instrukcję uruchomienia zapisz w `URUCHOMIENIE.md`, aby zachować treść zadań w tym README. Dołącz dokumentację wskazaną w poleceniu. Zadania oznaczone jako dodatkowe są dla chętnych.

[Spis lekcji](../README.md)
