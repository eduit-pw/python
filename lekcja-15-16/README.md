# Ćwiczenia: Praca z listami: dodawanie, usuwanie, modyfikowanie i przeszukiwanie elementów

**Temat 8 | Lekcje 15-16**

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

**Podczas pracy:** korzystaj z [tabel składni i krótkich wzorców](SCIAGA.md). W [starterach](startery/README.md) znajdziesz punkty wyjścia. Pełne polecenia i nazwy docelowych plików są poniżej.

## Zadanie 1. Lista adresów serwerów

Wszystkie adresy są tekstami do ćwiczenia list. 192.168.1.53 oznacza umowny lokalny serwer DNS, nie automatycznie bramę lub rzeczywiście dostępny serwer. Nie zmieniamy konfiguracji komputera.

Dane: serwery = ["8.8.8.8", "1.1.1.1", "9.9.9.9"].

1. Zachowaj listę przed zmianami przez copy. Dodaj na koniec "8.8.4.4" metodą append.
2. Wstaw "192.168.1.53" na pozycję 0 metodą insert.
3. Jeśli istnieje "1.1.1.1", znajdź pierwszy indeks i podmień tę pozycję na "1.0.0.1".
4. Jeśli istnieje "9.9.9.9", usuń pierwsze wystąpienie metodą remove.
5. Z niepustej listy zdejmij ostatni adres przez pop i zachowaj go w zmiennej zapasowy. Gdy lista jest pusta, zapasowy ma być None.
6. Pokaż listę końcową, zdjęty adres, długość i kopię listy początkowej. To rozgrzewka w programie głównym, bez narzucania funkcji łączącej wszystkie działania.

| Wynik | Oczekiwana wartość |
|---|---|
| Lista końcowa | ['192.168.1.53', '8.8.8.8', '1.0.0.1'] |
| Zdjęty adres | '8.8.4.4' |
| Długość | 3 |
| Kopia początkowa | ['8.8.8.8', '1.1.1.1', '9.9.9.9'] |

Osobno sprawdź remove/index przy braku adresu oraz pop dla pustej listy. Nie wypisuj komunikatu „PRAWIDŁOWA (CKE)”: ćwiczenie nie waliduje rzeczywistej konfiguracji DNS.

## Zadanie 2. Dodatnie pomiary

Dane: pomiary = [18, 0, -2, 25, 0, 31, 18]. Przyjmujemy listę liczb całkowitych.

1. Napisz wybierz_dodatnie(pomiary). Pętlą zbuduj nową listę wartości > 0, zachowując kolejność i powtórzenia. Nie zmieniaj wejścia.
2. Napisz srednia(liczby). Oblicz sumę jawną pętlą, podziel przez długość. Dla [] zwróć None, w pozostałych przypadkach liczbę float.
3. Funkcje zwracają wyniki, bez input/print. Program główny pokazuje filtr, wersję malejącą przez sorted(..., reverse=True), średnią do dwóch miejsc lub komunikat braku danych.
4. Pokaż, że lista źródłowa pozostała niezmieniona. Nie używaj comprehension ani usuwania w pętli po tej samej liście.

| Próba | Wynik |
|---|---|
| Filtr danych podstawowych | [18, 25, 31, 18] |
| Wersja malejąca | [31, 25, 18, 18] |
| Średnia filtru | 23.0, wydruk 23.00 |
| Pomiary [] lub [0, -2, 0] | Filtr [], średnia None, komunikat braku danych |
| Pomiary [5] | Filtr [5], średnia 5.0 |
| Pomiary [2, 2] | Filtr [2, 2], średnia 2.0 |

## Zadanie 3. Dostawa i wycofywanie towarów

Upraszczamy rekord do [kod, nazwa, ilosc] i pomijamy ceny. Kod i nazwa są tekstami, ilość liczbą całkowitą. Kody w bazie są unikalne i porównujemy je dokładnie. Ilości <= 0 oznaczają pozycje do wycofania.

Dane:

```python
magazyn = [
    ["RAM", "Pamięć", 5],
    ["CPU", "Procesor", 0],
    ["SSD", "Dysk", -1],
    ["GPU", "Karta graficzna", 4]
]
```

1. Napisz znajdz_towar(baza, kod): pętla for po range(len(baza)), wynik pierwszy indeks albo -1.
2. Napisz dostawa_towaru(baza, kod, dodana_ilosc). Dla dodatniej ilości i istniejącego kodu zwiększ baza[indeks][2] i zwróć True. W przeciwnym razie False, bez zmiany bazy.
3. Napisz wycofaj_wyprzedane(baza). Usuń w miejscu wszystkie rekordy z ilosc <= 0 i zwróć liczbę usuniętych. Zastosuj while z kontrolowanym indeksem oraz pop(i). Zachowaj względną kolejność pozostałych.
4. Funkcje nie wypisują. Dostawa i wycofanie celowo modyfikują argument. Po pop nie zwiększaj i, aby sprawdzić element, który zajął zwolnioną pozycję.
5. Program główny wykonuje dostawę RAM +3, próbę BRAK +2 i RAM +0, potem wycofanie i raport pozostałych rekordów.

| Próba | Wynik i zmiana |
|---|---|
| RAM +3 | True, ilość RAM rośnie z 5 do 8 |
| BRAK +2 | False, baza bez zmian |
| RAM +0 lub RAM -2 | False, baza bez zmian |
| Wycofanie po dostawie | 2, usunięto sąsiednie CPU i SSD |
| Pozostałe rekordy | [['RAM', 'Pamięć', 8], ['GPU', 'Karta graficzna', 4]] |
| Wycofanie pustej bazy | 0, nadal [] |
| Baza samych ilości <= 0 | Usunięto wszystkie, wynik równy długości początkowej |
| Baza samych dodatnich ilości | 0, zawartość bez zmian |

