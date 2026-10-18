# Ćwiczenia: Bezpieczny odczyt i zapis danych w plikach tekstowych z użyciem instrukcji with

**Temat 27 | Lekcje 55-56**

## Przygotowanie

Środowisko i polecenia uruchamiania opisano w [instrukcji głównej](../README.md#uruchamianie). Wystarcza biblioteka standardowa Pythona.

Utwórz pliki wskazane w zadaniach wewnątrz bieżącego folderu lekcji. Kod uruchamiaj w terminalu z tego folderu. Zadania wprowadzają kolejne zmiany; zachowuj wcześniejsze wersje w podfolderach, jeśli wymaga tego polecenie.

## Format danych i pliki

Używaj `with open(...)` oraz UTF-8; liczby zapisuj po jednej w wierszu. Dołączony `liczby.txt` zawiera 4, 7, -2 i pusty wiersz. W zadaniu 3 pięć wierszy rekordu oznacza kolejno: wykonawca, tytuł, liczba utworów, rok, liczba pobrań. Trzy ostatnie pola przekształć na int. Nie usuwaj pustych wierszy z pliku albumów przed kontrolą kompletności. `dane.txt` zawiera dwa kompletne rekordy.

## Zadanie 1. Raport z liczb

- Utwórz liczby.txt z wierszami: 4, 7, -2 oraz jednym pustym wierszem.
- Wczytaj liczby, pomijając puste wiersze. Oblicz sumę i liczbę danych.
- Zapisz raport.txt w UTF-8: „Suma: 9” i „Liczba danych: 3”.

**Wynik kontrolny:** dwa wiersze raportu, suma 9.

## Zadanie 2. Lista komunikatów

- Napisz funkcję dopisz_log(tekst), która dopisuje jeden wiersz do log.txt.
- Wywołaj ją dla „START”, „ZAPIS” i „KONIEC”. Zacznij od pustego pliku.
- Uruchom program drugi raz i sprawdź, że poprzednie wiersze pozostały.

**Wynik kontrolny:** 3 wiersze po pierwszym, 6 po drugim uruchomieniu.

## Zadanie 3. Albumy z pliku

- Utwórz dane.txt: Zespół Północ, Poranek, 8, 2024, 120 w osobnych wierszach.
- Dodaj drugi blok: Anna Nowak, Wieczór, 10, 2023, 80.
- Wczytaj rekordy do obiektów Album z pięcioma polami i wypisz ich dane.
- Jeżeli liczba wierszy nie jest wielokrotnością 5, zgłoś niepełny rekord. Adaptacja INF.04-02-24.06-SG, I: własne dane i kontrola kompletności.

**Wynik kontrolny:** 2 albumy, razem 200 pobrań.

## Zadanie 4. Błędy odczytu

- Rozbuduj zadanie 1: osobno obsłuż brak pliku i nieliczbowy wiersz.
- W komunikacie błędu danych podaj numer wiersza. Zakończ obliczenia.
- Sprawdź: brak pliku, pusty plik oraz plik z wierszami 4, abc, 7.

**Wynik kontrolny:** pusty plik: suma 0, liczba 0. „abc”: błąd wiersza 2.

## Oddanie pracy

Zachowaj źródła i niezbędne pliki danych. W `testy.md` opisz rzeczywiście wykonane próby: dane, oczekiwany wynik, wynik otrzymany i wniosek. Własną instrukcję uruchomienia zapisz w `URUCHOMIENIE.md`, aby zachować treść zadań w tym README. Dołącz dokumentację wskazaną w poleceniu. Zadania oznaczone jako dodatkowe są dla chętnych.

[Spis lekcji](../README.md)
