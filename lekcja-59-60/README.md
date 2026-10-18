# Ćwiczenia: Przetwarzanie ustrukturyzowanych danych tekstowych: pliki CSV oraz format JSON

**Temat 29 | Lekcje 59-60**

## Przygotowanie

Środowisko i polecenia uruchamiania opisano w [instrukcji głównej](../README.md#uruchamianie). Wystarcza biblioteka standardowa Pythona.

Utwórz pliki wskazane w zadaniach wewnątrz bieżącego folderu lekcji. Kod uruchamiaj w terminalu z tego folderu. Zadania wprowadzają kolejne zmiany; zachowuj wcześniejsze wersje w podfolderach, jeśli wymaga tego polecenie.

## Dane i reguły walidacji

Plik `magazyn.csv` jest dołączony. Zawiera nagłówek i trzy rekordy; średnik wewnątrz nazwy pióra jest ujęty w cudzysłowy. Używaj modułu `csv`, separatora `;`, UTF-8 oraz `newline=""`.

JSON ma zawierać listę słowników z polami `nazwa` (niepusty str po `strip()`) i `ilosc` (dokładnie int >= 0, bez bool). Pusta lista jest poprawna. Waliduj typ całej struktury, każdego rekordu i wymaganych pól. Nie zamieniaj automatycznie tekstu `"2"` na liczbę w walidatorze JSON.

## Zadanie 1. Suma ilości w CSV

- Otwórz dołączony `magazyn.csv`: nagłówek i trzy rekordy.
- Wczytaj rekordy przez DictReader z separatorem „;”.
- Zamień ilosc na int i oblicz sumę. Zachowaj pełną nazwę pióra.

**Wynik kontrolny:** 3 rekordy, suma 6.

## Zadanie 2. CSV do JSON

- Wczytaj magazyn.csv z zadania 1 i zbuduj listę słowników.
- Zapisz magazyn.json w UTF-8, z wcięciami i ilością typu int.
- Wczytaj JSON ponownie i sprawdź zgodność danych.

**Wynik kontrolny:** ilość pióra to liczba 1. Suma nadal wynosi 6.

## Zadanie 3. Raport braków

- Utwórz CSV z nagłówkiem nazwa;ilosc i rekordami: Ołówek;0, Zeszyt;2, Gumka;0.
- Zapisz braki.csv: ten sam nagłówek, tylko produkty o ilości równej 0.
- Użyj DictWriter. Zachowaj kolejność rekordów.

**Wynik kontrolny:** Ołówek;0 i Gumka;0.

## Zadanie 4. Walidacja JSON

- Napisz funkcję sprawdzającą listę produktów według umowy opisanej w przygotowaniu.
- Sprawdź puste [], brak ilosc, ilosc=-1, ilosc="2" oraz ilosc=true.
- Wykryj także składnię z przecinkiem po ostatnim polu JSON.

**Wynik kontrolny:** [] jest poprawne. Każdy z pozostałych przypadków zgłasza błąd.

## Oddanie pracy

Zachowaj źródła i niezbędne pliki danych. W `testy.md` opisz rzeczywiście wykonane próby: dane, oczekiwany wynik, wynik otrzymany i wniosek. Własną instrukcję uruchomienia zapisz w `URUCHOMIENIE.md`, aby zachować treść zadań w tym README. Dołącz dokumentację wskazaną w poleceniu. Zadania oznaczone jako dodatkowe są dla chętnych.

[Spis lekcji](../README.md)
