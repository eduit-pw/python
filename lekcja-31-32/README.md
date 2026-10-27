# Ćwiczenia: Specjalne metody obiektów: czytelne wyświetlanie obiektu, sprawdzanie długości i porównywanie (__str__, __repr__, __len__, __eq__)

**Temat 16 | Lekcje 31-32**

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

## Zadanie 1. Książka w konsoli

Ćwiczenie autorskie.

1. Napisz `Ksiazka(tytul, autor)` z atrybutami instancji.
2. `__str__` zwraca `"tytuł - autor"`, korzystając z aktualnych danych obiektu.
3. `__repr__` zwraca opis `Ksiazka('tytuł', 'autor')`. Użyj `!r`, aby reprezentować argumenty napisowe.
4. Utwórz `Ksiazka("Solaris", "Lem")`. Porównaj wyniki `print(ksiazka)`, `print(repr(ksiazka))`, `print([ksiazka])`.
5. Zmień tytuł na `"Eden"`. Sprawdź, czy oba opisy odzwierciedlają zmianę.

Początkowo oczekujemy `Solaris - Lem`, `Ksiazka('Solaris', 'Lem')` oraz `[Ksiazka('Solaris', 'Lem')]`. Po zmianie otrzymujemy `Eden - Lem` oraz `Ksiazka('Eden', 'Lem')`. Przyjmujemy napisy; nie dodajemy walidacji danych.

## Zadanie 2. Dziennik z długością

Ćwiczenie autorskie.

1. `Dziennik()` tworzy własną pustą listę `wpisy`.
2. `dodaj(tekst)` dopisuje napis, a `__len__` zwraca liczbę wpisów.
3. Dodaj `__str__` zwracające napis `"Wpisy: N"`, gdzie N jest bieżącą liczbą wpisów.
4. Utwórz dwa dzienniki. Do pierwszego dodaj kolejno `"Python"`, `""`, `"Powtórka"`. Drugi pozostaje pusty.
5. Po każdym dodaniu sprawdź długość i opis. Pusty napis jest pełnoprawnym wpisem w tej specyfikacji.

| Moment | `len(pierwszy)` | `str(pierwszy)` | `len(drugi)` |
|---|---|---|---|
| Początek | 0 | Wpisy: 0 | 0 |
| Po Python | 1 | Wpisy: 1 | 0 |
| Po pustym napisie | 2 | Wpisy: 2 | 0 |
| Po Powtórka | 3 | Wpisy: 3 | 0 |

## Zadanie 3. Porównywanie punktów

Ćwiczenie autorskie.

1. Napisz `Punkt(x, y)`. Równe punkty mają równe obie współrzędne.
2. Dodaj `__eq__`. Dla argumentu innego niż `Punkt` zwróć `NotImplemented`.
3. Utwórz `a = Punkt(2, 3)`, `b = Punkt(2, 3)`, `c = Punkt(2, 4)` i `d = a`.
4. Sprawdź `a == b`, `a == c`, `a is b`, `a is d`, `a == (2, 3)`.
5. Zmień `b.y` na 9 i ponownie sprawdź `a == b`. Oczekujemy `False`.

| Porównanie przed zmianą | Wynik |
|---|---|
| `a == b` | True |
| `a == c` | False |
| `a is b` | False |
| `a is d` | True |
| `a == (2, 3)` | False |

Pytanie: dlaczego `a == b` może być prawdą, mimo że `a is b` jest fałszem? Odpowiedź: dwa różne obiekty mogą reprezentować takie same współrzędne.

## Zadanie 4A. Notatka według arkusza

**Adaptacja:** CKE INF.04-02-23.01-SG, część I, s. 2. Wymagania w skrócie:

1. Zdefiniuj `Notatka` z licznikiem klasowym `__licznik = 0`, identyfikatorem instancji `__identyfikator` i tekstowymi `_tytul`, `_tresc`.
2. Konstruktor przyjmuje tytuł i treść. Najpierw zwiększa licznik klasy, potem zapisuje jego wartość jako identyfikator i przypisuje teksty.
3. `wyswietl()` wypisuje tytuł i treść. `diagnostyka()` wypisuje wszystkie cztery pola, oddzielając je średnikami. Obie metody nie zwracają wyniku.
4. Utwórz dwie notatki z danymi poniżej. Wywołaj dla każdej obie metody. Udokumentuj program zgodnie z zadaniem 4C.

