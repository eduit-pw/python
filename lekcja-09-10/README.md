# Ćwiczenia: Praca z tekstem: łączenie, wycinanie fragmentów napisów oraz metody tekstowe

**Temat 5 | Lekcje 9-10**

## Przygotowanie

Środowisko i polecenia uruchamiania opisano w [instrukcji głównej](../README.md#uruchamianie). Wystarcza biblioteka standardowa Pythona.

Utwórz pliki wskazane w zadaniach wewnątrz bieżącego folderu lekcji. Kod uruchamiaj w terminalu z tego folderu. Zadania wprowadzają kolejne zmiany; zachowuj wcześniejsze wersje w podfolderach, jeśli wymaga tego polecenie.

## Zadanie 1

1. Pobierz imię, nazwisko i rok. Usuń białe znaki z brzegów każdego wpisu.
2. Imię: minimum 2 znaki. Nazwisko: minimum 3. Rok: dokładnie 4 cyfry od 0 do 9.
3. Błędne dane: wypisz „Błędne dane”. W pozostałych przypadkach utwórz identyfikator.
4. Połącz 3 pierwsze znaki nazwiska, 2 pierwsze imienia i 2 ostatnie roku. Litery zmień na małe.

Plik: zadanie1.py. Identyfikator utworzony tym sposobem może się powtarzać.

| Imię, nazwisko, rok | Oczekiwany wynik |
| --- | --- |
| Jan, Kowalski, 2007 | kowja07 |
|   Ala  , Nowak, 2005 | nowal05 |
| J, Nowak, 2005 | Błędne dane |
| Jan, Nowak, 20²5 | Błędne dane |

Nie konwertuj całego roku na int: potrzebujesz jego ostatnich znaków.

## Zadanie 2

1. Pobierz jedną linię tekstu. Zamień litery na małe.
2. Podziel ją metodą split() bez argumentu i połącz pojedynczą spacją.
3. Wypisz „Tekst: …” oraz „Słowa: …”. Liczbę słów odczytaj z liczby pól.
4. Gdy nie ma słów, wypisz wyłącznie „Brak tekstu”.

Plik: zadanie2.py. Zachowaj interpunkcję. Nie usuwaj polskich liter.

| Wejście | Oczekiwane wyjście |
| --- | --- |
|   ALA   ma kota   | Tekst: ala ma kota / Słowa: 3 |
| Hej, świecie! | Tekst: hej, świecie! / Słowa: 2 |
| Same spacje lub pusty wpis | Brak tekstu |

W tym zadaniu „słowo” oznacza pole oddzielone białymi znakami.

## Zadanie 3

1. Pobierz wpis: metoda | ścieżka | kod. Rozdziel go znakiem | i oczyść pola.
2. Wymagaj dokładnie 3 pól. Metoda po upper(): GET lub POST.
3. Ścieżka musi zaczynać się od /. Kod: dokładnie 3 cyfry ASCII oraz wartość od 100 do 599.
4. Przy błędzie wypisz „Błędny rekord”. Poprawny rekord wypisz jako METODA;ścieżka;kod.

Plik: zadanie3.py. Sprawdź poprawny rekord, brakujące pole i błędny kod.

### Klasyfikacja statusu

1. Po poprawnym rekordzie wypisz kategorię kodu.
2. 200-299: „Sukces”. 400-599: „Błąd”. Pozostałe: „Inny status”.
3. Przykład: get | /start | 200 daje GET;/start;200, a w kolejnej linii Sukces.
4. Sprawdź także: POST | /login | 403 oraz GET | start | 200.

Pierwszy dodatkowy przykład daje POST;/login;403 i Błąd. Drugi: Błędny rekord.

## Zadanie 4

1. Pobierz PESEL jako tekst. Usuń białe znaki z brzegów.
2. Wymagaj 11 cyfr od 0 do 9. Przy błędzie wypisz „Błędny format PESEL” i pomiń obliczenia.
3. Odczytaj 10. cyfrę przez pesel[9]. Parzysta: „Kobieta”. Nieparzysta: „Mężczyzna”.
4. Potem oblicz cyfrę kontrolną według opisu wag i sumy poniżej.

Plik: zadanie4.py. Badamy format, płeć i sumę kontrolną, bez dekodowania daty.

### Suma kontrolna

1. Pierwsze 10 cyfr pomnóż kolejno przez wagi: 1, 3, 7, 9, 1, 3, 7, 9, 1, 3.
2. Zsumuj iloczyny. Oblicz resztę: reszta = suma % 10.
3. Jeżeli reszta == 0, cyfra kontrolna wynosi 0. W przeciwnym przypadku wynosi 10 - reszta.
4. Porównaj wynik z int(pesel[10]). Wypisz „Suma zgodna” albo „Suma niezgodna”.

Wagi możesz przechować jako napis "1379137913" i odczytywać jego cyfry.

| Wejście | Oczekiwane wyjście |
|---|---|
| 55030101193 | Mężczyzna / Suma zgodna |
| 55030101194 | Mężczyzna / Suma niezgodna |
| 04251208945 | Kobieta / Suma niezgodna |
| 00000000000 | Kobieta / Suma zgodna |
| 123 lub 5503010119² | Błędny format PESEL |

**Zakres adaptacji:** algorytm z INF.04-01-24.01-SG, bez dwóch funkcji wymaganych w oryginale. Dodatkowo walidujemy format. Nie realizujemy aplikacji desktopowej ani całej dokumentacji egzaminacyjnej. W oryginale występuje inicjalizacja numeru i późniejsze testowanie wejścia z klawiatury; tutaj pobieramy jeden numer testowy. Nie korzystamy z danych osobowych uczniów.

## Zadanie 5 dla chętnych: palindrom

Pobierz zdanie. Usuń białe znaki z brzegów, zmień litery na małe i usuń wyłącznie spacje ASCII. Zachowaj interpunkcję i tabulatory wewnątrz. Pusty wynik daje „Brak tekstu”. Inny wynik porównaj z jego odwróceniem przez `[::-1]` i wypisz „Palindrom” albo „Nie jest palindromem”.

Próby: `Kobyła ma mały bok` → Palindrom, `A!` → Nie jest palindromem, same spacje → Brak tekstu. To zadanie autorskie, nie pełna normalizacja tekstu naturalnego. W kolejnym temacie można wrócić do tego problemu przy definiowaniu funkcji.

## Oddanie pracy

Zachowaj źródła i niezbędne pliki danych. W `testy.md` opisz rzeczywiście wykonane próby: dane, oczekiwany wynik, wynik otrzymany i wniosek. Własną instrukcję uruchomienia zapisz w `URUCHOMIENIE.md`, aby zachować treść zadań w tym README. Dołącz dokumentację wskazaną w poleceniu. Zadania oznaczone jako dodatkowe są dla chętnych.

[Spis lekcji](../README.md)
