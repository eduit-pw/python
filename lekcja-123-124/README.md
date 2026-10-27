# Ćwiczenia: Automatyczne testowanie działania endpointów sieciowych z użyciem modułu unittest

**Temat 60 | Lekcje 123-124**

## Przygotowanie

Środowisko i polecenia uruchamiania opisano w [instrukcji głównej](../README.md#uruchamianie). Przed pracą zainstaluj zależności z dołączonego `requirements.txt` w wybranym środowisku: `py -m pip install -r requirements.txt`.

Utwórz pliki wskazane w zadaniach wewnątrz bieżącego folderu lekcji. Kod uruchamiaj w terminalu z tego folderu. Zadania wprowadzają kolejne zmiany; zachowuj wcześniejsze wersje w podfolderach, jeśli wymaga tego polecenie.

## Kod wejściowy i izolacja testów

Pracuj na kopii rozwiązania SQLite z tematu 59. Dodaj test_api.py, unittest, tempfile i fastapi.testclient.TestClient. W setUp zachowaj dotychczasową ścieżkę baza.SCIEZKA, utwórz TemporaryDirectory i skieruj bazę do niego. Użyj menedżera kontekstu TestClient, aby lifespan utworzył tabele. W tearDown zamknij klienta, przywróć ścieżkę i usuń katalog tymczasowy. Każda metoda zaczyna od pustej własnej bazy.

Pierwsze dwa testy: (1) POST Poranek=120 daje 201, potem GET po zwróconym ID daje 200 i ten sam tytuł; (2) POST z pobrania=-1 daje 422 i GET /albumy zwraca pustą listę. Nie koduj z góry ID istniejącego w bazie użytkownika. Uruchamiaj `py -m unittest discover -v` z folderu projektu; testy nie wymagają uruchomionego Uvicorn.

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

## Zadanie 1. Pierwsze dwa testy

- Napisz setUp, tearDown i dwa testy opisane powyżej. Uruchom `py -m unittest discover -v`.
- Uruchom cały zestaw ponownie. Nie usuwaj ręcznie bazy użytkowej.

**Wynik kontrolny:** oba testy przechodzą również w drugim uruchomieniu.

## Zadanie 2. Cykl edycji i usunięcia

- Dodaj test: POST, PUT pobrania=121, GET, DELETE i ponowny GET.
- Sprawdź niezmienione ID, nowe wartości, status 204 i puste ciało DELETE.

**Wynik kontrolny:** wartość 121 przed usunięciem, 404 po usunięciu.

## Zadanie 3. Uszkodzona implementacja

- Zmień lokalnie POST tak, aby oddawał 200 zamiast 201. Uruchom testy.
- Odczytaj nazwę testu, oczekiwaną i rzeczywistą wartość.
- Przywróć poprawny kod i powtórz zestaw.

**Wynik kontrolny:** test wykrywa błąd statusu, po naprawie przechodzi.

## Zadanie 4. Start aplikacji i izolacja

- Ustaw osobną ścieżkę bazy i wykonaj próbę wewnątrz with TestClient(app) as client.
- Nie wywołuj inicjalizuj ręcznie: sprawdź start tabeli przez lifespan.
- Przywróć ścieżkę bazy po próbie. Porównaj z przygotowaniem stanu we własnym setUp.

**Wynik kontrolny:** lifespan inicjalizuje bazę przy wejściu do with.

## Diagnoza i praca domowa

Otwórz [zadanie naprawcze](diagnoza/README.md). Ma własny kontrakt i celowo błędny kod. Wykonaj je na zajęciach lub dokończ w domu zgodnie z ustaleniem prowadzącego.

## Oddanie pracy

Zachowaj źródła i niezbędne pliki danych. W `testy.md` opisz rzeczywiście wykonane próby: dane, oczekiwany wynik, wynik otrzymany i wniosek. Własną instrukcję uruchomienia zapisz w `URUCHOMIENIE.md`, aby zachować treść zadań w tym README. Dołącz dokumentację wskazaną w poleceniu. Zadania oznaczone jako dodatkowe są dla chętnych.

[Spis lekcji](../README.md)
