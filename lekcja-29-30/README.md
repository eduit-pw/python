# Ćwiczenia: Zmienne i metody wewnątrz obiektów oraz metody przypisane do całej klasy (@classmethod, @staticmethod)

**Temat 15 | Lekcje 29-30**

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

## Zadanie 1. Dwa konta

1. Utwórz `Konto(wlasciciel, saldo)` i metodę `wplac(kwota)`.
2. Dodaj `wyplac(kwota)`: przy wystarczającym saldzie odejmij kwotę i zwróć `True`; w przeciwnym razie zwróć `False`, zachowując saldo.
3. Utwórz konto Ali z 100 zł i Jana z 50 zł. Wpłać Ali 30 zł, wypłać 80 zł, następnie spróbuj wypłacić 60 zł.
4. Wyświetl oba wyniki wypłat i oba salda. Zakładamy dodatnie kwoty.

Oczekiwane: `True`, `False`, `50 50`. Sprawdź dodatkowo wypłatę dokładnie całego salda oraz niezależną wpłatę Jana.

## Zadanie 2. Numerowane bilety

1. Utwórz `Bilet` z polem klasy `licznik = 0`.
2. W `__init__` zwiększ wspólny licznik i przypisz jego aktualną wartość do `self.numer`.
3. Dodaj metodę klasową `ile_utworzono()`, zwracającą licznik przez `cls`.
4. Utwórz trzy obiekty. Wyświetl ich numery i licznik. Ponownie odczytaj numer pierwszego biletu. Usuń trzecią zmienną instrukcją `del` i odczytaj licznik.

Oczekiwane: numery `1 2 3`, licznik `3`, pierwszy numer `1`, licznik po `del` nadal `3`. Każde uruchomienie pliku zaczyna się od nowej definicji klasy i licznika 0. Nie dodawaj zmniejszania licznika ani `__del__`.

## Zadanie 3. Produkt tworzony na dwa sposoby

1. Utwórz `Produkt(nazwa, cena)` z polami instancji. Cena jest całkowitą liczbą złotych.
2. Dodaj metodę klasową `z_tekstu(tekst)`. Rozdziel tekst przez średnik, zamień cenę na `int` i zwróć `cls(...)`.
3. Dodaj metodę klasową `darmowy(nazwa)`, zwracającą produkt o cenie 0.
4. Sprawdź `Produkt.z_tekstu("Zeszyt;12")` i `Produkt.darmowy("Naklejka")`. Wypisz pola obu obiektów.

Oczekiwane: `Zeszyt 12`, `Naklejka 0`. Zakładamy poprawny format z jednym średnikiem i nieujemną ceną całkowitą. Dodatkowo utwórz `"Długopis;5"` i zmień cenę tylko pierwszego produktu.

## Zadanie 4. Narzędzia tekstowe

Zachowujemy wymagania algorytmiczne oryginału. Nazwa klasy i metod oraz zestaw testów są doborem szkolnym. W Pythonie odpowiednikiem `null` jest `None`.

1. Utwórz klasę `Teksty` z dwiema publicznymi metodami statycznymi, wywoływanymi bez tworzenia obiektu.
2. `policz_samogloski(tekst)` zwraca liczbę znaków z zestawu `aąeęiouóyAĄEĘIOUÓY`. Dla `None` lub `""` zwraca 0.
3. `usun_powtorzenia(tekst)` usuwa tylko sąsiadujące powtórzenia znaków i zwraca napis. Dla `None` lub `""` zwraca `""`.
4. Program główny wczytuje napis i wyświetla opisane wyniki obu metod. Dodaj komentarz klasy i dokumentację.

**Podpowiedź algorytmiczna:** po obsłużeniu `None` i pustego napisu ustaw wynik na pierwszy znak. Pętla zaczyna się od indeksu 1. Dopisz znak, jeśli różni się od poprzedniego znaku wejścia. Znaki rozdzielone innymi znakami pozostają. Nie używaj `set`, wyrażeń regularnych ani gotowej eliminacji duplikatów.

| Argument | Liczba samogłosek | Wynik po usunięciu powtórzeń |
|---|---:|---|
| `None` | 0 | `""` |
| `""` | 0 | `""` |
| `"A"` | 1 | `"A"` |
| `"aaabbcdd"` | 3 | `"abcd"` |
| `"ala"` | 2 | `"ala"` |
| `"  AĄĘÓyy!!  "` | 6 | `" AĄĘÓy! "` |
| `"bBBb"` | 0 | `"bBb"` |

`input()` zawsze zwraca napis, więc `None` testujemy osobnym wywołaniem metod. Nie stosuj `.strip()` do wejścia: spacje są częścią danych i również podlegają przetwarzaniu. Porównanie znaków uwzględnia wielkość liter. Samogłoski liczymy w oryginalnym napisie, zanim usuniemy powtórzenia.

## Zadanie 5. Dla chętnych: Osobne dzienniki (autorskie, opcjonalne)

Utwórz klasę `Dziennik`, w której początkowo `wpisy = []` znajduje się w ciele klasy. Pokaż problem wspólnej listy i napraw go. Każdy obiekt ma własne `wpisy`. Dodaj metodę instancji `dodaj(tekst)`, utwórz dwa dzienniki, dodaj im różne wpisy i sprawdź, że każda lista zawiera wyłącznie swoje dane. Wyjaśnij różnicę między przypisaniem nowej listy w `__init__` a `append()` na wspólnej liście klasy.

## Diagnoza i praca domowa

Otwórz [zadanie naprawcze](diagnoza/README.md). Ma własny kontrakt i celowo błędny kod. Wykonaj je na zajęciach lub dokończ w domu zgodnie z ustaleniem prowadzącego.

## Oddanie pracy

Zachowaj źródła i niezbędne pliki danych. W `testy.md` opisz rzeczywiście wykonane próby: dane, oczekiwany wynik, wynik otrzymany i wniosek. Własną instrukcję uruchomienia zapisz w `URUCHOMIENIE.md`, aby zachować treść zadań w tym README. Dołącz dokumentację wskazaną w poleceniu. Zadania oznaczone jako dodatkowe są dla chętnych.

[Spis lekcji](../README.md)
