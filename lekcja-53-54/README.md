# Organizacja aplikacji w moduły: importowanie funkcji i klas oraz rozdzielenie logiki od interfejsu użytkownika

**Temat 27. Lekcje 53-54. Czas: 90 minut.**

## Po tej lekcji

- Podzielę aplikację na pliki o określonych zadaniach.
- Zaimportuję funkcję lub klasę i wyjaśnię nazwę, pod którą jest dostępna.
- Oddzielę uruchomienie menu od definicji i uruchomię testy.

## Praca w bloku

| Czas | Działanie |
| --- | --- |
| 0–20 min | Prezentacja, krótka demonstracja i pytania teoretyczne. |
| 20–35 min | Zadanie 1 z prowadzącym. |
| 35–55 min | Zadanie 2 w parach lub wspólnie. |
| 55–80 min | Zadanie 3 samodzielnie, kontrola wyniku. |
| 80–90 min | Omówienie, zapis pracy i krótkie pytania. |

Zadanie 4 jest dla osób, które ukończą podstawę wcześniej, albo do samodzielnej kontynuacji. Diagnoza jest materiałem zapasowym i do pracy własnej. Nie jest dodatkowym obowiązkowym etapem bloku.

## Przygotowanie stanowiska

Wystarczy Python 3.8 lub nowszy i edytor, np. VS Code. Używamy biblioteki standardowej. Otwórz ten folder lekcji i utwórz w nim własny katalog `praca`. Każde polecenie wykonuj z katalogu wskazanego przy zadaniu. Na stanowisku, które używa polecenia `python3` albo `py`, zastąp nim `python` we wszystkich przykładach.

Pliki ćwiczeniowe są w [startery](startery/). Krótkie wzorce składni znajdziesz w [KONSTRUKCJE.md](KONSTRUKCJE.md).

## Zadanie 1. Dwa moduły zamiast kopiowania funkcji

1. Otwórz `startery/przeliczniki_jeden_plik.py` i uruchom go. Wynik dla 7 minut to `7 min = 420 s`.
2. W `praca/zadanie1` utwórz pliki `przeliczniki.py` i `main.py`.
3. Do `przeliczniki.py` przenieś funkcje `minuty_na_sekundy` i `opis_czasu`. Zachowaj ich działanie.
4. W `main.py` importuj `opis_czasu`, zdefiniuj `main()` i uruchom ją pod warunkiem `if __name__ == "__main__":`.
5. W terminalu przejdź do `praca/zadanie1` i wykonaj:

```text
python main.py
python -c "import przeliczniki; print(przeliczniki.minuty_na_sekundy(2))"
```

Oczekiwane wyniki: najpierw `7 min = 420 s`, potem `120`. Sam import modułu przelicznika nie ma wypisywać dodatkowych komunikatów. Zakładamy całkowitą liczbę minut.

## Zadanie 2. Model, logika i menu notatnika

1. Otwórz działający program `startery/notatnik_jeden_plik.py`.
2. Utwórz folder `praca/notatnik`, a w nim trzy pliki wskazane w tabeli. Przenieś gotowy kod, zachowując jego działanie.

| Plik | Co ma zawierać? |
| --- | --- |
| `model.py` | Klasa `Notatka`: konstruktor, sprawdzenie niepustej treści i `__str__`. |
| `logika.py` | Import `Notatka` i klasa `Notatnik` z metodami `dodaj` oraz `wszystkie`. |
| `main.py` | Import `Notatnik`, funkcja `main()` i warunek uruchomienia menu. |

3. Pobieranie danych i wypisywanie komunikatów pozostaw w `main.py`. Model i logika mają działać także z testu, bez klawiatury.
4. Z folderu `praca/notatnik` uruchom `python main.py`. Sprawdź pusty notatnik, dodanie tekstu `  Zapisać pliki  `, wyświetlenie notatki i próbę dodania samych spacji.

**Kontrakt:** treść po `.strip()` jest niepusta; błędna treść powoduje `ValueError`. `dodaj()` zwraca dodany obiekt. `wszystkie()` zwraca kopię listy. Odrzucone dodanie nie dopisuje notatki. Używamy argumentów tekstowych.

## Zadanie 3. Testy i import bez uruchomienia menu

1. Skopiuj `startery/test_logika.py` do `praca/notatnik`.
2. Napisz trzy metody `test_...`, każdą z nowym obiektem `Notatnik`:

| Test | Oczekiwanie |
| --- | --- |
| Pusty notatnik | `wszystkie()` zwraca `[]`. |
| Poprawne dodanie | Dla `"  Sprawdzić importy  "` zapisano `"Sprawdzić importy"`, a lista zawiera zwrócony obiekt. |
| Błędne dodanie | Same spacje powodują `ValueError`, a lista nadal jest pusta. |

3. Z folderu `praca/notatnik` wykonaj:

```text
python -m unittest discover -v
python -c "import main; print('Import gotowy')"
```

Oczekuj trzech wykonanych testów i `OK`. Drugie polecenie ma wypisać wyłącznie `Import gotowy`, bez wyświetlania menu. Opcja `-c` wykonuje podany krótki fragment Pythona. Zaobserwuj, że testy importują logikę bez importowania menu.

## Zadanie 4. Dla chętnych: pierwszy pakiet

W osobnym folderze `praca/pakiet` utwórz katalog `notatki` z pustym `__init__.py` oraz plikami `model.py`, `logika.py` i `main.py`. Użyj importów `from notatki.model import Notatka` i `from notatki.logika import Notatnik`. Test umieść w `praca/pakiet/test_logika.py` i popraw jego import.

Z folderu `praca/pakiet` uruchom:

```text
python -m notatki.main
python -m unittest discover -v
```

Wyjaśnij rolę `__init__.py` w tym zwykłym pakiecie oraz znaczenie `-m`. W tym wariancie punktem startowym jest polecenie powyżej, wykonywane z katalogu nadrzędnego wobec `notatki`.

## Diagnoza do samodzielnej pracy

W [diagnoza/napraw.py](diagnoza/napraw.py) użyto `import pomoc`, ale wywołanie funkcji powoduje `NameError`. Zachowaj tę postać importu i popraw wywołanie. Z folderu `diagnoza` uruchom `python sprawdz.py`: ma przejść jeden test. Wyjaśnij, pod jaką nazwą import udostępnił moduł.

## Zakończenie

Pokaż działające menu i wynik trzech testów. W komentarzu w swoim `main.py` zapisz dwa zdania: skąd importujesz logikę i dlaczego import tego pliku nie uruchamia menu. Porównaj kod z [rozwiązaniami](rozwiazania/) po własnej próbie.

## Źródła

- [Python: moduły i pakiety](https://docs.python.org/3/tutorial/modules.html).
- [Python: punkt wejścia __main__](https://docs.python.org/3/library/__main__.html).
- [Python: unittest, discovery i asercje](https://docs.python.org/3/library/unittest.html).

Dostęp: 4 listopada 2026 r. Polecenia i przykłady przygotowano dla tej lekcji.
