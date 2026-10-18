# Ćwiczenia: Połączenie serwisu sieciowego FastAPI z relacyjną bazą danych SQLite

**Temat 59 | Lekcje 121-122**

## Przygotowanie

Środowisko i polecenia uruchamiania opisano w [instrukcji głównej](../README.md#uruchamianie). Przed pracą zainstaluj zależności z dołączonego `requirements.txt` w wybranym środowisku: `py -m pip install -r requirements.txt`.

Utwórz pliki wskazane w zadaniach wewnątrz bieżącego folderu lekcji. Kod uruchamiaj w terminalu z tego folderu. Zadania wprowadzają kolejne zmiany; zachowuj wcześniejsze wersje w podfolderach, jeśli wymaga tego polecenie.

## Wersja z bazą danych

Skopiuj kontrakt API i schematy z tematu 57. Napisz `baza.py`: połączenie SQLite, inicjalizacja tabeli oraz CRUD po ID. `albumy` ma pola: id INTEGER PRIMARY KEY AUTOINCREMENT, tytul TEXT NOT NULL, pobrania INTEGER NOT NULL CHECK(pobrania>=0). Ścieżkę bazy wyznacz względem modułu. Funkcje zapisują parametrami SQL, zatwierdzają operację i zamykają połączenie. Inicjalizacja przez lifespan FastAPI ma tworzyć brakującą tabelę bez usuwania danych.

Użyj `main.py`, `schematy.py`, `baza.py`. Zachowaj statusy z tematu 57 oraz GET /status. Restart nie kasuje danych. Samodzielnie połącz moduły; pełne rozwiązanie nie jest dołączone. Uruchom `py -m uvicorn main:app --reload`.

## Zadanie 1. Trwały zapis

- Zaimplementuj wersję SQLite według kontraktu powyżej i uruchom usługę.
- Dodaj Poranek=120 i Wieczór=80. Zatrzymaj i ponownie uruchom serwer.
- Odczytaj listę. Nie dodawaj danych startowych przy każdym uruchomieniu.

**Wynik kontrolny:** te same dwa rekordy po restarcie.

## Zadanie 2. Parametry i apostrof

- Dodaj album o tytule "Anna's album" i pobrania=0.
- Odczytaj go po ID i sprawdź dokładny tytuł.
- Przejrzyj INSERT i potwierdź osobne przekazanie parametrów.

**Wynik kontrolny:** apostrof zapisany poprawnie, bez błędu SQL.

## Zadanie 3. Brak rekordu

- Wywołaj GET, PUT i DELETE dla ID, którego nie ma w bazie.
- Nie wybieraj ID istniejącego albumu. Sprawdź listę przed i po próbach.

**Wynik kontrolny:** trzy statusy 404, istniejące dane bez zmian.

## Zadanie 4. Transakcja testowa

- W osobnej testowej bazie wykonaj w jednym with db dwa INSERT.
- Pierwszy album ma pobrania=1, drugi pobrania=-1 i narusza CHECK.
- Przechwyć IntegrityError poza with db i odczytaj tabelę.

**Wynik kontrolny:** oba zapisy wycofane, tabela pusta.

## Oddanie pracy

Zachowaj źródła i niezbędne pliki danych. W `testy.md` opisz rzeczywiście wykonane próby: dane, oczekiwany wynik, wynik otrzymany i wniosek. Własną instrukcję uruchomienia zapisz w `URUCHOMIENIE.md`, aby zachować treść zadań w tym README. Dołącz dokumentację wskazaną w poleceniu. Zadania oznaczone jako dodatkowe są dla chętnych.

[Spis lekcji](../README.md)
