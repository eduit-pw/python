# Ćwiczenia: Praca z datą i czasem: formatowanie, obliczanie różnic czasowych oraz filtrowanie danych (moduł datetime)

**Temat 38 | Lekcje 77-78**

## Przygotowanie

Środowisko i polecenia uruchamiania opisano w [instrukcji głównej](../README.md#uruchamianie). Wystarcza biblioteka standardowa Pythona.

Utwórz pliki wskazane w zadaniach wewnątrz bieżącego folderu lekcji. Kod uruchamiaj w terminalu z tego folderu. Zadania wprowadzają kolejne zmiany; zachowuj wcześniejsze wersje w podfolderach, jeśli wymaga tego polecenie.

## Zadanie 1. Termin za dwa tygodnie

- Utwórz date dla 2026-10-03 i dodaj 14 dni.
- Wypisz termin w ISO i w formacie DD.MM.RRRR.
- Sprawdź przejście roku: dodaj 2 dni do 2026-12-31.

**Wynik kontrolny:** 2026-10-17, 17.10.2026 oraz 2027-01-02.

## Zadanie 2. Wczytanie daty

- Wczytaj napis DD.MM.RRRR przez input i użyj strptime.
- Wypisz poprawną datę w ISO. Przy ValueError pokaż komunikat.
- Sprawdź 29.02.2024, 29.02.2025 oraz 31.04.2026.

**Wynik kontrolny:** tylko 29.02.2024 jest poprawna.

## Zadanie 3. Czas trwania

- Oblicz czas między 2026-10-03 23:30 a 2026-10-04 01:00.
- Dane traktuj jako wspólny czas lokalny bez tzinfo.
- Wypisz liczbę minut przez total_seconds(). Sprawdź też równe chwile.

**Wynik kontrolny:** 90 minut oraz 0 minut.

## Zadanie 4. Rekordy z października

- Użyj dat: 2026-09-30, 2026-10-01, 2026-10-31, 2026-11-01.
- Zamień napisy na date. Wybierz poczatek <= data < koniec.
- Początek: 2026-10-01. Koniec: 2026-11-01. Wypisz wybrane daty.

**Wynik kontrolny:** 2026-10-01 oraz 2026-10-31.

## Oddanie pracy

Zachowaj źródła i niezbędne pliki danych. W `testy.md` opisz rzeczywiście wykonane próby: dane, oczekiwany wynik, wynik otrzymany i wniosek. Własną instrukcję uruchomienia zapisz w `URUCHOMIENIE.md`, aby zachować treść zadań w tym README. Dołącz dokumentację wskazaną w poleceniu. Zadania oznaczone jako dodatkowe są dla chętnych.

[Spis lekcji](../README.md)
