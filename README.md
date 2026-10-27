# Python - ćwiczenia praktyczne

Materiały dla uczniów technikum. W folderach znajdziesz polecenia, dane wejściowe i wyniki kontrolne. Rozwiązania przygotowujesz samodzielnie. Ćwiczenia obejmują podstawy Pythona, obiekty, testy, algorytmy, pliki, aplikacje PyQt6 i usługi internetowe.

## Jak korzystać

1. Otwórz folder odpowiedniej lekcji i przeczytaj README. Numer tematu i numery lekcji są różne.
2. Przygotuj środowisko. Wykonuj polecenia terminalu z folderu wskazanego przy zadaniu.
3. Przed uruchomieniem zapisz oczekiwany wynik. Napisz własny kod, porównaj rezultat i sprawdź przypadki graniczne.
4. Zapisz testy i własną instrukcję w `testy.md` oraz `URUCHOMIENIE.md`. Zachowaj README z poleceniami.

## Uruchamianie

Materiały przygotowano dla Python 3.13. Poniższe polecenia dotyczą Windows i PowerShell. Po aktywacji używaj `python`, który ma wskazywać interpreter wybranego środowiska. W innych systemach użyj odpowiadającego mu `python3` lub `python`.

W katalogu repozytorium utwórz i aktywuj środowisko:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python --version
python -c "import sys; print(sys.executable)"
```

Ostatnie polecenie powinno pokazać interpreter z `.venv`. W VS Code wybierz ten sam interpreter. Jeśli korzystasz z kilku środowisk, sprawdź tę ścieżkę w każdym terminalu przed instalacją i uruchomieniem.

Przejdź do folderu lekcji. Dla prostego skryptu:

```powershell
cd lekcja-03-04
python zadanie1.py
```

Nazwy plików w zadaniach mają pierwszeństwo; polecenie pokazuje sposób uruchomienia pliku, który sam utworzysz. Gdy zadanie nie narzuca nazwy, użyj `zadanie1.py`, `zadanie2.py` itd. Projekty rozwijane etapami mogą korzystać z jednego main.py. W folderach z zewnętrznymi bibliotekami jest requirements.txt:

```powershell
python -m pip install -r requirements.txt
```

Bibliotek wbudowanych, np. csv, json, sqlite3, unittest i asyncio, nie instaluj z pip. PyQt6 wymaga środowiska graficznego. Qt Designer i Docker muszą być dostępne osobno na stanowisku. Django używa linii 5.2, Pydantic linii 2; zakresy wersji w requirements odpowiadają materiałom kursu.

Testy uruchamiaj z folderu projektu:

```powershell
python -m unittest discover -v
```

Celowo błędne demonstracje testów trzymaj poza folderem podstawowego zestawu. Nie uruchamiaj discover z katalogu całego kursu: lekcje mogą mieć moduły o tych samych nazwach.

Django: polecenia manage.py wykonuj w folderze szkola_web. FastAPI: `python -m uvicorn main:app --reload` wykonuj obok main.py. Lokalne serwery zatrzymuj Ctrl+C. Przed uruchomieniem kolejnego zwolnij port 8000.

## Kontynuacja projektów

Kopiuj własną działającą wersję poprzedniego projektu do folderu następnej lekcji, bez .venv i plików tymczasowych. Dotyczy to zwłaszcza serii Django 51-54 oraz API 55-60. Zachowaj poprzednią wersję, żeby móc do niej wrócić. Folder zawiera startery, a nie gotową implementację poprzedniego zadania.

Dane wejściowe są dołączone tam, gdzie polecenie ich wymaga. Klasa bazowa urządzenia, funkcja Cezara w lekcji testowania, funkcja zapisu do bufora i lokalny serwer integracyjny są materiałami początkowymi, a nie pełnymi rozwiązaniami ćwiczeń. Pozostałe wskazane pliki utwórz samodzielnie.

## Spis lekcji

67 tematów obejmuje 140 godzin lekcyjnych. Projekty w tematach 26, 47 i 62 zajmują po cztery lekcje; dlatego późniejsze numery lekcji nie wynikają z prostego podwojenia numeru tematu.

| Temat | Lekcje | Zakres |
| ---: | :---: | --- |
| 1 | [01-02](lekcja-01-02/README.md) | Organizacja stanowiska komputerowego, szkolenie BHP i regulamin pracowni. Wprowadzenie do języka Python i wirtualne środowiska (venv) |
| 2 | [03-04](lekcja-03-04/README.md) | Zmienne, proste typy danych oraz pobieranie i formatowanie wyświetlanych informacji (f-string) |
| 3 | [05-06](lekcja-05-06/README.md) | Działania na liczbach, warunki logiczne oraz podejmowanie decyzji w programie (if, elif, else) |
| 4 | [07-08](lekcja-07-08/README.md) | Powtarzanie operacji: pętle for oraz while, przerywanie i wznawianie pętli |
| 5 | [09-10](lekcja-09-10/README.md) | Praca z tekstem: łączenie, wycinanie fragmentów napisów oraz metody tekstowe |
| 6 | [11-12](lekcja-11-12/README.md) | Tworzenie własnych funkcji, przekazywanie argumentów, zwracanie wyników oraz oznaczanie typów danych |
| 7 | [13-14](lekcja-13-14/README.md) | Widoczność zmiennych w programie, wartości domyślne i funkcje z dowolną liczbą argumentów (*args, **kwargs) |
| 8 | [15-16](lekcja-15-16/README.md) | Praca z listami: dodawanie, usuwanie, modyfikowanie i przeszukiwanie elementów |
| 9 | [17-18](lekcja-17-18/README.md) | Niemodyfikowalne krotki oraz działania na zbiorach: łączenie, część wspólna i usuwanie duplikatów |
| 10 | [19-20](lekcja-19-20/README.md) | Praca ze słownikami: tworzenie powiązań klucz-wartość i przeglądanie danych |
| 11 | [21-22](lekcja-21-22/README.md) | Skrócony zapis tworzenia list i słowników oraz jednoczesne numerowanie elementów pętli (enumerate, zip) |
| 12 | [23-24](lekcja-23-24/README.md) | Krótkie funkcje jednorazowe (lambda), przekształcanie list oraz losowanie liczb i moduł matematyczny |
| 13 | [25-26](lekcja-25-26/README.md) | Praktyczny sprawdzian umiejętności: podstawy programowania, kolekcje danych, funkcje i standard PEP 8 |
| 14 | [27-28](lekcja-27-28/README.md) | Podstawy programowania obiektowego: tworzenie klas, obiektów i konstruktora __init__ |
| 15 | [29-30](lekcja-29-30/README.md) | Zmienne i metody wewnątrz obiektów oraz metody przypisane do całej klasy (@classmethod, @staticmethod) |
| 16 | [31-32](lekcja-31-32/README.md) | Specjalne metody obiektów: czytelne wyświetlanie obiektu, sprawdzanie długości i porównywanie (__str__, __repr__, __len__, __eq__) |
| 17 | [33-34](lekcja-33-34/README.md) | Ukrywanie wewnętrznych danych obiektu oraz bezpieczny dostęp za pomocą właściwości (@property) |
| 18 | [35-36](lekcja-35-36/README.md) | Dziedziczenie: tworzenie klas pochodnych i ponowne wykorzystanie kodu klasy bazowej (super) |
| 19 | [37-38](lekcja-37-38/README.md) | Wspólny interfejs dla różnych obiektów oraz tworzenie klas wzorcowych (@abstractmethod) |
| 20 | [39-40](lekcja-39-40/README.md) | Własne mechanizmy przeglądania elementów i generatory oszczędzające pamięć (yield) |
| 21 | [41-42](lekcja-41-42/README.md) | Zabezpieczanie programu przed awariami: obsługa błędów i wyjątków (try, except, finally) |
| 22 | [43-44](lekcja-43-44/README.md) | Własne komunikaty błędów oraz sprawdzanie poprawności danych wprowadzanych do obiektów |
| 23 | [45-46](lekcja-45-46/README.md) | Automatyczne sprawdzanie poprawności kodu: moduł unittest i pisanie prostych testów |
| 24 | [47-48](lekcja-47-48/README.md) | Przygotowanie danych do testów oraz sprawdzanie działania funkcji w sytuacjach nietypowych (setUp, tearDown) |
| 25 | [49-50](lekcja-49-50/README.md) | Wzorce projektowe w programowaniu obiektowym: Singleton, Metoda Wytwórcza oraz tworzenie własnych dekoratorów |
| 26 | [51-54](lekcja-51-54/README.md) | Projekt programistyczny: samodzielne stworzenie aplikacji obiektowej wraz z testami i dokumentacją |
| 27 | [55-56](lekcja-55-56/README.md) | Bezpieczny odczyt i zapis danych w plikach tekstowych z użyciem instrukcji with |
| 28 | [57-58](lekcja-57-58/README.md) | Sprawdzanie obecności plików, tworzenie folderów i porządkowanie dysku z poziomu Pythona (os, pathlib) |
| 29 | [59-60](lekcja-59-60/README.md) | Przetwarzanie ustrukturyzowanych danych tekstowych: pliki CSV oraz format JSON |
| 30 | [61-62](lekcja-61-62/README.md) | Sprawdzanie poprawności wpisów tekstowych za pomocą wyrażeń regularnych (moduł re) |
| 31 | [63-64](lekcja-63-64/README.md) | Zamiana liczb między systemami dwójkowym, ósemkowym, dziesiętnym i szesnastkowym oraz Schemat Hornera |
| 32 | [65-66](lekcja-65-66/README.md) | Szyfrowanie danych: zamiana liter w tekście, szyfr Cezara oraz szyfr GADERYPOLUKI |
| 33 | [67-68](lekcja-67-68/README.md) | Działania na liczbach: sprawdzanie liczb pierwszych, Sito Eratostenesa, rozkład na czynniki i Algorytm Euklidesa |
| 34 | [69-70](lekcja-69-70/README.md) | Algorytmy na tekstach i listach: badanie palindromów, anagramów oraz Algorytm Wyszukiwania Lidera |
| 35 | [71-72](lekcja-71-72/README.md) | Szybkość działania programów: wyszukiwanie liniowe, wyszukiwanie w posortowanej liście oraz Metoda Bisekcji |
| 36 | [73-74](lekcja-73-74/README.md) | Wyszukiwanie minimum i maksimum w parach oraz algorytmy sortowania danych (bąbelkowe, przez wstawianie, wybór) |
| 37 | [75-76](lekcja-75-76/README.md) | Funkcje wywołujące same siebie (rekurencja), sortowanie szybkie oraz kolejki i stosy |
| 38 | [77-78](lekcja-77-78/README.md) | Praca z datą i czasem: formatowanie, obliczanie różnic czasowych oraz filtrowanie danych (moduł datetime) |
| 39 | [79-80](lekcja-79-80/README.md) | Tworzenie pierwszego okna aplikacji w PyQt: okno główne i uruchomienie programu |
| 40 | [81-82](lekcja-81-82/README.md) | Wizualne projektowanie wyglądu okna w programie Qt Designer i łączenie go z kodem Pythona |
| 41 | [83-84](lekcja-83-84/README.md) | Dodawanie i obsługa elementów okna: napisy, pola tekstowe, przyciski i opcje wyboru |
| 42 | [85-86](lekcja-85-86/README.md) | Łączenie przycisków z akcjami w kodzie: reagowanie na kliknięcia i wprowadzany tekst (sygnały i sloty) |
| 43 | [87-88](lekcja-87-88/README.md) | Układanie elementów w oknie: rozmieszczenie pionowe, poziome i dopasowanie do rozmiaru ekranu |
| 44 | [89-90](lekcja-89-90/README.md) | Tworzenie menu programu, paska narzędzi oraz okienek z komunikatami i wyborem pliku |
| 45 | [91-92](lekcja-91-92/README.md) | Wyświetlanie list i tabel z danymi w oknie aplikacji oraz zaznaczanie wierszy (QTableWidget) |
| 46 | [93-94](lekcja-93-94/README.md) | Zapisywanie i odczytywanie danych z lokalnej bazy danych SQLite w aplikacji okienkowej (sqlite3) |
| 47 | [95-98](lekcja-95-98/README.md) | Projekt programistyczny: budowa kompletnego programu okienkowego z bazą danych i formularzem |
| 48 | [99-100](lekcja-99-100/README.md) | Przygotowanie programu do uruchomienia na innych komputerach: tworzenie pliku wykonywalnego (.exe) |
| 49 | [101-102](lekcja-101-102/README.md) | Praktyczny sprawdzian umiejętności: projektowanie i implementacja aplikacji okienkowej z interfejsem graficznym |
| 50 | [103-104](lekcja-103-104/README.md) | Jak działa sieć i strony internetowe: zapytania i odpowiedzi, przesyłanie danych oraz zasady API |
| 51 | [105-106](lekcja-105-106/README.md) | Pierwsze kroki z frameworkiem Django: tworzenie projektu, ustawienia i adresy podstron |
| 52 | [107-108](lekcja-107-108/README.md) | Wyświetlanie danych na stronach w Django: szablony HTML i przekazywanie informacji do widoku |
| 53 | [109-110](lekcja-109-110/README.md) | Tworzenie tabel bazy danych w Django za pomocą modeli i aktualizacja bazy (ORM) |
| 54 | [111-112](lekcja-111-112/README.md) | Gotowy panel zarządzania danymi w Django oraz tworzenie i sprawdzanie formularzy |
| 55 | [113-114](lekcja-113-114/README.md) | Nowoczesne usługi sieciowe w FastAPI: uruchomienie serwera i pierwsze punkty dostępu |
| 56 | [115-116](lekcja-115-116/README.md) | Sprawdzanie i zabezpieczanie przesyłanych danych w FastAPI za pomocą schematów Pydantic |
| 57 | [117-118](lekcja-117-118/README.md) | Pełna obsługa danych w FastAPI: pobieranie, dodawanie, edycja i usuwanie wpisów przez sieć |
| 58 | [119-120](lekcja-119-120/README.md) | Przeglądanie i sprawdzanie działania usługi za pomocą automatycznej strony Swagger UI i narzędzia typu Postman |
| 59 | [121-122](lekcja-121-122/README.md) | Połączenie serwisu sieciowego FastAPI z relacyjną bazą danych SQLite |
| 60 | [123-124](lekcja-123-124/README.md) | Automatyczne testowanie działania endpointów sieciowych z użyciem modułu unittest |
| 61 | [125-126](lekcja-125-126/README.md) | Pakowanie aplikacji do kontenera Docker: tworzenie pliku konfiguracyjnego i uruchamianie usługi |
| 62 | [127-130](lekcja-127-130/README.md) | Zespołowy projekt programistyczny: budowa serwisu internetowego z bazą danych i wersjonowaniem kodu w Git |
| 63 | [131-132](lekcja-131-132/README.md) | Komunikacja sieciowa i integracja z zewnętrznymi serwisami oraz modelami AI za pomocą biblioteki requests |
| 64 | [133-134](lekcja-133-134/README.md) | Odczytywanie i wyciąganie wybranych informacji ze stron internetowych za pomocą biblioteki BeautifulSoup4 |
| 65 | [135-136](lekcja-135-136/README.md) | Rejestrowanie pracy programu: zapisywanie komunikatów, ostrzeżeń i błędów do pliku dziennika (logging) |
| 66 | [137-138](lekcja-137-138/README.md) | Tworzenie programów uruchamianych z wiersza poleceń z opcjami i parametrami (argparse, dotenv) |
| 67 | [139-140](lekcja-139-140/README.md) | Współbieżne wykonywanie zadań i programowanie asynchroniczne: moduł asyncio oraz instrukcje async i await |

## Dokumentowanie pracy

W `testy.md` zapisuj własne, wykonane próby. Przykładowa tabela:

| Zadanie i dane | Wynik oczekiwany | Wynik otrzymany | Wniosek |
| --- | --- | --- | --- |
| Uzupełnij po wykonaniu próby | Wpisz przed uruchomieniem | Wpisz po uruchomieniu | Opisz zgodność lub poprawkę |

W instrukcji URUCHOMIENIE.md podaj rzeczywiste wersje narzędzi, pliki wejściowe, polecenia i ewentualne ograniczenia. Zachowuj nazwy zrzutów i dokumentów wskazane w konkretnym zadaniu.

Do Git dodawaj kod, potrzebne dane, pliki .ui, migracje Django i konfigurację projektu. Środowisk .venv, cache, logów, baz roboczych i sekretów nie dodawaj. `.env.example` jest przykładem do lokalnej konfiguracji. Plik `.gitignore` jest dołączony.

## Ćwiczenia z arkuszy

Jeśli zadanie jest adaptacją INF.04, jego zakres opisano w treści. Rozszerzenia szkolne nie są dodatkowym wymaganiem oryginalnego arkusza. Podczas egzaminu stosuj technologię, nazwy plików, algorytm i dokumentację wskazane w otrzymanym poleceniu. Tematy Django, FastAPI i Docker rozwijają kurs. Zadania algorytmiczne ćwiczą również analizę przydatną na maturze.

## Wersja kursu i dodatkowe materiały

Wersja 2: 67 tematów, 140 godzin lekcyjnych. W każdej zwykłej lekcji jest `SCIAGA.md`, folder `startery/`, zadanie `diagnoza/` i jeden plik `testy.md`. Prezentacje są w osobnej paczce; obok każdego PPTX jest tekstowa wersja treści. Możesz do niej wrócić bez otwierania podręcznika.

Tematy 13, 26, 47, 49 i 62 zawierają zakres przygotowania. Właściwe polecenia otrzymasz od nauczyciela. Wymagania zadań pochodzą z konspektów kursu; oznaczenia adaptacji INF.04 pozostawiono przy ćwiczeniach. Czas zajęć i wymagania tego kursu nie są regulaminem oficjalnego egzaminu.

Po aktywacji środowiska używaj `python`; bez aktywacji uruchom `ścieżka-do-repo\.venv\Scripts\python.exe`. Qt Designer, Docker i budowanie plików Windows przygotuj zgodnie z instrukcją stanowiska. Nie dołączaj haseł, plików .env, baz uczniów ani .venv do repozytorium.

[Zbiorcza ściąga do tematów 16-20](SCIAGA_16-20.md)