Testuj wyszukiwanie towaru na pierwszej i ostatniej pozycji oraz nieobecnego kodu. Wskazówka: -1 jest poprawnym indeksem Pythona oznaczającym ostatni element, dlatego wynik wyszukiwania sprawdzamy przed aktualizacją.

## Zadanie 4. Przeszukiwanie z wartownikiem - adaptacja INF.04-01-22.06-SG

Projektowe 01_zadania_konsolowe.md, § 1.2, wskazuje ten algorytm. Treść i komentarz sprawdzono w oryginalnym arkuszu oraz zasadach oceniania. Oryginał wymaga co najmniej 50 pseudolosowych liczb z zakresu 1-100. Na tej lekcji zastępujemy losowanie pięciokrotnym dołączeniem bloku:

```python
fragment = [12, 7, 18, 7, 25, 40, 3, 16, 9, 2]
```

1. Napisz przygotuj_dane(): utwórz pustą listę i w pętli wykonaj pięć razy extend(fragment). Zwróć nową listę 50 liczb. Fragment ma być lokalny w funkcji.
2. Napisz szukaj_z_wartownikiem(liczby, szukana). Przyjmujemy listę int i szukaną int. Utwórz kopię bufor, a następnie append(szukana). Ostatni element to wartownik.
3. Rozpocznij od i = 0. W while sprawdzaj tylko bufor[i] != szukana i zwiększaj i. Nie stosuj in, index ani dodatkowego testu i < len(...) w warunku tej pętli.
4. Zwróć i. Dla trafienia w danych będzie mniejsze niż len(liczby). Dla samego wartownika będzie równe len(liczby). To kontrakt tego zadania, odmienny od -1 w znajdz_indeks.
5. Program główny pobiera szukaną przez int(input(...)), uruchamia funkcję i wyświetla oryginalne liczby oddzielone przecinkami. Dla i < len(liczby) pokazuje pierwszy indeks, inaczej komunikat braku.
6. Funkcja wyszukująca nie zmienia wejścia, nie wypisuje, nie korzysta ze zmiennych globalnych. Dodaj komentarz i dokumentację uruchomienia.

| Dane / szukana | Wynik funkcji | Interpretacja |
|---|---:|---|
| Lista 50, szukana 12 | 0 | Pierwszy element |
| Lista 50, szukana 7 | 1 | Pierwsze z powtórzonych trafień |
| Lista 50, szukana 2 | 9 | Pierwsza dwójka, nie kolejna z powtórzeń bloku |
| Lista 50, szukana 99 | 50 | Trafienie w wartownika, brak w danych |
| [12, 7, 18], szukana 18 | 2 | Ostatni rzeczywisty element |
| [12, 7, 18], szukana 99 | 3 | Wartownik |
| [], szukana 5 | 0 | Wartownik, bez IndexError |
| [4], szukana 4 / 7 | 0 / 1 | Trafienie / wartownik |

W Pythonie indeksy zaczynają się od 0: dla n elementów rzeczywiste indeksy to 0..n-1, a dołączony wartownik ma indeks n. Nie przepisujemy dosłownie n+1 z opisu numerowania w ramce arkusza. Dane wypisujemy bez kopii z wartownikiem.

Po temacie 12 wymień tylko funkcję przygotowania danych na rzeczywiste pseudolosowanie. Pseudolosowość i część mobilna nie są realizowane w tej wersji. Nie przypisujemy ćwiczeniu spełnienia pełnych kryteriów egzaminu. Kopia i próba pustej listy są dodatkami szkolnymi.

## Zadanie 5. Dla chętnych: Mała kolejka zgłoszeń - adaptacja szkolna, dodatkowe

Zastępujemy słowniki tekstami i odkładamy sortowanie priorytetowe oraz identyfikatory. Dane: kolejka = ["Drukarka", "Sieć", "Mysz"], archiwum = [].

1. Dopisz "Monitor" na koniec kolejki.
2. Napisz obsluz_zgloszenie(kolejka, archiwum): dla pustej kolejki zwróć None. W przeciwnym razie zdejmij pop(0), dopisz do archiwum i zwróć tekst zgłoszenia.
3. Obie listy celowo się zmieniają. Funkcja nie wypisuje. Kolejka i archiwum mają być odrębnymi listami.
4. Obsłuż dwa zgłoszenia. Oczekujemy kolejki ['Mysz', 'Monitor'] i archiwum ['Drukarka', 'Sieć']. Dla pustej kolejki archiwum pozostaje bez zmian.

To małe ćwiczenie FIFO na listach. Nie nazywamy go pełną symulacją CKE. Dla dużych kolejek warto poznać deque później, bez benchmarku i deklarowania stałych czasów w milisekundach.

## Diagnoza i praca domowa

Otwórz [zadanie naprawcze](diagnoza/README.md). Ma własny kontrakt i celowo błędny kod. Wykonaj je na zajęciach lub dokończ w domu zgodnie z ustaleniem prowadzącego.

## Oddanie pracy

Zachowaj źródła i niezbędne pliki danych. W `testy.md` opisz rzeczywiście wykonane próby: dane, oczekiwany wynik, wynik otrzymany i wniosek. Własną instrukcję uruchomienia zapisz w `URUCHOMIENIE.md`, aby zachować treść zadań w tym README. Dołącz dokumentację wskazaną w poleceniu. Zadania oznaczone jako dodatkowe są dla chętnych.

[Spis lekcji](../README.md)
