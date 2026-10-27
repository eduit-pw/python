# Ćwiczenia: Zmienne, proste typy danych oraz pobieranie i formatowanie wyświetlanych informacji (f-string)

**Temat 2 | Lekcje 3-4**

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

## Zadanie 1. Wizytówka ucznia

1. Pobierz imię, nazwisko, klasę i nazwę kierunku jako tekst.
2. Pobierz numer w dzienniku jako int. Przyjmujemy numery 1-999.
3. Wypisz osobno: Uczeń, Klasa, Numer, Kierunek. Imię i nazwisko połącz w jednym f-stringu.
4. Numer pokaż w formacie 03d, np. 7 jako 007.

Plik zadanie1.py. Dane wpisuj kolejno: imię, nazwisko, klasa, kierunek, numer.

**Przykład pierwszego uruchomienia:**

Wejście, kolejno po jednym wpisie:

```text
Ala
Nowak
3TP
Technik programista
7
```

Wyjście, bez pytań przy input():

```text
Uczeń: Ala Nowak
Klasa: 3TP
Numer: 007
Kierunek: Technik programista
```

**Dodatkowe próby:**

Próba 2, kolejne wpisy: `Jan`, `Lis`, `2TP`, `Informatyka`, `12`.

```text
Uczeń: Jan Lis
Klasa: 2TP
Numer: 012
Kierunek: Informatyka
```

Próba 3, kolejne wpisy: `Żaneta`, `Wójcik`, `1TP`, `Programowanie`, `999`.

```text
Uczeń: Żaneta Wójcik
Klasa: 1TP
Numer: 999
Kierunek: Programowanie
```

Imię i nazwisko tworzą jeden wiersz. Kierunek też wypisz w jednym wierszu po etykiecie. Numer zachowuje typ int, a zera dodajemy dopiero przy wyświetlaniu.

## Zadanie 2. Podsumowanie zamówienia

1. Pobierz nazwę produktu, kod produktu, cenę sztuki, liczbę sztuk i wpłatę. Kod pozostaje tekstem.
2. Przyjmujemy cenę co najmniej 0, liczbę sztuk 0-999 i wpłatę nie mniejszą od kosztu.
3. Oblicz koszt = cena * sztuki oraz resztę = wpłata - koszt.
4. Wypisz Produkt, Kod, Sztuki, Cena, Koszt, Wpłata, Reszta. Wszystkie kwoty pokaż z .2f i jednostką zł.

Plik zadanie2.py. Cena i wpłata mają typ float. Liczba sztuk ma typ int.

**Przykład pierwszego uruchomienia:**

Wejście, kolejno po jednym wpisie:

```text
Zeszyt
0007
7.5
3
30
```

Wyjście, bez pytań przy input():

```text
Produkt: Zeszyt
Kod: 0007
Sztuki: 3
Cena: 7.50 zł
Koszt: 22.50 zł
Wpłata: 30.00 zł
Reszta: 7.50 zł
```

**Dodatkowe próby:**

Próba 2, kolejne wpisy: `Gumka`, `0012`, `2.5`, `0`, `0`.

```text
Produkt: Gumka
Kod: 0012
Sztuki: 0
Cena: 2.50 zł
Koszt: 0.00 zł
Wpłata: 0.00 zł
Reszta: 0.00 zł
```

Próba 3, kolejne wpisy: `Długopis`, `0001`, `2.5`, `4`, `10`.

```text
Produkt: Długopis
Kod: 0001
Sztuki: 4
Cena: 2.50 zł
Koszt: 10.00 zł
Wpłata: 10.00 zł
Reszta: 0.00 zł
```

Kolejność odczytu: nazwa, kod, cena, liczba sztuk, wpłata. W tej symulacji wpłata jest wystarczająca, więc reszta nie jest ujemna. Zero sztuk jest dozwolone. Kod `0007` zachowuje wszystkie znaki. Nie wymagamy tabeli ani wyrównania w tym zadaniu.

## Zadanie 3. Raport trzech pomiarów

1. Pobierz nazwę stacji, kod czujnika i trzy temperatury. Kod jest tekstem, temperatury mają typ float.
2. Przyjmujemy temperatury od -50 do 60 stopni Celsjusza.
3. Oblicz sumę pomiarów oraz średnią: suma / 3.
4. Wypisz Stacja, Czujnik, Pomiar 1, Pomiar 2, Pomiar 3, Suma, Średnia. Wyniki liczbowe pokaż z .2f.

Plik zadanie3.py. Jednostka pomiarów i średniej: °C. Sumę pokaż bez jednostki.

**Przykład pierwszego uruchomienia:**

Wejście, kolejno po jednym wpisie:

```text
Sala 12
0019
18.5
20
21.5
```

Wyjście, bez pytań przy input():

```text
Stacja: Sala 12
Czujnik: 0019
Pomiar 1: 18.50 °C
Pomiar 2: 20.00 °C
Pomiar 3: 21.50 °C
Suma: 60.00
Średnia: 20.00 °C
```

**Dodatkowe próby:**

Próba 2, kolejne wpisy: `Magazyn`, `0002`, `-5`, `0`, `5`.

```text
Stacja: Magazyn
Czujnik: 0002
Pomiar 1: -5.00 °C
Pomiar 2: 0.00 °C
Pomiar 3: 5.00 °C
Suma: 0.00
Średnia: 0.00 °C
```

