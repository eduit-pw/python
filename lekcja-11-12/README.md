# Ćwiczenia: Tworzenie własnych funkcji, przekazywanie argumentów, zwracanie wyników oraz oznaczanie typów danych

**Temat 6 | Lekcje 11-12**

## Przygotowanie

Środowisko i polecenia uruchamiania opisano w [instrukcji głównej](../README.md#uruchamianie). Wystarcza biblioteka standardowa Pythona.

Utwórz pliki wskazane w zadaniach wewnątrz bieżącego folderu lekcji. Kod uruchamiaj w terminalu z tego folderu. Zadania wprowadzają kolejne zmiany; zachowuj wcześniejsze wersje w podfolderach, jeśli wymaga tego polecenie.

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

## Zadanie 1. Pole i obwód, szkolne

**Polecenie:** utwórz pole_prostokata(szerokosc: float, wysokosc: float) -> float i obwod_prostokata(szerokosc: float, wysokosc: float) -> float. Dla nieujemnych boków zwracaj odpowiednio ich iloczyn i 2 * (szerokosc + wysokosc). Funkcje nie odczytują i nie wypisują danych. W programie głównym wykonaj testy. Przyjmujemy poprawne, nieujemne wartości float; zero to dopuszczony przypadek graniczny do testowania wzoru.

| Szerokość | Wysokość | Pole | Obwód |
|---:|---:|---:|---:|
| 2.5 | 4.0 | 10.0 | 13.0 |
| 1.0 | 1.0 | 1.0 | 4.0 |
| 0.0 | 4.0 | 0.0 | 8.0 |

## Zadanie 2. Palindrom, szkolne

**Polecenie:** napisz czy_palindrom(tekst: str) -> bool. Usuń białe znaki z końców przez strip, zwykłe spacje wewnątrz przez replace(" ", "") i zamień wielkie litery na małe przez lower. Pusty wynik oznacza False. Porównuj znak z początku i końca, przesuwając dwa indeksy pętlą while. Przy różnicy zwróć False, a po zakończeniu porównań True. Nie używaj odwracania wycinkiem [::-1]. Wypisywanie umieść poza funkcją.

| Argument | Wynik |
|---|---|
| " Kajak " | True |
| "Kobyła ma mały bok" | True |
| "A" | True |
| "Python" | False |
| "   " lub "" | False |

## Zadanie 3. Kalkulator przesyłki, szkolne

**Polecenie:** podziel program na trzy funkcje i program główny:

1. czy_masa_poprawna(masa: float) -> bool zwraca True dla 0 < masa <= 20, w pozostałych przypadkach False.
2. cena_przesylki(masa: float) -> float przyjmuje już sprawdzoną masę: do 1 kg włącznie koszt 12.00 zł, powyżej 1 do 5 kg włącznie 18.00 zł, powyżej 5 do 20 kg włącznie 30.00 zł. Są to umowne dane ćwiczenia.
3. opis_przesylki(masa: float, cena: float) -> str zwraca napis Masa: {masa:.2f} kg, koszt: {cena:.2f} zł.
4. Program główny wczytuje float(input(...)), ponawia odczyt, dopóki masa jest poza zakresem, następnie wywołuje funkcję ceny i funkcję opisu oraz wypisuje raport. Użytkownik wpisuje skończone liczby, z kropką jako separatorem dziesiętnym. Obsługa nienumerycznego tekstu jest poza zakresem tej lekcji.

| Masa | Poprawna? | Cena dla poprawnej masy |
|---:|---|---:|
| 0.0 | False | Nie wywołuj funkcji ceny |
| 1.0 | True | 12.00 zł |
| 1.01 | True | 18.00 zł |
| 5.0 | True | 18.00 zł |
| 5.01 | True | 30.00 zł |
| 20.0 | True | 30.00 zł |
| 20.01 | False | Nie wywołuj funkcji ceny |

## Zadanie 4. Narzędzia tekstowe, adaptacja INF.04

**Źródło:** CKE, INF.04-02-24.01-SG, część I.

**Polecenie:** zaimplementuj dwie funkcje. policz_samogloski ma zwracać liczbę znaków należących do "aąeęiouóyAĄEĘIOUÓY". usun_powtorzenia ma pozostawiać jeden znak z każdej serii identycznych sąsiadów. Wielkość liter ma znaczenie przy porównywaniu powtórzeń. Dla None lub pustego napisu zwracaj odpowiednio 0 i "". Funkcje nie odczytują ani nie wypisują danych. Program główny wczytuje napis i prezentuje oba wyniki. Sprawdź także None przez bezpośrednie wywołania testowe - input nie zwraca None.

Na tej lekcji używaj zwykłych funkcji. Jest to adaptacja algorytmów; klasę z metodami statycznymi ćwiczymy w temacie 15.

| Argument | Samogłoski | Tekst po usunięciu sąsiadujących powtórzeń |
|---|---:|---|
| "aaabbcdd" | 3 | "abcd" |
| "Abba;;;to  zespół" | 5 | "Aba;to zespół" |
| "Aa" | 2 | "Aa" |
| "" | 0 | "" |
| None | 0 | "" |

## Zadanie 5. Dla chętnych: Cyfry w raporcie - opcjonalne / domowe

**Polecenie:** utwórz policz_cyfry(tekst: str) -> int i zbuduj_raport(tekst: str) -> str. Pierwsza funkcja liczy wyłącznie znaki od "0" do "9" jawną pętlą. Druga wywołuje pierwszą i zwraca komunikat Cyfry: {liczba}. Testy: "Błąd 404, port 80" daje 5, "ABC" daje 0, "" daje 0. Użyj przynależności do napisu "0123456789", aby kontrakt obejmował wyłącznie cyfry ASCII.

## Diagnoza i praca domowa

Otwórz [zadanie naprawcze](diagnoza/README.md). Ma własny kontrakt i celowo błędny kod. Wykonaj je na zajęciach lub dokończ w domu zgodnie z ustaleniem prowadzącego.

## Oddanie pracy

Zachowaj źródła i niezbędne pliki danych. W `testy.md` opisz rzeczywiście wykonane próby: dane, oczekiwany wynik, wynik otrzymany i wniosek. Własną instrukcję uruchomienia zapisz w `URUCHOMIENIE.md`, aby zachować treść zadań w tym README. Dołącz dokumentację wskazaną w poleceniu. Zadania oznaczone jako dodatkowe są dla chętnych.

[Spis lekcji](../README.md)
