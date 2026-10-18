# Ćwiczenia: Projekt programistyczny: samodzielne stworzenie aplikacji obiektowej wraz z testami i dokumentacją

**Temat 26 | Lekcje 51-54**

## Przygotowanie

Środowisko i polecenia uruchamiania opisano w [instrukcji głównej](../README.md#uruchamianie). Wystarcza biblioteka standardowa Pythona.

Utwórz pliki wskazane w zadaniach wewnątrz bieżącego folderu lekcji. Kod uruchamiaj w terminalu z tego folderu. Zadania wprowadzają kolejne zmiany; zachowuj wcześniejsze wersje w podfolderach, jeśli wymaga tego polecenie.

### Architektura i kontrakty

| Plik | Odpowiedzialność |
|---|---|
| `notatka.py` | Dane pojedynczej notatki, nadawanie ID, dwie metody wyświetlające. |
| `demo_cke.py` | Demonstracja dwóch obiektów zgodna z rdzeniem konsolowym arkusza. |
| `notatnik.py` | Własna lista obiektów, walidacja, dodawanie i wyszukiwanie; bez `input` i `print`. |
| `main.py` | Menu, pobieranie danych, konwersja ID, komunikaty i obsługa spodziewanych błędów. |
| `test_notatka.py`, `test_notatnik.py` | Testy bez klikania i ręcznego wpisywania danych. |

`Notatnik` zawiera obiekty `Notatka` - to kompozycja. Nie dziedziczy po notatce: zbiór notatek nie jest pojedynczą notatką.

| Operacja | Wynik i warunki |
|---|---|
| `Notatka(tytul, tresc)` | Dwa napisy przekazane przez poprawnie używany program. Przypisuje je bez zmieniania zawartości. Inkrementuje wspólny licznik i nadaje ID. Walidację projektu wykonuje `Notatnik.dodaj`. |
| `wyswietl()` | Wypisuje tytuł i treść w osobnych wierszach; zwraca `None`. |
| `diagnostyka()` | Wypisuje `ID; bieżący licznik; tytuł; treść`; zwraca `None`. |
| `id`, `tytul`, `tresc` | Publiczny odczyt przez właściwości; bez możliwości przypisania do tych właściwości. |
| `Notatka.liczba_notatek()` | Liczba wszystkich utworzonych notatek w tym procesie, także z różnych notatników i podklas. Nie jest długością konkretnej listy. |
| `Notatnik.dodaj(tytul, tresc)` | Wymaga obydwu wartości typu `str` (`TypeError` w innym przypadku). Pusty tytuł lub same białe znaki: `ValueError`. Pusta treść jest dozwolona. Najpierw sprawdza, następnie tworzy i dopisuje obiekt; zwraca ten obiekt. |
| `wszystkie()` | Nowa lista zawierająca referencje do tych samych obiektów, w kolejności dodania. `clear()` na zwróconej liście nie kasuje listy menedżera. To kopia płytka. |
| `znajdz(identyfikator)` | Wymaga dokładnie typu `int`; `bool` i inne typy: `TypeError`. ID ≤ 0: `ValueError`. Zwraca istniejący obiekt albo `None`. |
| `szukaj(fragment)` | Wymaga `str`; inny typ: `TypeError`. Pusty lub wyłącznie biały fragment: `ValueError`. Wyszukiwanie podciągu w tytule przez `.lower()`, w kolejności dodania; zwraca listę, również pustą. |

Walidacja używa `.strip()` wyłącznie do rozpoznania wartości pustej. Nie usuwa spacji z zapisanego tytułu ani z niepustego fragmentu. Na przykład `" py "` szuka właśnie tego podciągu, z odstępami. `.lower()` wystarcza do przedstawionych przykładów; nie deklarujemy pełnej obsługi wszystkich językowych reguł porównania Unicode.

### Cztery etapy - treść dla uczniów

## Założenia projektu

Pracuj na danych przechowywanych w pamięci; po zamknięciu programu notatki znikają. W klasie `Notatka` nazwij prywatne pola `__licznik_notatek` i `__identyfikator`; pola tekstowe to `_tytul` i `_tresc`. Początkowa wartość licznika to 0. Wspólny licznik obejmuje obiekty utworzone także przez podklasy. Projekt rozdziel na pliki według poniższej tabeli.

## Etap 1. Model i demonstracja dwóch notatek

1. Utwórz katalog projektu i pliki `notatka.py`, `demo_cke.py`.
2. Zaimplementuj klasę według tabeli: wspólny licznik początkowo 0, ID oraz dwa pola tekstowe. Zachowaj rozróżnienie dostępu wynikające z arkusza.
3. W konstruktorze zwiększ licznik, nadaj ID i przypisz parametry. Napisz `wyswietl` oraz `diagnostyka`, bez dodatkowych argumentów i wartości zwracanej.
4. W demonstracji utwórz najpierw obie notatki: `("Zakupy", "Kup mleko")` oraz `("Python", "Powtórz klasy")`. Potem wywołaj obie metody dla każdej.
5. Dopisz komentarz nad klasą zgodnie z częścią III arkusza. Autor: na lekcji identyfikator ustalony przez nauczyciela; na egzaminie numer zdającego zgodnie z arkuszem.
6. Na potrzeby dalszego projektu dodaj publiczne właściwości odczytu i metodę liczby notatek. Są to rozszerzenia lekcji.

Oczekiwany wynik `python demo_cke.py` w **nowym procesie**:

```text
Diagnostyka: ID; licznik; tytuł; treść
Zakupy
Kup mleko
1; 2; Zakupy; Kup mleko
Python
Powtórz klasy
2; 2; Python; Powtórz klasy
```

Pierwsze ID nie zmienia się po utworzeniu kolejnych notatek; wspólny licznik rośnie. W metodach bezparametrowych `self` jest technicznym parametrem instancji, a wywołujący nie podaje dodatkowego argumentu.

## Etap 2. Menedżer i menu

1. Utwórz `notatnik.py`. Lista `_notatki` powstaje w `__init__` i należy do konkretnego menedżera.
2. Zaimplementuj `dodaj`, `wszystkie`, `znajdz` i `szukaj` zgodnie z kontraktami. Do wyszukiwania użyj zwykłej pętli `for`.
3. Sprawdzaj dane **przed** utworzeniem `Notatka`, aby błędna próba nie zmieniła listy ani licznika.
4. W `main.py` utwórz jedną instancję `Notatnik` i pętlę menu: 1 - dodaj, 2 - lista, 3 - ID, 4 - szukaj, 0 - koniec.
5. Wyszukiwanie po ID poprzedź konwersją `int`. Obsługuj `TypeError` i `ValueError` w interfejsie; po błędzie program wraca do menu.
6. Pokaż zrozumiałe komunikaty dla pustej listy, braku wyników i nieznanej opcji. Nie stosuj samego `except` ani przechwytywania każdego możliwego wyjątku.

Przykład w nowym uruchomieniu: dodaj `Python / Powtórz klasy`, następnie `Zakupy / Kup mleko`. Wyszukanie `pYt` zwraca pierwszą notatkę (ID 1), a ID 99 - komunikat o braku. Próba dodania tytułu `"   "` zgłasza błąd; kolejna poprawna notatka otrzymuje ID 3, a nie 4.

**Szkielet wspierający** (pojedyncza metoda do uzupełnienia, nie pełny program):

```python
def szukaj(self, fragment):
    # 1. Sprawdz typ i wartosc fragmentu.
    # 2. Utworz pusta liste wynikow.
    # 3. Przejdz po self._notatki.
    # 4. Porownaj fragment i tytul po lower().
    # 5. Zwroc wyniki.
    pass
```

## Etap 3. Testy i poprawianie usterek

1. Utwórz dwie klasy testowe w plikach `test_notatka.py` i `test_notatnik.py`.
2. Przygotuj niezależny stan w `setUp`; po teście posprzątaj w `tearDown`.
3. Zrealizuj **co najmniej 12 poniższych przypadków**. Możesz połączyć powiązane sprawdzenia w metodzie testowej albo rozdzielić je na kilka metod. Liczba przypadków i liczba metod testowych nie muszą być równe.
4. Do wyjścia `print` użyj `StringIO` i `redirect_stdout`; dla wartości, tożsamości i wyjątków dobierz odpowiednią asercję.
5. Uruchom `python -m unittest discover -v`, przeanalizuj ewentualny `FAIL` lub `ERROR`, popraw przyczynę i uruchom ponownie.

| Nr | Próba | Oczekiwany rezultat |
|---|---|---|
| 1 | Dwa obiekty w nowym stanie | ID 1 i 2; wspólny licznik 2. |
| 2 | Diagnostyka pierwszego po utworzeniu drugiego | `1; 2; Zakupy; Kup mleko` i znak nowego wiersza. |
| 3 | `wyswietl` | Tytuł i treść w oddzielnych wierszach. |
| 4 | Pusty menedżer | `wszystkie()` zwraca `[]`. |
| 5 | Dodanie dwóch notatek | Zachowana kolejność i dane obiektów. |
| 6 | Pusty tytuł i same spacje | `ValueError`; lista i licznik niezmienione. |
| 7 | Poprawna próba po odrzuconej | Kolejne ID bez luki wywołanej odrzuceniem. |
| 8 | Istniejące ID i ID 99 | Ten sam obiekt albo `None`. |
| 9 | ID 0, -1, napis `"1"` | `ValueError` dla niedodatnich; `TypeError` dla napisu. |
| 10 | Tytuły `Python`, `Zakupy`, `Testy PYTHON`; fragment `pYt` | Pierwszy i trzeci obiekt, w tej kolejności. |
| 11 | Fragment bez wyników oraz pusty fragment | Odpowiednio `[]` i `ValueError`. |
| 12 | `clear()` na wyniku `wszystkie()` | Wewnętrzna lista menedżera zachowana. |

**Uwaga o izolacji:** nowa instancja `TestCase` nie resetuje automatycznie licznika innej klasy. W testach świadomie używamy `Notatka._Notatka__licznik_notatek = 0`. To kontrolowany wyjątek na potrzeby przygotowania stanu, nie wzorzec dostępu w aplikacji. Testy uruchamiamy sekwencyjnie. Reset po teście zapobiega pozostawieniu stanu. Nie dodajemy publicznego resetowania ID do produkcyjnego programu.

`OK` oznacza przejście wykonanych przypadków. Nie dowodzi braku wszystkich możliwych błędów ani kompletności projektu.

## Etap 4. Dokumentacja i przekazanie projektu

1. Zapisz `URUCHOMIENIE.md`: cel, pliki, sposób uruchomienia, funkcje menu, zasady danych i ograniczenie pamięciowe.
2. W `testy.md` opisz co najmniej sześć rzeczywiście wykonanych prób konsoli z tabeli poniżej; wpisz oczekiwany i rzeczywisty rezultat oraz wniosek. Dopisz wynik własnego zestawu `unittest`.
3. W `opis_srodowiska.md` wpisz rzeczywisty system, edytor/IDE i wynik `python --version`. Nie kopiuj przykładowej wersji jako własnej.
4. Wykonaj zrzut demonstracji dwóch notatek, działania menu oraz wyniku testów. Na potrzeby ćwiczenia wzoru z tego arkusza zachowaj cały ekran z paskiem zadań. Podczas egzaminu format i nazwy dokumentacji dobieraj do jego aktualnej treści.
5. Zrób kopię lub archiwum pełnego projektu, otwórz je w nowym katalogu i uruchom demonstrację, menu oraz testy z jego wnętrza.
6. Uzupełnij dokumentację wynikiem tej próby. Jeżeli coś nie działa, zapisz problem i popraw projekt.

| Próba konsoli | Oczekiwanie |
|---|---|
| Lista przed dodaniem | `Brak notatek.` |
| Dodanie `Python / Powtórz klasy` | Potwierdzenie ID 1 w nowym procesie. |
| Szukanie `pYt` | Wyświetlenie dodanej notatki. |
| Szukanie ID 99 | `Nie znaleziono notatki.` |
| Tytuł z samymi spacjami, potem poprawna notatka | Komunikat błędu, potem ID 2. |
| ID wpisane jako `abc`, następnie wybór 0 | Komunikat konwersji, powrót do menu, zakończenie. |

Proponowane pliki końcowe: cztery moduły aplikacji, dwa pliki testów, `README.md`, `testy.md`, `opis_srodowiska.md` i zrzuty w `dokumentacja/`. Dodatkowy `pilna.py` tylko po wykonaniu rozszerzenia. Pełne archiwum ma zawierać pliki potrzebne do uruchomienia; nie opieraj go na bezwzględnych ścieżkach do własnego komputera.

## Zadanie 5. Dla chętnych: pilna notatka

Dodaj `NotatkaPilna(Notatka)`. Nadpisz tylko `wyswietl()`, aby wypisać `[PILNE]` i tytuł w jednym wierszu, a treść w następnym. Odczytaj `_tytul` i `_tresc`. Inicjalizacja, ID i licznik zachowują działanie klasy bazowej.

W osobnym `pilna.py` utwórz zwykłą notatkę `("Zakupy", "Kup mleko")` oraz pilną `("Projekt", "Oddaj jutro")`. Wywołaj wyswietl w jednej pętli i wypisz `Notatka.liczba_notatek()`. W nowym procesie oczekuj:

```text
Zakupy
Kup mleko
[PILNE] Projekt
Oddaj jutro
Licznik: 2
```

Nie musisz dodawać wyboru pilnej notatki do menu.

## Oddanie pracy

Zachowaj źródła i niezbędne pliki danych. W `testy.md` opisz rzeczywiście wykonane próby: dane, oczekiwany wynik, wynik otrzymany i wniosek. Własną instrukcję uruchomienia zapisz w `URUCHOMIENIE.md`, aby zachować treść zadań w tym README. Dołącz dokumentację wskazaną w poleceniu. Zadania oznaczone jako dodatkowe są dla chętnych.

[Spis lekcji](../README.md)