Próba 3, kolejne wpisy: `Sala 1`, `0001`, `0`, `0`, `0`.

```text
Stacja: Sala 1
Czujnik: 0001
Pomiar 1: 0.00 °C
Pomiar 2: 0.00 °C
Pomiar 3: 0.00 °C
Suma: 0.00
Średnia: 0.00 °C
```

Średnia dotyczy trzech podanych wartości, nie automatycznie całej doby. Suma jest pośrednią wielkością obliczeniową, dlatego pokazujemy ją bez jednostki i nie przedstawiamy jako osobnej temperatury. Nie określamy sprawności czujnika na podstawie trzech pomiarów.

## Zadanie 4. Dane adresowe na podstawie arkusza INF.04

**Pochodzenie:** projektowe `02_zadania_desktopowe.md`, D.2, wskazuje arkusz **INF.04-01-23.06-SG**, czerwiec 2023. Oryginalna część II, strona 3 z 5, zawiera pola „Ulica z numerem”, „Kod pocztowy”, „Miasto”. Nasze ćwiczenie wykorzystuje te pola do szkolnego programu konsolowego. Nie jest pełnym zadaniem egzaminacyjnym: nie tworzy GUI, nie wybiera ceny przesyłki, nie podmienia obrazów i nie sprawdza kodu.

1. Źródło pól: INF.04-01-23.06-SG, czerwiec 2023, część II, aplikacja desktopowa do obsługi poczty.
2. W konsoli pobierz Ulicę z numerem, Kod pocztowy i Miasto jako trzy napisy.
3. Wypisz trzy wiersze z etykietami: Ulica, Kod pocztowy, Miasto. Zachowaj zera w kodzie.
4. Przyjmujemy kod złożony z pięciu cyfr bez myślnika. Kontrolę poprawności i GUI dodamy w późniejszych tematach.

Plik zadanie4.py. Ćwiczenie zbierania danych z pól opisanych w arkuszu.

**Przykład pierwszego uruchomienia:**

Wejście, kolejno po jednym wpisie:

```text
Polna 7
00123
Warszawa
```

Wyjście, bez pytań przy input():

```text
Ulica: Polna 7
Kod pocztowy: 00123
Miasto: Warszawa
```

**Dodatkowe próby:**

Próba 2, kolejne wpisy: `Długa 12A`, `00345`, `Nowy Sącz`.

```text
Ulica: Długa 12A
Kod pocztowy: 00345
Miasto: Nowy Sącz
```

Próba 3, kolejne wpisy: `Łąkowa 1`, `00001`, `Łódź`.

```text
Ulica: Łąkowa 1
Kod pocztowy: 00001
Miasto: Łódź
```

Kod jest pięcioznakowym napisem. Wpisy ulicy i miasta mogą mieć spacje oraz polskie znaki. Nie dodajemy komunikatu „Dane poprawne”, ponieważ program nie przeprowadza sprawdzenia. Oryginalny arkusz przyjmuje pięć cyfr bez myślnika - projektowe opracowanie mniej precyzyjnie opisuje możliwość myślnika. Przy pełnej realizacji zadania kierujemy się oryginałem.

## Zadanie 5 dla chętnych. Dwie pozycje w tabeli

1. Pobierz nazwę, liczbę sztuk i cenę dla pierwszego produktu. Powtórz odczyt dla drugiego.
2. Przyjmujemy nazwy do 12 znaków, sztuki 0-999 i ceny od 0 do 999.99.
3. Wypisz nagłówek Nazwa, Szt, Cena oraz dwa wiersze danych.
4. Nazwa: pole 12 znaków do lewej. Sztuki: pole 3 do prawej. Cena: pole 7 do prawej z .2f. Pola oddziel jedną spacją.

Plik zadanie5.py. Użyj dwóch zestawów zmiennych, np. nazwa1 i nazwa2, bez pętli.

Przykładowe dane: `Zeszyt`, `3`, `7.5`, `Gumka`, `12`, `2`. Wynik:

```text
Nazwa        Szt    Cena
Zeszyt         3    7.50
Gumka         12    2.00
```

Kwoty w tej tabeli oznaczają cenę jednej sztuki. W nagłówku stosujemy same etykiety, bez dopisku zł. Używamy dokładnie jednej spacji **między polami**, oprócz spacji dopełnienia wewnątrz pól. Program przyjmuje podane ograniczenia, nie weryfikuje ich. Próba z nazwami A i B, sztukami 0 i 999 oraz cenami 0 i 999.99 sprawdza szerokość skrajnych wartości. Przy dłuższej nazwie pole się rozszerzy - nie traktujemy formatowania jako kontroli długości.

## Diagnoza i praca domowa

Otwórz [zadanie naprawcze](diagnoza/README.md). Ma własny kontrakt i celowo błędny kod. Wykonaj je na zajęciach lub dokończ w domu zgodnie z ustaleniem prowadzącego.

## Oddanie pracy

Zachowaj źródła i niezbędne pliki danych. W `testy.md` opisz rzeczywiście wykonane próby: dane, oczekiwany wynik, wynik otrzymany i wniosek. Własną instrukcję uruchomienia zapisz w `URUCHOMIENIE.md`, aby zachować treść zadań w tym README. Dołącz dokumentację wskazaną w poleceniu. Zadania oznaczone jako dodatkowe są dla chętnych.

[Spis lekcji](../README.md)
