# Ćwiczenia: Sprawdzanie poprawności wpisów tekstowych za pomocą wyrażeń regularnych (moduł re)

**Temat 30 | Lekcje 61-62**

## Przygotowanie

Środowisko i polecenia uruchamiania opisano w [instrukcji głównej](../README.md#uruchamianie). Wystarcza biblioteka standardowa Pythona.

Utwórz pliki wskazane w zadaniach wewnątrz bieżącego folderu lekcji. Kod uruchamiaj w terminalu z tego folderu. Zadania wprowadzają kolejne zmiany; zachowuj wcześniejsze wersje w podfolderach, jeśli wymaga tego polecenie.

## Zadanie 1. Kod z łącznikiem

- Napisz funkcję poprawny_kod(tekst) zwracającą bool.
- Wymagaj dokładnie formatu NN-NNN i cyfr ASCII.
- Sprawdź: 12-345, 12345, 12-345x, 1a-345 oraz pusty napis.

**Wynik kontrolny:** tylko 12-345 daje True.

## Zadanie 2. Pięć cyfr

- Przygotuj walidację formatu uproszczonego: dokładnie pięć cyfr ASCII.
- Sprawdź 12345, 12-345, 1234, 12a45 oraz napis "\uFF11\uFF12\uFF13\uFF14\uFF15".
- Wyjaśnij, dlaczego nie używasz wzorca z łącznikiem. Adaptacja INF.04-01-23.06-SG, II: sama funkcja walidująca.

**Wynik kontrolny:** tylko 12345 daje True.

## Zadanie 3. Identyfikatory w tekście

- Dla „Zgłoszenia: ID-12, ID-7, ID-305.” znajdź wszystkie numery po „ID-”.
- Użyj jednej grupy przechwytującej i findall.
- Zamień wyniki na int i oblicz ich sumę.

**Wynik kontrolny:** [12, 7, 305], suma 324.

## Zadanie 4. Format daty

- Sprawdź fullmatch dla RRRR-MM-DD: 2026-10-03, 2026-02-30 i 26-10-03.
- Wymagaj 4, 2 i 2 cyfr, rozdzielonych łącznikami.
- Wskaż przykład, który pasuje do wzorca, lecz nie jest datą kalendarzową.

**Wynik kontrolny:** dwa pierwsze pasują. 2026-02-30 wymaga dalszej kontroli.

## Oddanie pracy

Zachowaj źródła i niezbędne pliki danych. W `testy.md` opisz rzeczywiście wykonane próby: dane, oczekiwany wynik, wynik otrzymany i wniosek. Własną instrukcję uruchomienia zapisz w `URUCHOMIENIE.md`, aby zachować treść zadań w tym README. Dołącz dokumentację wskazaną w poleceniu. Zadania oznaczone jako dodatkowe są dla chętnych.

[Spis lekcji](../README.md)
