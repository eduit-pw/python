# Ćwiczenia: Praca ze słownikami: tworzenie powiązań klucz-wartość i przeglądanie danych

**Temat 10 | Lekcje 19-20**

## Przygotowanie

Środowisko i polecenia uruchamiania opisano w [instrukcji głównej](../README.md#uruchamianie). Wystarcza biblioteka standardowa Pythona.

Utwórz pliki wskazane w zadaniach wewnątrz bieżącego folderu lekcji. Kod uruchamiaj w terminalu z tego folderu. Zadania wprowadzają kolejne zmiany; zachowuj wcześniejsze wersje w podfolderach, jeśli wymaga tego polecenie.

## Zadanie 1. Konfiguracja serwera

To zadanie szkolne, nie wskazane zadanie z arkusza CKE. Porty i nazwa serwera są przykładowymi wartościami danych; program nie nawiązuje połączenia sieciowego.

1. Napisz przygotuj_konfiguracje(), bez parametrów i bez input/print. Wewnątrz utwórz słownik: host = "127.0.0.1", port = 8080, ssl_enabled = False, timeout = 30, server_name = "Apache-Test".
2. Odczytaj konfiguracja.get("max_connections", 100).
3. Za pomocą update ustaw port = 443, ssl_enabled = True oraz server_name = "Nginx-Production".
4. Usuń timeout przez pop i zachowaj usuniętą wartość.
5. Zwróć krotkę (konfiguracja, max_polaczen, usuniety_timeout). W programie głównym wypisz słownik, obie dodatkowe wartości i sprawdź obecność max_connections.

| Sprawdzenie | Oczekiwany wynik |
|---|---|
| port, ssl_enabled, server_name | 443, True, Nginx-Production |
| host | 127.0.0.1 |
| max_polaczen | 100 |
| usuniety_timeout | 30 |
| "timeout" in konfiguracja | False |
| "max_connections" in konfiguracja | False |
| len(konfiguracja) | 4 |

Uruchom funkcję dwukrotnie: za każdym razem ma tworzyć nowy słownik i zwracać takie same wartości. Nie wprowadzamy tu try/except ani type hints.

## Zadanie 2. Licznik słów

Napisz zlicz_slowa(tekst), która zwraca dict z liczbami wystąpień słów. Przejdź pętlą po tekst.lower().split(). Z obu końców każdego fragmentu usuń znaki przez strip(".,!?;:"). Pomiń pusty rezultat. Użyj if do utworzenia licznika i zwiększaj go przy każdym wystąpieniu. Funkcja nie pobiera danych i niczego nie wypisuje. W programie głównym wypisz klucze alfabetycznie z licznikami.

| Tekst | Oczekiwany słownik |
|---|---|
| Python, python! i SQL; SQL. | {'python': 2, 'i': 1, 'sql': 2} |
| pusty tekst lub same odstępy | {} |
| ... !!! | {} |
| Kot kot KOT | {'kot': 3} |
| a-b a-b | {'a-b': 2} |

To celowo uproszczona definicja słowa: split dzieli po białych znakach, strip usuwa wskazane znaki tylko z końców, nie z wnętrza. Nie wymagamy regex ani pełnego przetwarzania języka naturalnego. Funkcja lower zwraca nowy tekst i nie zmienia oryginalnego argumentu.

## Zadanie 3. Magazyn

Ceny są umownymi liczbami całkowitymi. To zadanie szkolne, nie kopia konkretnego arkusza. Nie liczymy VAT ani procentów; skupiamy się na rekordach i agregacji.

```python
magazyn = {
    "A01": {"nazwa": "zeszyt", "ilosc": 4, "cena": 7},
    "B02": {"nazwa": "dlugopis", "ilosc": 8, "cena": 3},
    "C03": {"nazwa": "gumka", "ilosc": 2, "cena": 2}
}
```

1. Napisz zwieksz_stan(magazyn, kod, dodana_ilosc). Dla znanego kodu i dodatniej ilości zwiększ stan w oryginalnym magazynie i zwróć True. W przeciwnym razie zwróć False bez zmian.
2. Napisz wartosc_magazynu(magazyn), która zwraca sumę ilosc × cena dla wszystkich rekordów. Nie zmieniaj magazynu.
3. Napisz niski_stan(magazyn, prog), która zwraca **nowy** dict {kod: ilosc} dla ilości mniejszych lub równych progowi. Użyj pętli i if, nie comprehension. Nie zmieniaj magazynu.
4. W programie głównym pokaż wartość przed dostawą, dodaj 3 sztuki A01, pokaż rekordy uporządkowane według kodu, wartość po dostawie oraz niski stan z progiem 4.

Przyjmujemy kompletny schemat rekordów: pola nazwa, ilosc, cena. Ilości, ceny i próg są liczbami całkowitymi, początkowe ilości i ceny nieujemne. Nie wymagamy walidacji typów lub brakujących pól. Żadna funkcja nie wykonuje input/print.

| Przypadek | Oczekiwany wynik |
|---|---|
| Wartość danych początkowych | 56 |
| Niski stan początkowo, próg 4 | {'A01': 4, 'C03': 2} |
| Dostawa A01, +3 | True; stan 7 |
| Wartość po tej dostawie | 77 |
| Niski stan po dostawie, próg 4 | {'C03': 2} |
| Dostawa nieznanego X99 | False, żadnej zmiany |
| Dostawa A01, 0 lub -1 | False, żadnej zmiany |
| Pusty magazyn | wartość 0; niski stan {}; dostawa False |

Nie filtrujemy według nazwy jako klucza: dwa produkty mogą mieć taką samą nazwę. Kod zachowuje ich odrębność. Zmiana słownika wynikowego niski_stan nie może zmienić ilości w magazynie.

## Zadanie 4. Punkty za kości - fragment INF.04-01-24.06-SG

**Zakres adaptacji:** wyniki są podane w liście, liczniki tworzymy w dict. Nie losujemy ani nie powtarzamy gry; te etapy wymagają zagadnień ćwiczonych później. Dodajemy pomocniczą kontrolę listy. To ćwiczenie algorytmu, nie pełny próbny egzamin. Punktacja jest szkolna.

1. Napisz zlicz_oczka(oczka): nowy dict {wartosc: liczba_wystapien}. Zainicjalizuj licznik dla nowego klucza i zwiększaj go w pętli.
2. Napisz licz_punkty(oczka). Pobierz liczniki, przejdź po parach przez items i dodawaj wartosc × liczba_wystapien tylko dla licznika co najmniej 2. Zwróć int.
3. Napisz poprawny_rzut(oczka): True dla listy od 3 do 10 elementów, każdy od 1 do 6; inaczej False. Przyjmujemy, że elementy są liczbami całkowitymi. To szkolna kontrola podanych wyników.
4. Program główny pracuje na liście oczka. Dla błędnych danych wypisuje komunikat i pomija obliczenia. Dla poprawnych wypisuje kolejne kości, liczniki i wynik. Numer kości zaczyna się od 1 i rośnie w pętli.
5. Funkcje zliczania i punktacji nie zmieniają wejścia, niczego nie wypisują i nie używają zmiennych globalnych. Dodaj nagłówek komentarza funkcji licz_punkty i dokumentację.

| Dane | Wynik punktacji |
|---|---:|
| [1, 5, 2, 2, 5] | 14 |
| [2, 1, 2, 3, 2] | 6 |
| [3, 3, 5, 5, 1] | 16 |
| [1, 2, 3, 4, 5] | 0 |
| [6, 6, 6, 6, 6] | 30 |
| [2, 2, 2] | 6 |
| Dziesięć szóstek | 60 |

Odrzuć w programie głównym dwie kości, jedenaście kości, [0, 2, 2] i [7, 2, 2]. Liczba kości 3 oraz 10 to granice poprawnego przypadku. Funkcje zliczania i punktacji można dodatkowo testować dla [], uzyskując {} i 0; sam pusty rzut **nie jest poprawnym przypadkiem gry**. Te funkcje mają szerszy zakres długości wejścia niż program główny. Ich warunek wejściowy: wszystkie elementy są całkowitymi wartościami od 1 do 6.

Punkty liczymy za **wszystkie** powtórzenia, nie tylko parę: [2, 2, 2] daje 6, nie 4. Pojedyncza szóstka nie punktuje. Słownik liczników jest naszym sposobem implementacji; oryginał nie narzuca jego użycia.

## Zadanie 5. Dla chętnych: Grupowanie uczniów - autorskie, dodatkowe

Dane: [("Ala", "2A"), ("Jan", "2B"), ("Ola", "2A")]. Napisz grupuj_uczniow(uczniowie), która zwraca nowy słownik. Kluczem jest klasa, wartością lista imion w kolejności wejścia. Dla nowej klasy utwórz osobną listę, potem dopisz imię. Zachowuj powtórzone rekordy. Funkcja nie zmienia wejścia ani niczego nie wypisuje. Program główny pokazuje grupy według klasy.

| Wejście | Wynik |
|---|---|
| Dane podstawowe | {'2A': ['Ala', 'Ola'], '2B': ['Jan']} |
| [] | {} |
| [('Ala', '2A'), ('Ala', '2A')] | {'2A': ['Ala', 'Ala']} |

Każda klasa ma własną listę. To rozszerzenie pokazujące inny rodzaj agregacji niż zliczanie.

## Oddanie pracy

Zachowaj źródła i niezbędne pliki danych. W `testy.md` opisz rzeczywiście wykonane próby: dane, oczekiwany wynik, wynik otrzymany i wniosek. Własną instrukcję uruchomienia zapisz w `URUCHOMIENIE.md`, aby zachować treść zadań w tym README. Dołącz dokumentację wskazaną w poleceniu. Zadania oznaczone jako dodatkowe są dla chętnych.

[Spis lekcji](../README.md)
