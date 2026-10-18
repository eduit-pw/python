# Ćwiczenia: Organizacja stanowiska komputerowego, szkolenie BHP i regulamin pracowni. Wprowadzenie do języka Python i wirtualne środowiska (venv)

**Temat 1 | Lekcje 1-2**

## Przygotowanie

Środowisko i polecenia uruchamiania opisano w [instrukcji głównej](../README.md#uruchamianie). Wystarcza biblioteka standardowa Pythona.

Utwórz pliki wskazane w zadaniach wewnątrz bieżącego folderu lekcji. Kod uruchamiaj w terminalu z tego folderu. Zadania wprowadzają kolejne zmiany; zachowuj wcześniejsze wersje w podfolderach, jeśli wymaga tego polecenie.

## Zadanie 1. Stanowisko i folder projektu

1. Ustaw krzesło, klawiaturę i monitor; sprawdź przejście przy stanowisku.
2. Wskaż, komu i w jaki sposób zgłosisz uszkodzony przewód lub inne zagrożenie.
3. Utwórz folder `temat01` w miejscu wskazanym przez nauczyciela.
4. Otwórz go w VS Code, otwórz terminal i sprawdź `py --version`.

W razie usterki, braku uprawnień lub niedziałającego polecenia zgłoś problem nauczycielowi. Nie naprawiaj sprzętu i nie instaluj programu samodzielnie.

## Zadanie 2. Pierwszy program

1. Utwórz `hello.py` i dodaj komentarz z tematem lekcji.
2. Wyświetl, w trzech osobnych liniach:

   ```text
   Cześć, Python!
   To mój pierwszy program.
   Program działa.
   ```

3. Zapisz plik i uruchom go przez `py hello.py` w terminalu.
4. Zmień drugi komunikat na `Uczę się programowania.`, zapisz i uruchom ponownie.

## Zadanie 3. Naprawa trzech fragmentów

Każdy poniższy fragment jest **osobnym przypadkiem**. Sprawdzaj je kolejno w `poprawa.py`: najpierw zobacz komunikat błędu, następnie popraw kod i uruchom. Nie łącz trzech błędów w jeden program.

**A.**

```python
print("Program działa."
```

**B.**

```python
Print("Program działa.")
```

**C.**

```python
print(Program działa.)
```

Za każdym razem poprawny wynik ma brzmieć `Program działa.`. Nazwij pomyłkę własnymi słowami. Po zakończeniu pozostaw w `poprawa.py` poprawną wersję.

## Zadanie 4. Środowisko i dokumentacja programu

1. W folderze `temat01` utwórz `.venv` poleceniem `py -m venv .venv`.
2. Wybierz ten interpreter w VS Code.
3. Uruchom zmieniony `hello.py` przez `.\.venv\Scripts\python.exe hello.py`.
4. Porównaj wynik z zadaniem 2 po zmianie.
5. Utwórz w `temat01` folder `dokumentacja` i zapisz zrzut jako `uruchomienie.png`. Zrzut ma przedstawiać polecenie z jawną ścieżką i wynik. Może też pokazywać kod; zadbaj o jego czytelność.
6. Utwórz `URUCHOMIENIE.md`: podaj rzeczywistą wersję Pythona, nazwę pliku oraz polecenia utworzenia środowiska i uruchomienia programu.

## Zadanie 5. Dla chętnych: Uruchomienie kopii - dodatkowe

1. Utwórz osobny folder `temat01_kopia` obok `temat01`.
2. Skopiuj do niego `hello.py`, `URUCHOMIENIE.md` i folder `dokumentacja`. Nie kopiuj `.venv`.
3. Otwórz folder kopii, utwórz tam nowe środowisko i wybierz jego interpreter.
4. Uruchom program według URUCHOMIENIE.md. Wynik ma być taki sam.

## Oddanie pracy

Zachowaj źródła i niezbędne pliki danych. W `testy.md` opisz rzeczywiście wykonane próby: dane, oczekiwany wynik, wynik otrzymany i wniosek. Własną instrukcję uruchomienia zapisz w `URUCHOMIENIE.md`, aby zachować treść zadań w tym README. Dołącz dokumentację wskazaną w poleceniu. Zadania oznaczone jako dodatkowe są dla chętnych.

[Spis lekcji](../README.md)
