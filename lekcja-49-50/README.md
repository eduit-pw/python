# Ćwiczenia: Wzorce projektowe w programowaniu obiektowym: Singleton, Metoda Wytwórcza oraz tworzenie własnych dekoratorów

**Temat 25 | Lekcje 49-50**

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

## Zadanie 1. Wspólne ustawienia - trzy testy

1. Utwórz `Ustawienia` z polem klasowym `_instancja` oraz metodą `__new__`.
2. Przy pierwszym utworzeniu ustaw `tryb = "jasny"`. Kolejne wywołanie klasy ma zachować zmieniony tryb.
3. Utwórz dwa odwołania, zmień tryb przez pierwsze i odczytaj przez drugie. Sprawdź `pierwsze is drugie`.
4. Napisz trzy testy: ta sama instancja, początkowy tryb, zachowanie zmiany po kolejnym `Ustawienia()`.
5. Resetuj pole klasowe przed i po każdym teście, przez przypisanie `Ustawienia._instancja = None`.

| Próba | Oczekiwanie |
| --- | --- |
| Dwa wywołania `Ustawienia()` | Tożsamość `True`. |
| Pierwsze ustawienia | `"jasny"`. |
| Zmiana na `"ciemny"`, ponowne wywołanie | Nadal `"ciemny"`. |

## Zadanie 2. Metoda Wytwórcza - cztery testy

1. Zdefiniuj klasy produktów: `Powiadomienie`, `Email`, `SMS`.
2. Utwórz bazowego twórcę `Nadawca` z abstrakcyjną metodą `utworz`.
3. W `przygotuj_wiadomosc` wywołaj metodę wytwórczą i metodę produktu.
4. W podklasach twórcy zwracaj odpowiednio `Email()` i `SMS()`.
5. Sprawdź typ obu produktów oraz wynik wspólnej operacji dla napisu `"Gotowe"`.

| Twórca | Produkt | Oczekiwana wiadomość |
| --- | --- | --- |
| `NadawcaEmail` | `Email` | `"E-mail: Gotowe"` |
| `NadawcaSMS` | `SMS` | `"SMS: Gotowe"` |

Nie wysyłamy wiadomości. Funkcja produktu jedynie przygotowuje napis. Wspólna operacja twórcy nie zawiera warunków zależnych od typu produktu.

## Zadanie 3. Dekorator logujący - cztery testy

1. Zdefiniuj `loguj(funkcja)` oraz wewnętrzne `opakowanie(*args, **kwargs)`.
2. Dodaj komunikat początku, pojedyncze wywołanie funkcji i komunikat końca po sukcesie.
3. Zwróć oryginalny wynik. Z dekoratora zwróć funkcję `opakowanie`, bez nawiasów.
4. Użyj `wraps`, aby zachować nazwę i docstring.
5. Oznacz `dodaj` przez `@loguj`. Wywołaj pozycyjnie i przez argumenty nazwane.
6. Sprawdź wynik i log, argumenty nazwane, metadane oraz przejście wyjątku do wywołującego.

| Próba | Oczekiwanie |
| --- | --- |
| `dodaj(2, 3)` | Wynik 5, początek i koniec w logu. |
| `dodaj(a=2, b=3)` | Wynik 5. |
| Nazwa i docstring | Dane oryginalnej funkcji. |
| Funkcja zgłasza `ValueError` | Ten sam typ wyjątku, tylko komunikat początku. |

## Zadanie 4. NWD z arkusza i osobne opakowanie - pięć testów

1. W `nwd.py` zachowaj algorytm z odejmowaniem. Funkcja przyjmuje dwa dodatnie argumenty i zwraca liczbę, bez `input()` ani `print()`.
2. Uzupełnij komentarz nad funkcją. Program główny pobiera dane i wypisuje wynik.
3. W osobnym `nwd_demo.py` utwórz `nwd_z_logiem = loguj(nwd)`. Nie nadpisuj egzaminowej funkcji.
4. Porównaj pięć dodatnich przypadków z tabeli: obie wersje mają zwracać ten sam wynik.
5. Sprawdź, że oryginalna funkcja niczego nie wypisuje, a opakowanie dodaje dwa komunikaty. Są to autorskie testy lekcyjne, nie tabela narzucona przez arkusz.
6. Zapisz wynik działania oryginalnej konsoli i krótką notatkę `wzorce.md`: która część pochodzi z zadania, a która jest rozszerzeniem.

| a | b | Oczekiwany NWD |
| --- | --- | --- |
| 84 | 30 | 6 |
| 7 | 7 | 7 |
| 17 | 13 | 1 |
| 12 | 36 | 12 |
| 36 | 12 | 12 |

## Zadanie 5. Dla chętnych: Trzeci produkt - dodatkowe

Dodaj `Push(Powiadomienie)` i `NadawcaPush(Nadawca)`. Zwróć `"Push: " + tekst`. Wykorzystaj odziedziczoną metodę `przygotuj_wiadomosc`, bez zmiany `Nadawca`, `Email` i `SMS`. Sprawdź typ produktu i wiadomość `"Push: Gotowe"`.

## Diagnoza i praca domowa

Otwórz [zadanie naprawcze](diagnoza/README.md). Ma własny kontrakt i celowo błędny kod. Wykonaj je na zajęciach lub dokończ w domu zgodnie z ustaleniem prowadzącego.

## Oddanie pracy

Zachowaj źródła i niezbędne pliki danych. W `testy.md` opisz rzeczywiście wykonane próby: dane, oczekiwany wynik, wynik otrzymany i wniosek. Własną instrukcję uruchomienia zapisz w `URUCHOMIENIE.md`, aby zachować treść zadań w tym README. Dołącz dokumentację wskazaną w poleceniu. Zadania oznaczone jako dodatkowe są dla chętnych.

[Spis lekcji](../README.md)
