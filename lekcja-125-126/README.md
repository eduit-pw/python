# Ćwiczenia: Pakowanie aplikacji do kontenera Docker: tworzenie pliku konfiguracyjnego i uruchamianie usługi

**Temat 61 | Lekcje 125-126**

## Przygotowanie

Środowisko i polecenia uruchamiania opisano w [instrukcji głównej](../README.md#uruchamianie). Przed pracą zainstaluj zależności z dołączonego `requirements.txt` w wybranym środowisku: `py -m pip install -r requirements.txt`.

Utwórz pliki wskazane w zadaniach wewnątrz bieżącego folderu lekcji. Kod uruchamiaj w terminalu z tego folderu. Zadania wprowadzają kolejne zmiany; zachowuj wcześniejsze wersje w podfolderach, jeśli wymaga tego polecenie.

## Projekt i polecenia Docker

Pracuj na własnym API SQLite z tematu 59 lub 60. Docker musi działać na stanowisku. Utwórz Dockerfile: obraz bazowy python:3.13-slim, WORKDIR /app, kopiowanie requirements.txt, instalacja zależności, kopiowanie aplikacji. Proces startowy: `python -m uvicorn main:app --host 0.0.0.0 --port 8000`. W .dockerignore pomiń .venv, .git, __pycache__, pliki baz i logi. Zachowaj GET /status. W zadaniu 3 ustaw ścieżkę SQLite na `/app/dane/albumy.db`, utwórz katalog przed startem i wykorzystaj nazwany wolumen.

```powershell
docker build -t albumy-api .
docker run --name albumy-test -p 127.0.0.1:8000:8000 albumy-api
docker logs albumy-test
```

Po próbie zatrzymaj albumy-test. Wersję z bazą uruchom po przebudowaniu obrazu:

```powershell
docker run --name albumy-db -p 127.0.0.1:8000:8000 -v albumy-dane:/app/dane albumy-api
```

Po usunięciu kontenera albumy-db uruchom to samo polecenie ponownie. Nie usuwaj wolumenu albumy-dane, bo to on przechowuje wynik próby trwałości. Wariant z błędnym CMD zbuduj pod inną nazwą obrazu i kontenera.

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

## Zadanie 1. Obraz i odpowiedź API

- Dodaj Dockerfile oraz .dockerignore do projektu. Zbuduj obraz albumy-api.
- Uruchom kontener i sprawdź /status oraz /docs.
- Zapisz, który port należy do hosta, a który do kontenera.

**Wynik kontrolny:** usługa odpowiada lokalnie na porcie 8000.

## Zadanie 2. Błąd startu

- Zatrzymaj kontener, utwórz wariant z błędnym modułem brak:app w CMD i uruchom go.
- Sprawdź docker ps -a i docker logs dla nowego kontenera.
- Przywróć main:app, zbuduj poprawny obraz i uruchom usługę.

**Wynik kontrolny:** log wskazuje brak modułu; poprawiony obraz uruchamia API.

## Zadanie 3. Baza w wolumenie

- Zmień ścieżkę bazy, przebuduj obraz i uruchom wariant albumy-db z wolumenem.
- Zatrzymaj wcześniejszy kontener, aby zwolnić port 8000. Dodaj jeden album.
- Usuń tylko kontener albumy-db i uruchom nowy z tym samym wolumenem.

**Wynik kontrolny:** zapisany album pozostaje po utworzeniu nowego kontenera.

## Zadanie 4. Instrukcja uruchomienia

- Przygotuj URUCHOMIENIE.md: build, run z portem i wolumenem, adres /docs oraz logs.
- Sprawdź polecenia od nowego kontenera. Opisz miejsce trwałej bazy.

**Wynik kontrolny:** druga osoba uruchamia usługę według instrukcji.

## Diagnoza i praca domowa

Otwórz [zadanie naprawcze](diagnoza/README.md). Ma własny kontrakt i celowo błędny kod. Wykonaj je na zajęciach lub dokończ w domu zgodnie z ustaleniem prowadzącego.

## Oddanie pracy

Zachowaj źródła i niezbędne pliki danych. W `testy.md` opisz rzeczywiście wykonane próby: dane, oczekiwany wynik, wynik otrzymany i wniosek. Własną instrukcję uruchomienia zapisz w `URUCHOMIENIE.md`, aby zachować treść zadań w tym README. Dołącz dokumentację wskazaną w poleceniu. Zadania oznaczone jako dodatkowe są dla chętnych.

[Spis lekcji](../README.md)
