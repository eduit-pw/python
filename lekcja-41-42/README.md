# Ćwiczenia: Zabezpieczanie programu przed awariami: obsługa błędów i wyjątków (try, except, finally)

**Temat 21 | Lekcje 41-42**

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

## Zadanie 1. Pobieranie wieku

**Plik:** `zadanie1.py`.

1. Pobieraj wiek do momentu otrzymania liczby całkowitej z zakresu 0-120 włącznie.
2. `ValueError` przy `int()` obsłuż komunikatem `Podaj liczbę całkowitą.` i ponów pytanie.
3. Wartość poza zakresem obsłuż osobnym `if`: `Zakres: 0-120.` i ponów pytanie.
4. Po sukcesie wyświetl `Wiek:` i wartość, a następnie zakończ pętlę.

Próby: `abc`, `3.5`, pusty wpis - błędny zapis; `-1`, `121` - zły zakres; `0`, `120` - przyjmowane granice. Sekwencja `abc → -1 → 121 → 18` daje trzy komunikaty błędu i końcowe `Wiek: 18`.

## Zadanie 2. Dzielenie z zakończeniem każdej próby

**Plik:** `zadanie2.py`.

1. Pobierz pierwszy tekst. Dokładnie małe `q` kończy program przed rozpoczęciem próby, bez drugiego pytania i bez komunikatu z `finally`.
2. W pozostałych przypadkach pobierz drugi tekst. Dopiero po pobraniu obu tekstów rozpocznij `try` i zamień je na liczby przez `int()`.
3. Podziel pierwszą liczbę przez drugą. Po sukcesie w `else` wyświetl `Wynik:` z dwoma miejscami po kropce.
4. Konwersję obsłuż przez `ValueError`: `Podaj liczby całkowite.`. Dzielenie przez zero obsłuż przez `ZeroDivisionError`: `Nie dziel przez 0.`.
5. W `finally` wyświetl `Koniec próby.`. Po każdej rozpoczętej próbie wróć do pytania o pierwszy tekst, niezależnie od wyniku.

| Wejście jednej próby | Wynik bez tekstów pytań |
| --- | --- |
| `8`, `2` | `Wynik: 4.00`, następnie `Koniec próby.` |
| `abc`, `2` | `Podaj liczby całkowite.`, następnie `Koniec próby.` |
| `8`, `0` | `Nie dziel przez 0.`, następnie `Koniec próby.` |
| `-5`, `2` | `Wynik: -2.50`, następnie `Koniec próby.` |
| `q` jako pierwszy tekst | Koniec bez pobrania drugiego tekstu i bez nowej próby. |

## Zadanie 3. Raport z mieszanego wiersza danych

**Plik:** `zadanie3.py`.

1. Pobierz jeden wiersz tekstu; podziel go na fragmenty przez `split()`.
2. Każdy fragment osobno konwertuj przez `int()`. Po `ValueError` zwiększ liczbę błędnych fragmentów i przejdź do następnego, bez kończenia całej pętli.
3. Dla poprawnych fragmentów zlicz wartości i oblicz sumę. Dopuszczamy liczby ujemne i zero; nie wprowadzamy sprawdzania zakresu.
4. Wyświetl kolejno `Poprawne:`, `Błędne:`, `Suma:` i `Średnia:`. Średnia ma dwa miejsca po kropce.
5. Przy braku poprawnych liczb zamiast średniej wyświetl `Brak poprawnych danych.`. Suma pozostaje równa 0. Nie wykonuj wtedy dzielenia.

Dla `10 x -2 3.5 0`:

```text
Poprawne: 3
Błędne: 2
Suma: 8
Średnia: 2.67
```

| Wiersz | Poprawne | Błędne | Suma | Średnia |
| --- | ---: | ---: | ---: | --- |
| `2 4 6` | 3 | 0 | 12 | 4.00 |
| `abc 3.5` | 0 | 2 | 0 | Brak poprawnych danych. |
| pusty lub same spacje | 0 | 0 | 0 | Brak poprawnych danych. |
| `-3 0 3` | 3 | 0 | 0 | 0.00 |

