# Ćwiczenia: Zapisywanie i odczytywanie danych z lokalnej bazy danych SQLite w aplikacji okienkowej (sqlite3)

**Temat 46 | Lekcje 93-94**

## Przygotowanie

Środowisko i polecenia uruchamiania opisano w [instrukcji głównej](../README.md#uruchamianie). Przed pracą zainstaluj zależności z dołączonego `requirements.txt` w wybranym środowisku: `py -m pip install -r requirements.txt`.

Utwórz pliki wskazane w zadaniach wewnątrz bieżącego folderu lekcji. Kod uruchamiaj w terminalu z tego folderu. Zadania wprowadzają kolejne zmiany; zachowuj wcześniejsze wersje w podfolderach, jeśli wymaga tego polecenie.

## Schemat bazy i podział kodu

Przygotuj `baza.py` dla operacji SQL i `main.py` dla okna. Baza `albumy.db` jest plikiem roboczym obok skryptu. Tabela `albumy`: `id INTEGER PRIMARY KEY`, `tytul TEXT NOT NULL`, `rok INTEGER NOT NULL CHECK(rok BETWEEN 1900 AND 2100)`. Tytuł po strip nie może być pusty. Używaj parametrów `?`, zatwierdzaj transakcje i zamykaj połączenia. Inicjalizacja tabeli ma być idempotentna. Dane początkowe dodawaj jednorazowo, nie przy każdym odczycie.

Próbę wycofania wykonaj w oddzielnej pustej bazie testowej, np. `:memory:`; przygotowanie tabeli zatwierdź przed transakcją z dwoma INSERT. Nie testuj błędnych transakcji na własnych danych użytkowych.

## Zadanie 1. Utwórz i odczytaj bazę

- Utwórz nową albumy.db z tabelą opisaną powyżej.
- Dodaj parametrami dwa albumy: (Poranek,2024), (Wieczór,2023).
- Wypisz id, tytuł i rok, uporządkowane po id. Uruchom osobno sam odczyt.

**Wynik kontrolny:** 2 trwałe rekordy. Odczyt nie dopisuje nowych.

## Zadanie 2. Formularz dodawania

- Zbuduj QLineEdit tytułu, QSpinBox 1900-2100 i przycisk „Dodaj”.
- Po poprawnym zapisie odśwież QTableWidget. Odrzuć pusty tytuł.
- Dodaj tytuł „Anna's album”, aby sprawdzić przekazanie apostrofu jako danych.

**Wynik kontrolny:** apostrof zapisany poprawnie, pusty tytuł nie tworzy rekordu.

## Zadanie 3. Zmiana i usunięcie po ID

- Dodaj obsługę zaznaczonego rekordu: zmień jego tytuł, potem usuń go.
- Wykonuj SQL po id, nie po numerze wiersza ani po tytule.
- Sprawdź próbę operacji bez zaznaczenia i po sortowaniu tabeli.

**Wynik kontrolny:** zmienia się tylko wskazany rekord, brak wyboru daje komunikat.

## Zadanie 4. Wycofanie transakcji

- W nowej testowej bazie wykonaj w jednym with db dwa INSERT.
- Pierwszy: (Dobry,2024). Drugi: (Błędny,1800), naruszający CHECK.
- Przechwyć IntegrityError poza with db i odczytaj tabelę.

**Wynik kontrolny:** tabela pusta. Cała transakcja została wycofana.

## Oddanie pracy

Zachowaj źródła i niezbędne pliki danych. W `testy.md` opisz rzeczywiście wykonane próby: dane, oczekiwany wynik, wynik otrzymany i wniosek. Własną instrukcję uruchomienia zapisz w `URUCHOMIENIE.md`, aby zachować treść zadań w tym README. Dołącz dokumentację wskazaną w poleceniu. Zadania oznaczone jako dodatkowe są dla chętnych.

[Spis lekcji](../README.md)
