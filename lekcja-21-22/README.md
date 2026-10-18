# Ćwiczenia: Skrócony zapis tworzenia list i słowników oraz jednoczesne numerowanie elementów pętli (enumerate, zip)

**Temat 11 | Lekcje 21-22**

## Przygotowanie

Środowisko i polecenia uruchamiania opisano w [instrukcji głównej](../README.md#uruchamianie). Wystarcza biblioteka standardowa Pythona.

Utwórz pliki wskazane w zadaniach wewnątrz bieżącego folderu lekcji. Kod uruchamiaj w terminalu z tego folderu. Zadania wprowadzają kolejne zmiany; zachowuj wcześniejsze wersje w podfolderach, jeśli wymaga tego polecenie.

## Zadanie 1. Analiza liczb

Dane: `liczby = [-3, 0, 2, -1, 4]`.

1. Napisz `analizuj_liczby(liczby)` za pomocą pętli, warunku i append.
2. Zwróć krotkę zawierającą dwie listy: kwadraty liczb nieujemnych oraz indeksy liczb ujemnych. Indeksy licz od 0; zachowaj kolejność wejścia.
3. Nie zmieniaj wejściowej listy. Funkcja nie pobiera danych i niczego nie wypisuje.
4. W programie głównym wyświetl obie listy z opisami. Wyjaśnij równoważny zapis listy kwadratów jako comprehension.

| Wejście | Kwadraty | Indeksy ujemnych |
|---|---|---|
| [-3, 0, 2, -1, 4] | [0, 4, 16] | [0, 3] |
| [] | [] | [] |
| [-2, -1] | [] | [0, 1] |
| [0, 3] | [0, 9] | [] |

## Zadanie 2. Raport ocen

Dane: `imiona = ["Ala", "Jan", "Ola"]`, `punkty = [18, 12, 20]`. Próg 15 jest szkolny, nie pochodzi z kryteriów CKE. Przyjmujemy listę tekstowych imion i listę liczbowych wyników; nie sprawdzamy zakresu punktów.

1. Napisz `raport_ocen(imiona, punkty)`. Jeśli listy mają różne długości, zwróć None przed użyciem zip.
2. Użyj zip i enumerate z start=1. Zwróć listę krotek `(numer, imie, wynik, status)`.
3. Dla wyniku co najmniej 15 status ma być "zaliczono", w przeciwnym razie "niezaliczono". Zachowaj powtórzone imiona jako osobne wiersze.
4. Funkcja nie zmienia wejścia ani nie wykonuje wejścia/wyjścia. Program główny wyświetla wiersze; dla None komunikat „Różne długości list”, dla [] „Brak danych”.

| Wejście | Oczekiwany wynik funkcji |
|---|---|
| Dane podstawowe | [(1, 'Ala', 18, 'zaliczono'), (2, 'Jan', 12, 'niezaliczono'), (3, 'Ola', 20, 'zaliczono')] |
| [], [] | [] |
| 3 imiona, 2 wyniki | None |
| ['Ala', 'Ala'], [15, 14] | Dwa wiersze: numery 1, 2; statusy zaliczono, niezaliczono |

## Zadanie 3. Aktualizacja cennika

Dane: `pozycje = [("zeszyt", 7), ("dlugopis", 3), ("zeszyt", 8), ("gumka", 2)]`.

1. Napisz `zbuduj_cennik(pozycje)` za pomocą pętli. Zwróć słownik, którego kluczem jest nazwa produktu, a wartością cena.
2. Ostatnia cena danej nazwy zastępuje wcześniejszą. Wejście pozostaje niezmienione, funkcja nie wypisuje danych.
3. W programie głównym wypisz nazwy alfabetycznie, po jednej z ceną. Skorzystaj z sorted(cennik).
4. Wyjaśnij równoważne wyrażenie składane słownika.

Wynik zawiera ceny: zeszyt 8, dlugopis 3, gumka 2. Wypisanie: `dlugopis 3`, `gumka 2`, `zeszyt 8`. Dla pustej listy wynik to `{}`, a pętla wypisująca nie wykonuje żadnego kroku.

## Zadanie 4. Suma kontrolna i cyfra płci PESEL - adaptacja INF.04-01-24.01-SG

**Rdzeń z arkusza:** PESEL przechowywany jako tekst lub tablica, oddzielna funkcja płci zwracająca K/M, oddzielna funkcja sumy zwracająca bool, wczytanie numeru, wywołania funkcji i opisane wyniki. Dziesiąta cyfra określa płeć parzystością, jedenasta służy do kontroli. Algorytm używa wag oraz etapów S, M i R.

**Adaptacja szkolna:** stosujemy tekst, przykład 55030101193, dodatkową kontrolę formatu i poniższy zestaw testów. Po wersji klasycznej porównujemy sumowanie z użyciem zip. 

1. Zainicjuj tekst `pesel = "55030101193"` i sprawdź jego sumę, następnie wczytaj nowy tekst.
2. Napisz `poprawny_format(pesel)`: True wyłącznie dla 11 znaków od "0" do "9". Przy złym formacie program główny wypisuje komunikat i nie wywołuje dwóch pozostałych funkcji.
3. Napisz `okresl_plec(pesel)`: "K", gdy int(pesel[9]) jest parzyste; "M" w przeciwnym razie.
4. Napisz `sprawdz_sume(pesel)`. Dla pierwszych dziesięciu cyfr użyj wag `[1, 3, 7, 9, 1, 3, 7, 9, 1, 3]`. Oblicz sumę iloczynów S, M = S % 10, R = 0 dla M == 0 lub R = 10 - M w innym przypadku. Zwróć wynik porównania R z int(pesel[10]).
5. Dla poprawnego formatu program główny wywołuje obie funkcje i wypisuje pełną nazwę płci oraz zgodność sumy. Odczyt cyfry płci odbywa się także przy niezgodnej sumie; są to dwie niezależne operacje.
6. Dodaj zgodny z kodem nagłówek komentarza, uruchom testy i przygotuj dokumentację opisaną w części „Oddanie pracy”.

Funkcje płci i sumy mają warunek wejściowy: tekst długości 11 zawierający tylko cyfry ASCII. Nie sprawdzają ponownie formatu. Nie wykonują input ani print. Numeru nie zamieniamy w całości na int: utracilibyśmy początkowe zera. isdigit() samo w sobie jest szersze niż dopuszczone tu znaki ASCII, dlatego w przykładzie używamy sprawdzenia przynależności.

| PESEL / wejście | Format | S, M, R | Suma zgodna | Płeć z cyfry |
|---|---|---|---|---|
| 55030101193 | dobry | 87, 7, 3 | True | M |
| 55030101186 | dobry | 84, 4, 6 | True | K |
| 55030101194 | dobry | 87, 7, 3 | False | M |
| 00000000000 | dobry | 0, 0, 0 | True | K |
| 123 | zły | nie obliczamy | nie wywołujemy | nie wywołujemy |
| 5503010119A | zły | nie obliczamy | nie wywołujemy | nie wywołujemy |
| pusty tekst | zły | nie obliczamy | nie wywołujemy | nie wywołujemy |

Zerowy przypadek służy sprawdzeniu gałęzi M == 0. Zgodna suma nie oznacza poprawnej daty urodzenia, nadania numeru ani jego pełnej poprawności. W tej lekcji sprawdzamy tylko format, sumę i cyfrę płci. Dla przykładu podstawowego iloczyny to `[5, 15, 0, 27, 0, 3, 0, 9, 1, 27]`, suma 87.

## Zadanie 5. Dla chętnych: Macierz - autorskie, dodatkowe

Napisz `przetworz_macierz(macierz)`. Za pomocą dwóch pętli zwróć krotkę: lista sum wierszy i lista wszystkich liczb w kolejności wierszy. Funkcja nie zmienia danych ani niczego nie wypisuje. Wiersze mogą mieć różne długości; pusty wiersz ma sumę 0. Program główny wypisuje rezultat. Porównaj kod z dwoma wyrażeniami składanymi.

| Wejście | Wynik |
|---|---|
| [[1, 2, 3], [], [4, 5]] | ([6, 0, 9], [1, 2, 3, 4, 5]) |
| [] | ([], []) |
| [[]] | ([0], []) |
| [[-1, 1], [2]] | ([0, 2], [-1, 1, 2]) |

## Oddanie pracy

Zachowaj źródła i niezbędne pliki danych. W `testy.md` opisz rzeczywiście wykonane próby: dane, oczekiwany wynik, wynik otrzymany i wniosek. Własną instrukcję uruchomienia zapisz w `URUCHOMIENIE.md`, aby zachować treść zadań w tym README. Dołącz dokumentację wskazaną w poleceniu. Zadania oznaczone jako dodatkowe są dla chętnych.

[Spis lekcji](../README.md)