## Zadanie 4. NWD z bezpiecznym wejściem - adaptacja INF.04

**Plik:** `zadanie4.py` • **Źródło algorytmu:** INF.04-01-23.01-SG, część I.

1. Napisz funkcję `pobierz_liczbe(komunikat)`. Ma używać `while`, `int()` i `except ValueError`, ponawiać pytanie po błędnym zapisie i zwracać dopiero liczbę z zakresu **1-1000**.
2. Przy błędnym zapisie wyświetl `Podaj liczbę całkowitą.`. Przy wartości poza zakresem: `Zakres: 1-1000.`.
3. Napisz funkcję `nwd(a, b)` z odejmowaniem: dopóki `a != b`, odejmuj mniejszą wartość od większej. Zachowaj te nazwy argumentów; zwróć `a`.
4. W `nwd` nie używaj `input()` ani `print()`. Pobierz dwie liczby w programie głównym przez funkcję wejścia i wyświetl `NWD:` oraz wynik.
5. Dodaj krótki komentarz funkcji określający argumenty, wymaganie dodatniości i zwracany wynik. W `testy.md` zapisz dane wejściowe, oczekiwany i rzeczywisty wynik co najmniej trzech prób, w tym jednej z poprawą błędnego wejścia.

| Próba | Oczekiwana reakcja |
| --- | --- |
| `48`, `18` | `NWD: 6` |
| `7`, `7` | `NWD: 7`; pętla obliczeń nie wykona się ani razu. |
| `35`, `12` | `NWD: 1` |
| `1`, `1000` | `NWD: 1` |
| przy pobieraniu `a`: `abc → 0 → 48`, potem `b = 18` | Komunikat o zapisie, komunikat o zakresie, następnie `NWD: 6`. |
| `-5` lub `1001` | Odrzucenie wartości i nowe pytanie o tę samą liczbę. |

## Zadanie 5. Dla chętnych: Cennik i dwa rodzaje błędów - dodatkowe

**Plik:** `zadanie5.py` • **Status:** autorskie rozszerzenie po wykonaniu zadań 1-4.

1. Utwórz słownik `{"A1": 12.5, "B2": 8.0, "C3": 5.0}` z cenami w zł.
2. Pobieraj kod produktu; dokładnie małe `q` kończy pętlę bez pytania o ilość. Dla pozostałych kodów pobierz także tekst liczby sztuk przed rozpoczęciem sprawdzania.
3. Odczytaj cenę ze słownika, a następnie zamień liczbę sztuk przez `int()`. `KeyError` obsłuż komunikatem `Nieznany kod produktu.`; `ValueError` - `Podaj liczbę całkowitą.`.
4. Po udanym `try` sprawdź, czy liczba sztuk jest dodatnia. W przeciwnym przypadku: `Liczba sztuk musi być dodatnia.`.
5. Dla poprawnych danych podaj `Koszt:` z dwoma miejscami po kropce i jednostką `zł`. Po każdej próbie wróć do pytania o kod.

Próby: `A1, 3 → Koszt: 37.50 zł`; `X9, 2 → Nieznany kod produktu.`; `B2, abc → Podaj liczbę całkowitą.`; `C3, 0 → Liczba sztuk musi być dodatnia.`. Gdy oba teksty są błędne, najpierw sprawdzamy kod, więc otrzymujemy komunikat o kodzie. Nie wyszukujemy wszystkich problemów naraz.

## Diagnoza i praca domowa

Otwórz [zadanie naprawcze](diagnoza/README.md). Ma własny kontrakt i celowo błędny kod. Wykonaj je na zajęciach lub dokończ w domu zgodnie z ustaleniem prowadzącego.

## Oddanie pracy

Zachowaj źródła i niezbędne pliki danych. W `testy.md` opisz rzeczywiście wykonane próby: dane, oczekiwany wynik, wynik otrzymany i wniosek. Własną instrukcję uruchomienia zapisz w `URUCHOMIENIE.md`, aby zachować treść zadań w tym README. Dołącz dokumentację wskazaną w poleceniu. Zadania oznaczone jako dodatkowe są dla chętnych.

[Spis lekcji](../README.md)
