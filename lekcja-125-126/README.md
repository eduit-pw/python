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

## Oddanie pracy

Zachowaj źródła i niezbędne pliki danych. W `testy.md` opisz rzeczywiście wykonane próby: dane, oczekiwany wynik, wynik otrzymany i wniosek. Własną instrukcję uruchomienia zapisz w `URUCHOMIENIE.md`, aby zachować treść zadań w tym README. Dołącz dokumentację wskazaną w poleceniu. Zadania oznaczone jako dodatkowe są dla chętnych.

[Spis lekcji](../README.md)
