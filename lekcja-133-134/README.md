# Ćwiczenia: Odczytywanie i wyciąganie wybranych informacji ze stron internetowych za pomocą biblioteki BeautifulSoup4

**Temat 64 | Lekcje 133-134**

## Przygotowanie

Środowisko i polecenia uruchamiania opisano w [instrukcji głównej](../README.md#uruchamianie). Przed pracą zainstaluj zależności z dołączonego `requirements.txt` w wybranym środowisku: `py -m pip install -r requirements.txt`.

Utwórz pliki wskazane w zadaniach wewnątrz bieżącego folderu lekcji. Kod uruchamiaj w terminalu z tego folderu. Zadania wprowadzają kolejne zmiany; zachowuj wcześniejsze wersje w podfolderach, jeśli wymaga tego polecenie.

## Plik źródłowy i reguły parsera

Dołączony `albumy.html` jest lokalnym źródłem, nie trzeba pobierać zewnętrznej strony. W main.py wczytaj UTF-8, zbuduj BeautifulSoup z parserem html.parser. Karty wybierz selektorem article.album. ID jest w data-id, tytuł w h2, liczba pobrań w p.pobrania. Przed odczytem tekstu sprawdź istnienie węzła, a pola liczbowe konwertuj na int. Początkowo wymagaj wszystkich pól; brak tytułu albo błędna liczba daje komunikat i pominięcie karty. Dopiero zadanie 3 zmienia regułę brakujących pobrań na 0. Każdą próbę błędu wykonuj na osobnej kopii oryginalnego HTML.

## Zadanie 1. Dwa rekordy

- Otwórz dołączony albumy.html i wybierz article.album.
- Odczytaj ID, tytuł i pobrania. Oblicz sumę.

**Wynik kontrolny:** 2 rekordy i suma 200.

## Zadanie 2. Eksport CSV

- Zapisz odczytane dane do albumy.csv przez csv.DictWriter, separator ;.
- Kolumny: id, tytul, pobrania. Użyj UTF-8 i newline="".
- Wczytaj zapisany plik ponownie i sprawdź wiersze.

**Wynik kontrolny:** nagłówek i dwa rekordy z poprawnym tekstem Wieczór.

## Zadanie 3. Brak pola

- W kopii HTML usuń p.pobrania z drugiego albumu.
- Ustal w tym ćwiczeniu: brak pola pobrania oznacza 0. Sprawdź None przed get_text.
- Pozostaw zasadę, że brak h2 oznacza błąd i pominięcie karty.

**Wynik kontrolny:** 2 rekordy, suma 120. Brak tytułu pomija odpowiednią kartę.

## Zadanie 4. Niepoprawna liczba i zmiana klasy

- Zmień 80 na tekst osiemdziesiąt i odnotuj błąd konwersji rekordu.
- W osobnej próbie zmień klasę jednej karty na rekord. Sprawdź liczbę dopasowań.
- Zapisz, jak wykryjesz zmianę źródłowego HTML w regularnym imporcie.

**Wynik kontrolny:** wykryty błąd liczby oraz tylko 1 karta dla article.album.

## Oddanie pracy

Zachowaj źródła i niezbędne pliki danych. W `testy.md` opisz rzeczywiście wykonane próby: dane, oczekiwany wynik, wynik otrzymany i wniosek. Własną instrukcję uruchomienia zapisz w `URUCHOMIENIE.md`, aby zachować treść zadań w tym README. Dołącz dokumentację wskazaną w poleceniu. Zadania oznaczone jako dodatkowe są dla chętnych.

[Spis lekcji](../README.md)
