# Ćwiczenia: Działania na liczbach, warunki logiczne oraz podejmowanie decyzji w programie (if, elif, else)

**Temat 3 | Lekcje 5-6**

## Przygotowanie

Środowisko i polecenia uruchamiania opisano w [instrukcji głównej](../README.md#uruchamianie). Wystarcza biblioteka standardowa Pythona.

Utwórz pliki wskazane w zadaniach wewnątrz bieżącego folderu lekcji. Kod uruchamiaj w terminalu z tego folderu. Zadania wprowadzają kolejne zmiany; zachowuj wcześniejsze wersje w podfolderach, jeśli wymaga tego polecenie.

## Zadanie 1. Kalkulator dwóch liczb

1. Pobierz dwie liczby całkowite a i b.
2. Wypisz sumę, różnicę a - b oraz iloczyn.
3. Dla b różnego od 0 wypisz a / b z dwoma miejscami po kropce, a // b oraz a % b.
4. Dla b = 0 wypisz „Nie można dzielić przez zero” i pomiń trzy działania dzielenia.

Plik zadanie1.py. Etykiety wyników: Suma, Różnica, Iloczyn, Iloraz, Podłoga, Reszta.

| Wynik | a = 7, b = 3 | a = -7, b = 3 | a = 7, b = 0 |
| --- | --- | --- | --- |
| Suma | 10 | -4 | 7 |
| Różnica | 4 | -10 | 7 |
| Iloczyn | 21 | -21 | 0 |
| Iloraz | 2.33 | -2.33 | Pomiń |
| Podłoga | 2 | -3 | Pomiń |
| Reszta | 1 | 2 | Pomiń |

Dla b = 0 po iloczynie wypisz: Nie można dzielić przez zero.

Każdy wynik wypisz w osobnym wierszu w postaci `Suma: 10`, analogicznie pozostałe etykiety. „Podłoga” nazywa wynik `a // b`. Dodatkowo sprawdź (0, 3), (7, -3) i (0, 0).

## Zadanie 2. Szkolny cennik biletów

| Kolejność | Warunek | Cena |
| --- | --- | --- |
| 1 | Wiek 0-6 | 0 zł |
| 2 | Wiek 7-17 lub 65-120 | 10 zł |
| 3 | Pozostałe osoby do 26 lat<br>z kartą T | 12 zł |
| 4 | Pozostałe osoby | 20 zł |

Cennik autorski. Obowiązuje pierwsza pasująca reguła, bez sumowania rabatów.

1. Pobierz wiek jako liczbę całkowitą i kartę jako tekst T albo N.
2. Wiek poza 0-120: wypisz „Błędny wiek”. Nie obliczaj ceny.
3. Dla poprawnego wieku i karty innej niż T lub N wypisz „Błędna karta”.
4. Dla poprawnych danych wybierz cenę z cennika przez if…elif…else i wypisz „Cena: … zł”.

Plik zadanie2.py. Przy obu błędach zgłoś Błędny wiek. Karta: tylko wielkie T lub N.

| Wiek | Karta | Wynik |
| --- | --- | --- |
| 0 i 6 | N | Cena: 0 zł |
| 7 i 17 | T | Cena: 10 zł |
| 18 i 26 | T | Cena: 12 zł |
| 27 i 64 | T | Cena: 20 zł |
| 65 i 120 | N | Cena: 10 zł |
| -1 i 121 | X | Błędny wiek |
| 20 | X | Błędna karta |

Każdy wiek z wiersza sprawdź osobno. Dodatkowo: wiek 20 i karta N dają cenę 20 zł.

Dodatkowe próby: (6, T), (18, N), (26, N), (65, T), (20, t), (20, pusty wpis), (20, pojedyncza spacja). Warunki dla wieku i karty są rozłączne w raporcie: wypisujemy jeden komunikat o pierwszym błędzie.

## Zadanie 3. Cena i koszt przesyłek - adaptacja arkusza

**Pochodzenie:** projektowe `02_zadania_desktopowe.md`, D.2, odpowiadające arkuszowi **INF.04-01-23.06-SG**, czerwiec 2023, część II, strona 3 z 5. Ceny potwierdzono w arkuszu i w zasadach, R.3.7.

| Wybór | Rodzaj przesyłki | Cena jednej sztuki |
| --- | --- | --- |
| 1 | Pocztówka | 1.00 zł |
| 2 | List | 1.50 zł |
| 3 | Paczka | 10.00 zł |

To **adaptacja fragmentu**, a nie całe zadanie egzaminacyjne. Zachowujemy trzy rodzaje przesyłek i ich ceny. Wybór pól radiowych zastępujemy menu 1-3. Dodajemy liczbę sztuk 1-100 i koszt łączny. Pomijamy GUI, grafiki, dane adresowe i kontrolę kodu pocztowego. Tak dobrana treść ćwiczy warunki przed tematami o napisach i aplikacjach okienkowych. Ceny są danymi historycznej specyfikacji, nie ofertą dzisiejszej poczty.

1. Pokaż menu: 1 - pocztówka, 2 - list, 3 - paczka. Pobierz wybór i liczbę sztuk jako liczby całkowite.
2. Wybór poza 1-3: wypisz „Błędny wybór”. Nie obliczaj kosztu.
3. Dla poprawnego wyboru i liczby sztuk poza 1-100 wypisz „Błędna liczba sztuk”.
4. Dla poprawnych danych wybierz cenę przez if…elif…else. Wypisz „Cena: … zł” i „Koszt: … zł”, oba z .2f.

Plik zadanie3.py. Koszt = cena * liczba sztuk. Przy obu błędach zgłoś Błędny wybór.

| Wybór | Sztuki | Wynik |
| --- | --- | --- |
| 1 | 1 | Cena: 1.00 zł<br>Koszt: 1.00 zł |
| 2 | 3 | Cena: 1.50 zł<br>Koszt: 4.50 zł |
| 3 | 100 | Cena: 10.00 zł<br>Koszt: 1000.00 zł |
| 0 | 0 | Błędny wybór |
| 2 | 101 | Błędna liczba sztuk |

Cena i koszt zajmują dwie osobne linie. Dla błędnych danych wypisz jeden komunikat.

Dodatkowe próby: (1, 100), (2, 1), (3, 1), (1, 0), (4, 2). Cena i koszt mają kropkę oraz dokładnie dwa miejsca po niej. Menu wypisujemy zawsze przed wczytaniem obu liczb.

## Zadanie 4. Analiza trzech liczb

1. Pobierz trzy liczby całkowite a, b i c.
2. Wyznacz minimum i maksimum przez porównania. Zacznij od a. Nie używaj min() ani max().
3. Wypisz minimum, maksimum i sumę jako liczby całkowite. Średnią arytmetyczną wypisz z dwoma miejscami po kropce.
4. Wypisz jedną kategorię: „Wszystkie równe”, „Dwie równe” albo „Wszystkie różne”.

Plik zadanie4.py. Etykiety: Minimum, Maksimum, Suma, Średnia. Każdy wynik wypisz osobno. Równość trzech liczb sprawdź przed parą.

| a, b, c | Minimum / maksimum | Suma / średnia | Kategoria |
| --- | --- | --- | --- |
| 2, 7, 4 | 2 / 7 | 13 / 4.33 | Wszystkie różne |
| -5, -2, -9 | -9 / -2 | -16 / -5.33 | Wszystkie różne |
| 3, 3, 3 | 3 / 3 | 9 / 3.00 | Wszystkie równe |
| 4, 4, 1 | 1 / 4 | 9 / 3.00 | Dwie równe |
| 0, 0, 0 | 0 / 0 | 0 / 0.00 | Wszystkie równe |

Średnia = (a + b + c) / 3. Każdy wynik i kategorię wypisz w osobnej linii.

Każdy wynik wypisz w osobnym wierszu z etykietą: `Minimum: …`, `Maksimum: …`, `Suma: …`, `Średnia: …`. Następnie wypisz kategorię. „Dwie równe” oznacza dokładnie jedną równą parę i inną trzecią liczbę. Sprawdź też wszystkie pozycje pary, np. (4, 1, 4) i (1, 4, 4), oraz wszystkie kolejności trzech różnych liczb. Nie używamy list, sortowania ani pętli.

## Zadanie 5 dla chętnych. Rok przestępny

1. Pobierz całkowity rok w zakresie 1-9999. Poza nim wypisz „Błędny rok”.
2. Zastosuj regułę kalendarza gregoriańskiego: podzielność przez 400 albo jednoczesna podzielność przez 4 i brak podzielności przez 100.
3. Dla poprawnego roku wypisz „Przestępny” albo „Zwykły”. Zapisz `zadanie5.py`, bez bibliotek.

Szkolne uproszczenie: stosujemy tę samą regułę do całego zakresu, bez modelowania historycznego wprowadzenia kalendarza. To ćwiczenie autorskie, bez przypisania do arkusza INF.04.

| Rok | Oczekiwany wynik | Przyczyna |
| --- | --- | --- |
| 2024 | Przestępny | Podzielny przez 4, nie przez 100 |
| 1900 | Zwykły | Podzielny przez 100, nie przez 400 |
| 2000 | Przestępny | Podzielny przez 400 |
| 2023 | Zwykły | Niepodzielny przez 4 |
| 0 i 10000 | Błędny rok | Poza zakresem 1-9999 |

## Oddanie pracy

Zachowaj źródła i niezbędne pliki danych. W `testy.md` opisz rzeczywiście wykonane próby: dane, oczekiwany wynik, wynik otrzymany i wniosek. Własną instrukcję uruchomienia zapisz w `URUCHOMIENIE.md`, aby zachować treść zadań w tym README. Dołącz dokumentację wskazaną w poleceniu. Zadania oznaczone jako dodatkowe są dla chętnych.

[Spis lekcji](../README.md)
