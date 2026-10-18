# Ćwiczenia: Tworzenie menu programu, paska narzędzi oraz okienek z komunikatami i wyborem pliku

**Temat 44 | Lekcje 89-90**

## Przygotowanie

Środowisko i polecenia uruchamiania opisano w [instrukcji głównej](../README.md#uruchamianie). Przed pracą zainstaluj zależności z dołączonego `requirements.txt` w wybranym środowisku: `py -m pip install -r requirements.txt`.

Utwórz pliki wskazane w zadaniach wewnątrz bieżącego folderu lekcji. Kod uruchamiaj w terminalu z tego folderu. Zadania wprowadzają kolejne zmiany; zachowuj wcześniejsze wersje w podfolderach, jeśli wymaga tego polecenie.

## Pliki projektu

Rozwijaj jeden program `main.py`, zachowując kopie etapów. QAction importuj z `PyQt6.QtGui`. Menu, pasek narzędzi i skrót mają korzystać z tej samej instancji akcji. Anulowanie dialogu rozpoznaj po pustej ścieżce, zanim otworzysz plik. Po nieudanym zapisie zachowaj tekst; po nieudanym odczycie nie zastępuj zawartości edytora.

## Zadanie 1. Menu i skrót

- Utwórz QMainWindow z QTextEdit w obszarze centralnym.
- Dodaj akcję „Wyczyść”, menu „Edycja” i skrót Ctrl+L.
- Obsługa ma wyczyścić tekst. Sprawdź zarówno menu, jak i skrót.

**Wynik kontrolny:** obie drogi wywołują tę samą akcję.

## Zadanie 2. Pasek narzędzi

- Dodaj do zadania 1 QToolBar i tę samą akcję „Wyczyść”.
- Dodaj „O programie”, pokazującą information z tekstem „Edytor 1.0”.
- Sprawdź działanie po kilku użyciach. Nie twórz ponownych połączeń.

**Wynik kontrolny:** jedna akcja czyszczenia, czytelny dialog o programie.

## Zadanie 3. Zapis i anulowanie

- Dodaj akcję „Zapisz” z Ctrl+S oraz dialog zapisu.
- Zapisz tekst „Zażółć gęślą jaźń” jako wynik.txt w UTF-8.
- Powtórz akcję i anuluj dialog. Obsłuż błąd zapisu przez warning.

**Wynik kontrolny:** tekst w pliku jest zgodny, anulowanie nie zmienia pliku.

## Zadanie 4. Otwieranie pliku

- Dodaj akcję „Otwórz”, getOpenFileName i odczyt UTF-8.
- Po sukcesie wstaw odczytany tekst przez setPlainText.
- Sprawdź plik z zadania 3, anulowanie i niedostępny plik.

**Wynik kontrolny:** sukces zmienia pole. Anulowanie lub błąd zachowuje jego treść.

## Oddanie pracy

Zachowaj źródła i niezbędne pliki danych. W `testy.md` opisz rzeczywiście wykonane próby: dane, oczekiwany wynik, wynik otrzymany i wniosek. Własną instrukcję uruchomienia zapisz w `URUCHOMIENIE.md`, aby zachować treść zadań w tym README. Dołącz dokumentację wskazaną w poleceniu. Zadania oznaczone jako dodatkowe są dla chętnych.

[Spis lekcji](../README.md)