Konwencje podkreślników są wymaganiem tego klucza: dwa dla pól numerycznych, jeden dla tekstowych. Szczegóły hermetyzacji rozwiniemy w temacie 17. Licznik aktualizuj przez `Notatka.__licznik`, aby nie utworzyć osobnego licznika instancji.

**Dane:** pierwsza notatka: tytuł `"Python"`, treść `"Powtórz klasy"`; druga: tytuł `"Egzamin"`, treść `"Sprawdź kod"`.

Utwórz **obie notatki przed wywołaniem diagnostyki**. Przyjmujemy kolejność pól w wydruku: identyfikator, licznik klasy, tytuł, treść. Pierwsza linia diagnostyczna to `1;2;Python;Powtórz klasy`, druga `2;2;Egzamin;Sprawdź kod`.

Identyfikator pierwszego obiektu pozostaje 1, choć licznik wspólny ma już wartość 2. Jeśli wyświetlisz pierwszą notatkę przed utworzeniem drugiej, licznik będzie wtedy 1; to inna prawidłowa kolejność działań, ale nie nasz ustalony scenariusz.

## Zadanie 4B. Metody specjalne notatki

**Autorskie rozszerzenie, poza wymaganiami CKE.** Dodaj do gotowej klasy z 4A:

1. `__str__` zwracające `"tytuł: treść"`.
2. `__len__` zwracające liczbę znaków **wyłącznie treści**.
3. Wyświetl obie notatki przez `print()` i sprawdź `len()`.

Wyniki: `Python: Powtórz klasy` i 13 znaków; `Egzamin: Sprawdź kod` i 11 znaków. Dla treści pustej `len()` wynosi 0. Nie tworzymy tutaj dodatkowego obiektu w głównym scenariuszu diagnostycznym - próba pustej treści powinna być osobnym uruchomieniem albo wystąpić po zakończeniu testów dwóch notatek.

`__str__` zwraca napis, a `wyswietl()` drukuje informacje. Zachowaj obie metody. Samo dodanie metod specjalnych nie zastępuje wykonania polecenia z arkusza.

## Zadanie 4C. Dokumentacja i oddanie

- Nad klasą umieść komentarz `#`: nazwa klasy, przeznaczenie, nazwy wszystkich pól z ich opisem i szkolny numer autora. To zakres komentarza z tego arkusza, inny niż lista metod używana w niektórych innych zadaniach.
- W folderze `konsola` zapisz `main.py` oraz archiwum projektu `konsola.zip`.
- W folderze `dokumentacja` umieść `konsola1.png` z pełnym ekranem, wynikiem i środowiskiem pracy. Pasek zadań powinien być widoczny.
- Zapisz dokument `egzamin.docx` albo `egzamin.odt` ze zrzutem oraz nazwami systemu, środowiska i języka. Dokumentujemy tylko realizowaną aplikację konsolową.

## Zadanie 5. Dla chętnych: Równość książek - dodatkowe

Ćwiczenie autorskie. Rozszerz `Ksiazka` z zadania 1 o `__eq__`. Dwie książki są równe, gdy mają takie same tytuły i autorów. Dla innych typów zwróć `NotImplemented`.

Sprawdź dwie książki Solaris/Lem, książkę Eden/Lem oraz porównanie książki z napisem `"Solaris"`. Wyniki porównań pierwszej z pozostałymi: `True`, `False`, `False`. Porównanie dwóch osobno utworzonych Solaris/Lem przez `is` daje `False`. Nie implementuj sortowania ani haszowania.

## Diagnoza i praca domowa

Otwórz [zadanie naprawcze](diagnoza/README.md). Ma własny kontrakt i celowo błędny kod. Wykonaj je na zajęciach lub dokończ w domu zgodnie z ustaleniem prowadzącego.

## Oddanie pracy

Zachowaj źródła i niezbędne pliki danych. W `testy.md` opisz rzeczywiście wykonane próby: dane, oczekiwany wynik, wynik otrzymany i wniosek. Własną instrukcję uruchomienia zapisz w `URUCHOMIENIE.md`, aby zachować treść zadań w tym README. Dołącz dokumentację wskazaną w poleceniu. Zadania oznaczone jako dodatkowe są dla chętnych.

[Spis lekcji](../README.md)
