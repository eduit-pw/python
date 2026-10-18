# Ćwiczenia: Zespołowy projekt programistyczny: budowa serwisu internetowego z bazą danych i wersjonowaniem kodu w Git

**Temat 62 | Lekcje 127-130**

## Przygotowanie

Środowisko i polecenia uruchamiania opisano w [instrukcji głównej](../README.md#uruchamianie). Przed pracą zainstaluj zależności z dołączonego `requirements.txt` w wybranym środowisku: `py -m pip install -r requirements.txt`.

Utwórz pliki wskazane w zadaniach wewnątrz bieżącego folderu lekcji. Kod uruchamiaj w terminalu z tego folderu. Zadania wprowadzają kolejne zmiany; zachowuj wcześniejsze wersje w podfolderach, jeśli wymaga tego polecenie.

## Umowa projektu zespołowego

To blok czterech lekcji. Podzielcie odpowiedzialności za schematy, SQL, endpointy, testy i dokumentację; pracujcie na gałęziach Git, scalając małe działające zmiany. Uruchomienie: `py -m uvicorn main:app --reload`; testy: `py -m unittest discover -v`. Pliki: main.py, schematy.py, baza.py, test_api.py, requirements.txt i URUCHOMIENIE.md.

SQLite `kursy.db`: tabela kursy(id, nazwa) i zapisy(id, imie_nazwisko, kurs_id). ID zapisu jest INTEGER PRIMARY KEY AUTOINCREMENT, kurs_id to klucz obcy do kursy; włącz PRAGMA foreign_keys=ON przy każdym połączeniu. Startowa lista kursów: Programowanie w C#, Angular dla początkujących, Kurs Django. Wstawcie ją tylko przy pustej tabeli.

| Operacja | Oczekiwany wynik |
| --- | --- |
| GET /kursy | 200, lista kursów z id i nazwa |
| POST /zapisy | 201, zapis z nadanym id |
| GET /zapisy | 200, lista zapisów |
| GET /zapisy/{id} | 200 albo 404 |
| DELETE /zapisy/{id} | 204 bez ciała albo 404 |

Wejście POST: imie_nazwisko jest niepustym str po strip, do 80 znaków; kurs_id to dokładnie dodatni int (bez bool). Nadmiarowe pola odrzućcie. Błędy schematu dają 422, nieistniejący kurs 404 bez zapisu. Sukces zwraca id, imie_nazwisko, kurs_id. Testy używają osobnej bazy; obejmują poprawny zapis, błędy, usuwanie i ponowną inicjalizację bez duplikowania kursów.

## Etap 1. Kursy i trwała baza

- Utwórzcie pustą bazę i inicjalizację kursów. Udostępnijcie GET /kursy.
- Sprawdźcie listę i brak duplikatów po dwóch restartach.
- Zapiszcie test oraz URUCHOMIENIE.md z poleceniem uruchomienia.

**Punkt kontrolny:** dokładnie 3 kursy po każdym uruchomieniu.

## Etap 2. Zapis uczestnika

- Dodajcie POST /zapisy ze schematem wejścia i kontrolą istnienia kursu.
- Anna Nowak zapisuje się na Kurs Django. Wybierzcie jego ID z GET /kursy.
- Sprawdźcie pustą osobę, ujemne ID i poprawne ID nieistniejącego kursu.

**Punkt kontrolny:** 201 dla zapisu, 422 dla schematu, 404 dla brakującego kursu.

## Etap 3. Odczyt, usunięcie i testy

- Dodajcie listę zapisów, szczegóły zapisu i DELETE po ID.
- Sprawdźcie 204 bez ciała, późniejszy GET 404 oraz zachowanie innych zapisów.
- Testy mają własną bazę. Po scaleniach uruchamiajcie cały zestaw.

**Punkt kontrolny:** restart zachowuje zapisy, usunięcie dotyczy jednego ID.

## Oddanie pracy

Zachowaj źródła i niezbędne pliki danych. W `testy.md` opisz rzeczywiście wykonane próby: dane, oczekiwany wynik, wynik otrzymany i wniosek. Własną instrukcję uruchomienia zapisz w `URUCHOMIENIE.md`, aby zachować treść zadań w tym README. Dołącz dokumentację wskazaną w poleceniu. Zadania oznaczone jako dodatkowe są dla chętnych.

[Spis lekcji](../README.md)
