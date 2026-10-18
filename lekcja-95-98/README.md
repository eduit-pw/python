# Ćwiczenia: Projekt programistyczny: budowa kompletnego programu okienkowego z bazą danych i formularzem

**Temat 47 | Lekcje 95-98**

## Przygotowanie

Środowisko i polecenia uruchamiania opisano w [instrukcji głównej](../README.md#uruchamianie). Przed pracą zainstaluj zależności z dołączonego `requirements.txt` w wybranym środowisku: `py -m pip install -r requirements.txt`.

Utwórz pliki wskazane w zadaniach wewnątrz bieżącego folderu lekcji. Kod uruchamiaj w terminalu z tego folderu. Zadania wprowadzają kolejne zmiany; zachowuj wcześniejsze wersje w podfolderach, jeśli wymaga tego polecenie.

## Kontrakt projektu i dane

To blok czterech lekcji. Rozdziel kod na `baza.py`, `walidacja.py`, `okno.py`, `main.py` i testy warstwy danych. Tabela `albumy` ma pola:

| Pole | Warunek |
| --- | --- |
| id | INTEGER PRIMARY KEY AUTOINCREMENT |
| artysta | Niepusty tekst po strip |
| tytul | Niepusty tekst po strip |
| rok | Całkowity, od 1900 do 2100 |
| pobrania | Całkowite, >= 0 |

W SQL użyj NOT NULL i CHECK dla pól liczbowych, w Pythonie waliduj teksty przed zapisem. W `walidacja.przygotuj(...)` zwracaj oczyszczone dane lub zgłaszaj ValueError; błąd nie może częściowo zmienić rekordu. Inicjalizacja nie nadpisuje istniejącej bazy.

| Artysta | Tytuł | Rok | Pobrania |
| --- | --- | ---: | ---: |
| Zespół Północ | Poranek | 2024 | 120 |
| Anna Nowak | Wieczór | 2023 | 80 |

Wynik początkowy: dwa rekordy i suma 200. Nowy album „Noc” z 0 pobrań nie zmienia tej sumy. Przy filtrowaniu „por” tabela zawiera Poranek, a suma wynosi 120. Potwierdź trwałość po ponownym uruchomieniu, niezależność ID od sortowania i brak zmian po anulowaniu usunięcia. Dodaj testy walidacji oraz odczytu/zapisu na osobnej bazie.

## Etap 1. Baza i odczyt

- Utwórz tabelę albumy zgodną z umową pól.
- Przygotuj funkcje odczytu oraz dodawania, z parametrami SQL.
- Zapisz dwa rekordy kontrolne z powyższej tabeli i odczytaj je w tabeli.
- Nie dodawaj danych przykładowych przy każdym uruchomieniu.

**Punkt kontrolny:** restart aplikacji zachowuje dokładnie dwa rekordy.

## Etap 2. Formularz dodawania

- Dodaj pola wykonawcy, tytułu, roku i pobrań oraz przycisk „Dodaj”.
- Sprawdź dane w funkcji walidującej, zanim rozpoczniesz zapis.
- Po sukcesie odśwież tabelę i wyczyść pola tekstowe.
- Po błędzie pokaż komunikat i zachowaj wprowadzone dane.

**Punkt kontrolny:** pusty tytuł nie zmienia liczby rekordów.

## Etap 3. Wybór, edycja i usuwanie

- Zaznaczenie wiersza przenosi dane rekordu do formularza i zapamiętuje jego ID.
- Przycisk „Zapisz zmiany” aktualizuje wybrany rekord po ID.
- Przycisk „Usuń” pyta o potwierdzenie, a potem usuwa rekord po ID.
- Po usunięciu wyczyść wybór. Bez wyboru pokaż komunikat.

**Punkt kontrolny:** odwrócenie sortowania nie zmienia tożsamości rekordu.

## Etap 4. Filtr i kompletność programu

- Filtr tytułu działa bez rozróżniania wielkości liter ASCII.
- Pusty filtr pokazuje wszystkie albumy. „por” pokazuje Poranek.
- Brak dopasowań daje pustą tabelę i nie usuwa rekordów z bazy.
- Dodaj widoczną sumę pobrań rekordów pokazanych po filtrowaniu. Filtr potraktuj jako dosłowny fragment. Znaki % i _ nie mają być wildcardami.

## Oddanie pracy

Zachowaj źródła i niezbędne pliki danych. W `testy.md` opisz rzeczywiście wykonane próby: dane, oczekiwany wynik, wynik otrzymany i wniosek. Własną instrukcję uruchomienia zapisz w `URUCHOMIENIE.md`, aby zachować treść zadań w tym README. Dołącz dokumentację wskazaną w poleceniu. Zadania oznaczone jako dodatkowe są dla chętnych.

[Spis lekcji](../README.md)
