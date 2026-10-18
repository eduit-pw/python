# Ćwiczenia: Przygotowanie danych do testów oraz sprawdzanie działania funkcji w sytuacjach nietypowych (setUp, tearDown)

**Temat 24 | Lekcje 47-48**

## Przygotowanie

Środowisko i polecenia uruchamiania opisano w [instrukcji głównej](../README.md#uruchamianie). Wystarcza biblioteka standardowa Pythona.

Utwórz pliki wskazane w zadaniach wewnątrz bieżącego folderu lekcji. Kod uruchamiaj w terminalu z tego folderu. Zadania wprowadzają kolejne zmiany; zachowuj wcześniejsze wersje w podfolderach, jeśli wymaga tego polecenie.

## Zadanie 1. Granice magazynu - siedem testów

1. W `magazyn.py` zachowaj definicje z tematu 22, bez sekwencji demonstracyjnej wykonywanej przy imporcie.
2. W `test_magazyn.py` utwórz `self.magazyn = Magazyn(5)` w `setUp`.
3. Sprawdź stan początkowy oraz pobrania 2, 5, 6, 0, -1 i napisu `"2"`.
4. Po błędzie sprawdź typ wyjątku i stan 5. Nie dodawaj `tearDown`, bo nie ma tu zasobu wymagającego zamknięcia.

| Próba w osobnym teście | Oczekiwanie |
| --- | --- |
| Sam stan początkowy | 5 |
| `pobierz(2)` | 3 |
| `pobierz(5)` | 0; pobranie całego stanu jest dozwolone. |
| `pobierz(6)` | `BrakTowaruError`, nadal 5. |
| `pobierz(0)` | `ValueError`, nadal 5. |
| `pobierz(-1)` | `ValueError`, nadal 5. |
| `pobierz("2")` | `TypeError`, nadal 5. |

## Zadanie 2. Granice właściwości ocena - sześć testów

1. W `uczen.py` zachowaj `Uczen`, `OcenaError` i walidator z tematu 22. Imię jest napisem; po `strip()` ma być niepuste. Ocena wymaga dokładnie `int`, w zakresie 1-6.
2. W `setUp` utwórz `self.uczen = Uczen("Ala", 4)`.
3. Przypisuj do publicznej właściwości `ocena`, nie bezpośrednio do `_ocena`.
4. Dla 1 i 6 sprawdź nową wartość. Dla 0 i 7 oczekuj `OcenaError`; dla 3.5 i `True` oczekuj `TypeError`. Po odrzuceniu ocena ma wynosić 4.

Każda metoda zaczyna z oceną 4. Nie traktujemy kolejnych wierszy jako sekwencji zmian na jednym współdzielonym uczniu. Odrzucenie `True` wynika z jawnego kontraktu dokładnego typu z tematu 22.

## Zadanie 3. Cezar z arkusza i pięć dodatkowych prób - dziesięć testów

**Źródło podstawowych pięciu prób:** INF.04-02-25.06-SG, część III, tabela 4. Kolejne próby są autorskie.

1. Przenieś funkcję z tematu 23 do `cezar.py`. Zachowaj małe litery `a`-`z`, niezmienione spacje i całkowity klucz. Import nie ma pytać o wejście; interakcja konsolowa pozostaje pod warunkiem `__name__`.
2. Zachowaj pięć metod z tabeli arkusza. W `setUp` przygotuj `self.tekst = "abc"`; używaj go w tych próbach, które wymagają tego napisu.
3. Dopisz osobne testy pustego napisu, trzech spacji oraz kluczy 0, 26 i -26. Nie zmieniaj zakresu wejścia na duże litery, cyfry czy inne znaki.
4. Uruchom dziesięć testów. Zapisz `test1.png` z rzeczywistymi wynikami oraz całym ekranem, paskiem zadań i IDE, zgodnie z ćwiczonym wymaganiem użytego arkusza.
5. W `testy.md` rozdziel przypadki z arkusza i autorskie rozszerzenia. Nie wykonujemy tu całej części desktopowej ani pakowania egzaminu.

| Pochodzenie | Tekst | Klucz | Oczekiwany wynik |
| --- | --- | --- | --- |
| Arkusz: dodatni | `"abc"` | 3 | `"def"` |
| Arkusz: zawijanie | `"xyz"` | 3 | `"abc"` |
| Arkusz: ujemny | `"def"` | -3 | `"abc"` |
| Arkusz: duży klucz | `"abc"` | 29 | `"def"` |
| Arkusz: spacja | `"ab cd"` | 2 | `"cd ef"` |
| Dodatkowy: pusty napis | `""` | 3 | `""` |
| Dodatkowy: same spacje | `"   "` | 2 | `"   "` |
| Dodatkowy: klucz 0 | `"abc"` | 0 | `"abc"` |
| Dodatkowy: klucz 26 | `"abc"` | 26 | `"abc"` |
| Dodatkowy: klucz -26 | `"abc"` | -26 | `"abc"` |

Dane są stałe, a oczekiwania zapisane wprost. `setUp` nie jest obowiązkowe do testowania funkcji: stosujemy je tu do wydzielenia powtarzanego napisu. Metody mogą nadal podawać własne inne dane, np. `"xyz"`.

## Zadanie 4. Bufor i tearDown - trzy testy

1. W dołączonym `raport.py` znajduje się funkcja `zapisz_wynik(bufor, nazwa, czy_ok)`. Założenia ćwiczenia: `nazwa` jest napisem, `czy_ok` ma typ `bool`, bufor jest otwarty i umożliwia zapis tekstu.
2. W `test_raport.py` zaimportuj `io`, `unittest` i funkcję. W `setUp` twórz `self.bufor = io.StringIO()`.
3. W `tearDown` wykonuj `self.bufor.close()`.
4. Napisz trzy metody: początkowo pusty bufor, zapis dla `True`, zapis dla `False`.
5. Porównuj pełny tekst z `getvalue()` w metodzie testowej, przed zamknięciem.

| Próba | Oczekiwana zawartość |
| --- | --- |
| Bufor po przygotowaniu | `""` |
| `zapisz_wynik(bufor, "ocena", True)` | `"ocena: OK\n"` |
| `zapisz_wynik(bufor, "ocena", False)` | `"ocena: FAIL\n"` |

W literałach `\n` oznacza znak nowego wiersza. Zapisujemy i sprawdzamy rzeczywistą nową linię, a nie dwa znaki backslash i n. Nie mylimy etykiety `FAIL` zapisanej przez funkcję z niepowodzeniem testu: test zapisu tej etykiety ma przejść, jeśli tekst jest zgodny z wymaganiem.

## Zadanie 5. Dla chętnych: Sprzątanie po nieudanej asercji - dodatkowe

W osobnym folderze poza bieżącym folderem lekcji zapisz `test_sprzatanie.py`. W `setUp` przygotuj pusty bufor, a w `tearDown` zamknij go i pokaż `closed`. Test ma celowo porównywać pustą zawartość z `"tekst"`. Nie naprawiaj oczekiwania w tym pokazie: jego celem jest zaobserwowanie sprzątania po `FAIL`.

## Oddanie pracy

Zachowaj źródła i niezbędne pliki danych. W `testy.md` opisz rzeczywiście wykonane próby: dane, oczekiwany wynik, wynik otrzymany i wniosek. Własną instrukcję uruchomienia zapisz w `URUCHOMIENIE.md`, aby zachować treść zadań w tym README. Dołącz dokumentację wskazaną w poleceniu. Zadania oznaczone jako dodatkowe są dla chętnych.

[Spis lekcji](../README.md)
