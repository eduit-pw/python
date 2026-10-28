# Ćwiczenia: Automatyczne sprawdzanie poprawności kodu: moduł unittest i pisanie prostych testów

**Temat 23 | Lekcje 45-46**

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

## Zadanie 1. Cztery testy funkcji logicznej

1. W `parzystosc.py` przygotuj `czy_parzysta(n)`, która dla argumentu `int` zwraca `True`, gdy liczba jest parzysta, a w przeciwnym razie `False`.
2. Utwórz `test_parzystosc.py` i klasę `TestParzystosc(unittest.TestCase)`.
3. Napisz osobne metody: zero, dodatnia parzysta, dodatnia nieparzysta, ujemna nieparzysta. Użyj `assertTrue` lub `assertFalse`.
4. Uruchom zestaw i sprawdź, że raport mówi o czterech testach.

| Argument | Oczekiwany wynik |
| --- | --- |
| 0 | `True` |
| 8 | `True` |
| 7 | `False` |
| -3 | `False` |

W tym zadaniu zakładamy argument `int`; nie dodajemy walidacji ani przypadków napisowych. Zero jest parzyste, a reszta z dzielenia -3 przez 2 w Pythonie jest różna od zera.

## Zadanie 2. Sześć testów walidatora oceny

1. W `oceny.py` zapisz same definicje `OcenaError` i `sprawdz_ocene` z tematu 22. Reguła: dokładnie `int`, zakres 1-6 włącznie.
2. W `test_oceny.py` importuj definicje i utwórz klasę testową.
3. Dla 1 i 6 sprawdź zwróconą wartość przez `assertEqual`.
4. Dla 0 i 7 sprawdź `OcenaError`; dla 3.5 i `True` sprawdź `TypeError`. Powinno być sześć metod.

| Dane | Oczekiwanie |
| --- | --- |
| 1 / 6 | Zwrócona odpowiednio wartość 1 / 6. |
| 0 / 7 | `OcenaError`. |
| 3.5 / `True` | `TypeError`. |

`bool` dziedziczy po `int`, lecz szkolny kontrakt z tematu 22 wymaga dokładnie typu `int`. To wyjaśnia odrzucenie `True`. Zwykły `assertRaises(ValueError, ...)` akceptowałby również jego podtyp `OcenaError`; tutaj używamy szczegółowego typu, ponieważ to on opisuje regułę oceny.

## Zadanie 3. Cztery testy magazynu

1. W `magazyn.py` zapisz definicje `Magazyn` i `BrakTowaruError` z tematu 22, bez sekwencji wykonywanej przy imporcie.
2. W `test_magazyn.py` napisz cztery metody. W każdej stwórz nowy `Magazyn(5)`.
3. Sprawdź stan początkowy 5, a po poprawnym pobraniu 2 - stan 3.
4. Pobranie 6 ma zgłosić `BrakTowaruError`, a pobranie 0 - `ValueError`. Po każdym z tych błędów stan ma nadal wynosić 5.

| Próba w osobnym obiekcie | Oczekiwanie |
| --- | --- |
| Konstrukcja ze stanem 5 | `stan == 5`. |
| Pobranie 2 | `stan == 3`. |
| Pobranie 6 | `BrakTowaruError`, następnie `stan == 5`. |
| Pobranie 0 | `ValueError`, następnie `stan == 5`. |

## Zadanie 4. Pięć testów szyfru Cezara z arkusza

**Źródło:** INF.04-02-25.06-SG, część III, tabela 4. Wykorzystujemy podane przypadki i własne nazwy plików.

1. W `cezar.py` przygotuj funkcję `szyfruj(tekst, klucz)`. Założenie: małe litery `a`-`z`, spacje i całkowity klucz. Spacje pozostają niezmienione, litery zawijają się w alfabecie. Klucz może być ujemny lub większy od 26. Oryginał nie wymaga walidacji tekstu.
2. W `test_cezar.py` importuj badaną funkcję. Zapisz pięć osobnych metod o nazwach opisujących cele z tabeli. Każda ma porównywać wynik rzeczywistego wywołania z podaną wartością oczekiwaną przez `assertEqual`.
3. Uruchom `python -m unittest test_cezar -v`; sprawdź pięć metod i zachowaj faktyczne wyniki.
4. Zapisz `test1.png` z wynikami oraz całym ekranem, paskiem zadań i IDE. To wymaganie ćwiczymy według użytego arkusza. Zapisz krótką notatkę w `testy.md`.

| Cel | Tekst | Klucz | Oczekiwany wynik |
| --- | --- | --- | --- |
| Klucz dodatni | `abc` | 3 | `def` |
| Zawijanie alfabetu | `xyz` | 3 | `abc` |
| Klucz ujemny | `def` | -3 | `abc` |
| Klucz większy od alfabetu | `abc` | 29 | `def` |
| Spacja | `ab cd` | 2 | `cd ef` |

Funkcja do testowania znajduje się w dołączonym pliku `cezar.py`. Napisz samodzielnie testy.

## Zadanie 5. Dla chętnych: Test ujawnia celowy błąd - dodatkowe

1. Skopiuj `cezar.py` i `test_cezar.py` do osobnego folderu `proba_bledu`, poza katalogiem podstawowego zestawu.
2. W kopii `cezar.py`, tylko w gałęzi `if znak == " ":`, zamień `wynik = wynik + " "` na `wynik = wynik + "_"`.
3. Nie zmieniaj danych i oczekiwań testów. Z katalogu kopii uruchom `python -m unittest test_cezar -v`.
4. W `testy.md` zapisz, który test ujawnił problem oraz wartości: rzeczywistą `cd_ef` i oczekiwaną `cd ef`.
5. Napraw kopię i uruchom ponownie.

## Diagnoza i praca domowa

Otwórz [zadanie naprawcze](diagnoza/README.md). Ma własny kontrakt i celowo błędny kod. Wykonaj je na zajęciach lub dokończ w domu zgodnie z ustaleniem prowadzącego.

## Oddanie pracy

Zachowaj źródła i niezbędne pliki danych. W `testy.md` opisz rzeczywiście wykonane próby: dane, oczekiwany wynik, wynik otrzymany i wniosek. Własną instrukcję uruchomienia zapisz w `URUCHOMIENIE.md`, aby zachować treść zadań w tym README. Dołącz dokumentację wskazaną w poleceniu. Zadania oznaczone jako dodatkowe są dla chętnych.

[Spis lekcji](../README.md)
