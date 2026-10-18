# Ćwiczenia: Własne komunikaty błędów oraz sprawdzanie poprawności danych wprowadzanych do obiektów

**Temat 22 | Lekcje 43-44**

## Przygotowanie

Środowisko i polecenia uruchamiania opisano w [instrukcji głównej](../README.md#uruchamianie). Wystarcza biblioteka standardowa Pythona.

Utwórz pliki wskazane w zadaniach wewnątrz bieżącego folderu lekcji. Kod uruchamiaj w terminalu z tego folderu. Zadania wprowadzają kolejne zmiany; zachowuj wcześniejsze wersje w podfolderach, jeśli wymaga tego polecenie.

## Zadanie 1. Walidator oceny

**Plik:** `zadanie1.py`.

1. Zdefiniuj `OcenaError(ValueError)`.
2. Napisz `sprawdz_ocene(ocena)`: wymagaj dokładnie `int` i zakresu 1-6 włącznie. Zły typ: `TypeError("Ocena musi być typu int.")`; zły zakres: `OcenaError("Zakres: 1-6.")`.
3. Funkcja zwraca poprawną ocenę; nie wykonuje `input()` ani `print()`.
4. W programie głównym pobieraj ocenę przez `int(input())`. Po błędnym zapisie: `Podaj liczbę całkowitą.`. Po złym zakresie wyświetl komunikat wyjątku. Ponawiaj pytanie, aż przyjmiesz ocenę; potem wyświetl `Ocena:` i wartość.
5. Umieść szczegółowy `except OcenaError` przed `except ValueError`. `TypeError` obsługuj osobno. Zły typ sprawdź dodatkowym bezpośrednim wywołaniem funkcji, bez konwersji.

Próby: `1` i `6` - sukces; `0` i `7` - błąd zakresu; `abc`, pusty tekst, `3.5` w konsoli - błąd konwersji. `sprawdz_ocene(3.5)`, `sprawdz_ocene("3")` i `sprawdz_ocene(True)` - `TypeError`.

## Zadanie 2. Uczeń z walidowaną właściwością

**Plik:** `zadanie2.py`.

1. Umieść w pliku klasę `OcenaError` i walidator z zadania 1.
2. Napisz `Uczen(imie, ocena)`. Imię ma być dokładnie `str`; po `strip()` nie może być puste. Zły typ: `TypeError("Imię musi być napisem.")`; puste imię: `ValueError("Imię nie może być puste.")`.
3. W konstruktorze sprawdź obie wartości przed ich zapisaniem. Przechowuj imię po usunięciu spacji z początku i końca. Ustaw ocenę przez właściwość `ocena`.
4. Getter zwraca `_ocena`. Setter korzysta z `sprawdz_ocene(nowa_ocena)` przed przypisaniem do `_ocena`.
5. Utwórz ucznia z `"  Ala  "` i oceną 4, zmień ocenę na 6, a potem spróbuj ustawić 7. Obsłuż wyjątek w programie głównym i pokaż, że ocena nadal wynosi 6.
6. Osobno sprawdź nieudane konstrukcje z pustym imieniem i oceną 0; nie korzystaj z wyniku nieudanej próby.

## Zadanie 3. Magazyn i odrzucona operacja

**Plik:** `zadanie3.py`.

1. Utwórz `BrakTowaruError(Exception)` i klasę `Magazyn(stan)`.
2. Stan początkowy ma być dokładnie `int` i nieujemny. Zły typ: `TypeError("Wymagany typ int.")`; ujemny stan: `ValueError("Stan nie może być ujemny.")`.
3. Właściwość `stan` ma tylko getter zwracający `_stan`.
4. Metoda `pobierz(sztuki)` wymaga dokładnie `int`, wartości większej od 0 oraz nie większej od aktualnego stanu. Komunikaty: `Wymagany typ int.`, `Ilość musi być dodatnia.`, `Za mało towaru.`. Ostatni komunikat ma pochodzić z `BrakTowaruError`.
5. Zmniejsz `_stan` dopiero po wszystkich sprawdzeniach. Metoda nie wykonuje wejścia ani wyjścia.
6. Zacznij od stanu 5 i wykonaj kolejno pobrania 2, 4, 0, 3, 1. Obsłuż każdą próbę oddzielnie; po niej wyświetl stan.

| Pobranie w sekwencji | Oczekiwany stan i ewentualny komunikat |
| --- | --- |
| 2 | `Stan: 3` |
| 4 | `Za mało towaru.`, następnie `Stan: 3` |
| 0 | `Ilość musi być dodatnia.`, następnie `Stan: 3` |
| 3 | `Stan: 0` |
| 1 | `Za mało towaru.`, następnie `Stan: 0` |

## Zadanie 4. Format PESEL w obiekcie i funkcje z arkusza

**Plik:** `zadanie4.py` • **Źródło:** INF.04-01-24.01-SG, część I, **adaptacja**.

1. Zdefiniuj `PeselFormatError(ValueError)` i walidator `sprawdz_format(pesel)`. Wymagaj dokładnie `str`, długości 11 i znaków ASCII od `"0"` do `"9"`.
2. Zły typ: `TypeError("PESEL musi być napisem.")`. Zła długość: `PeselFormatError("PESEL musi mieć 11 znaków.")`. Błędny znak: `PeselFormatError("PESEL musi zawierać cyfry 0-9.")`. Najpierw sprawdzaj typ, potem długość, potem znaki. Nie normalizuj numeru przez `strip()` ani konwersję całości do liczby.
3. W `NumerPesel(pesel)` sprawdź format przed zapisaniem `_wartosc`. Getter `wartosc` udostępnia napis tylko do odczytu; nie definiuj settera.
4. Zachowaj osobną funkcję `plec(pesel)`, która zwraca `K` dla parzystej cyfry o indeksie 9 i `M` dla nieparzystej. Zachowaj `sprawdz_sume(pesel)`, zwracającą `True` albo `False`.
5. W obu funkcjach wywołaj walidator, aby mogły bezpiecznie działać również poza klasą. Nie używaj w nich `input()` ani `print()`.
6. W programie głównym pobieraj tekst; dokładnie małe `q` kończy pętlę. Po błędnym formacie wyświetl komunikat i ponów pytanie. Dla przyjętego obiektu użyj obu funkcji: wyświetl pełne słowo `Kobieta`/`Mężczyzna` oraz `Suma kontrolna: zgodna.` lub `Suma kontrolna: niezgodna.`.
7. W `testy.md` zapisz co najmniej trzy próby: dane, oczekiwany i rzeczywisty wynik; uwzględnij błąd formatu oraz niezgodną sumę po poprawnym formacie.

Algorytm sumy: wagi `[1, 3, 7, 9, 1, 3, 7, 9, 1, 3]`; `S` jest sumą dziesięciu iloczynów. Oblicz `M = S % 10`. Jeśli `M == 0`, `R = 0`; inaczej `R = 10 - M`. Porównaj `R` z ostatnią cyfrą. Pętlę i warunki zapisujemy jawnie, bez skrótu przez comprehension lub alternatywnego wzoru.

| Dane | Oczekiwana reakcja |
| --- | --- |
| `"123"` | Błąd długości. |
| `"0000000000a"` | Błąd znaku. |
| `"0000000000 "` | Błąd znaku; spacji nie usuwamy. |
| `"٠٠٠٠٠٠٠٠٠٠٠"` | Błąd znaków: cyfry spoza ASCII. |
| `"00000000000"` | `K`, zgodna suma; napis zachowuje wszystkie zera. |
| `"00000000001"` | `K`, niezgodna suma; normalny wynik `False`. |
| `"00000000017"` | `M`, zgodna suma. |
| `123` przekazane bezpośrednio do klasy | `TypeError`: wymagany napis. |

## Zadanie 5. Dla chętnych: Wartość w obiekcie wyjątku - dodatkowe

**Plik:** `zadanie5.py`.

Rozbuduj `OcenaError`, aby jego konstruktor przyjmował odrzuconą wartość, zapisywał `wartosc` i ustawiał czytelny komunikat przez `super().__init__()`. Zgłoś `OcenaError(7)`, przechwyć go przez `as blad`, wyświetl komunikat i `blad.wartosc`. To pokaz danych w wyjątku; nie trzeba przepisywać wszystkich poprzednich zadań.

## Oddanie pracy

Zachowaj źródła i niezbędne pliki danych. W `testy.md` opisz rzeczywiście wykonane próby: dane, oczekiwany wynik, wynik otrzymany i wniosek. Własną instrukcję uruchomienia zapisz w `URUCHOMIENIE.md`, aby zachować treść zadań w tym README. Dołącz dokumentację wskazaną w poleceniu. Zadania oznaczone jako dodatkowe są dla chętnych.

[Spis lekcji](../README.md)
