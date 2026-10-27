# Ćwiczenia: Przygotowanie programu do uruchomienia na innych komputerach: tworzenie pliku wykonywalnego (.exe)

**Temat 48 | Lekcje 99-100**

## Przygotowanie

Środowisko i polecenia uruchamiania opisano w [instrukcji głównej](../README.md#uruchamianie). Przed pracą zainstaluj zależności z dołączonego `requirements.txt` w wybranym środowisku: `py -m pip install -r requirements.txt`.

Utwórz pliki wskazane w zadaniach wewnątrz bieżącego folderu lekcji. Kod uruchamiaj w terminalu z tego folderu. Zadania wprowadzają kolejne zmiany; zachowuj wcześniejsze wersje w podfolderach, jeśli wymaga tego polecenie.

## Projekt wejściowy i polecenia

Użyj własnego działającego projektu z poprzedniej lekcji; wariant .ui pochodzi z tematu 40. Zainstaluj PyInstaller. Polecenia wykonuj z folderu zawierającego main.py, po sprawdzeniu zwykłego `py main.py`.

```powershell
py -m PyInstaller --onedir main.py
py -m PyInstaller --onedir --add-data "okno.ui:." main_load.py
py -m PyInstaller --onefile main.py
```

Drugie polecenie dotyczy wariantu dynamicznie wczytującego .ui i tworzy dist/main_load. W zadaniu 3 wyznacz katalog danych przez `QStandardPaths.AppDataLocation`, po ustawieniu nazwy aplikacji i organizacji; utwórz go przed połączeniem z bazą. Dane trwałe nie mogą trafiać do tymczasowego katalogu rozpakowania onefile. Do odbiorcy przekaż całą paczkę onedir albo właściwy plik onefile, dla użytego systemu i architektury.

## Sposób pracy podczas bloku

| Etap | Czas | Co robisz |
| --- | ---: | --- |
| Wyjaśnienia i demonstracja | 0-25 min | Czytasz przykład, przewidujesz wynik i zadajesz pytania. |
| Zadanie 1 z prowadzącym | 25-35 min | Uruchamiasz pierwszy wariant i objaśniasz kluczowy zapis. |
| Zadanie 2 wspólnie | 35-50 min | Proponujesz kolejne kroki, sam zapisujesz kod. |
| Zadanie 3 samodzielnie | 50-70 min | Realizujesz kontrakt i wykonujesz próby. |
| Zadanie 4 lub diagnoza błędu | 70-85 min | Sprawdzasz przypadki graniczne i poprawiasz program. |
| Zakończenie | 85-90 min | Zapisujesz kod, jeden wniosek i wykonane próby. |

Tempo ustala nauczyciel. Jeśli zadanie 4 jest większe, stanowi kontynuację na kolejnych zajęciach lub zastępuje dodatkową diagnozę. Zadania dodatkowe nie są warunkiem ukończenia podstawowego bloku.

**Przed praktyką:** przeczytaj [ściągę](SCIAGA.md). W [starterach](startery/README.md) znajdziesz punkty wyjścia. Pełne polecenia i nazwy docelowych plików są poniżej.

## Zadanie 1. Paczka onedir

- Sprawdź działanie main.py, potem zbuduj --onedir z widoczną konsolą.
- Skopiuj cały dist/main do nowego folderu testowego.
- Uruchom plik wynikowy z tego folderu. Zanotuj brakujące zasoby lub błędy.

**Wynik kontrolny:** aplikacja działa bez otwartego projektu źródłowego.

## Zadanie 2. Interfejs .ui

- Spakuj formularz z tematu 40, używający loadUi.
- Dołącz okno.ui przez --add-data i odczytuj ścieżkę względem __file__.
- Sprawdź uruchomienie paczki z folderu o innej ścieżce.

**Wynik kontrolny:** formularz ładuje się bez kopiowania .ui ręcznie obok źródeł.

## Zadanie 3. Trwała baza

- W projekcie albumów umieść bazę w AppDataLocation, także przed pakowaniem.
- Dodaj rekord, zamknij program i uruchom go ponownie.
- Zbuduj onefile i powtórz test. Wypisz w URUCHOMIENIE.md faktyczne miejsce bazy.

**Wynik kontrolny:** rekord pozostaje po obu restartach.

## Zadanie 4. Przekazanie odbiorcy

- Przygotuj paczkę onedir lub onefile dla tego samego systemu i architektury.
- Sprawdź start, zapis, odczyt, anulowanie dialogu i brak zasobu.
- Dodaj krótką instrukcję uruchomienia oraz wersje użytych zależności.

**Wynik kontrolny:** odbiorca wie, co uruchomić i gdzie program zapisuje dane.

## Diagnoza i praca domowa

Otwórz [zadanie naprawcze](diagnoza/README.md). Ma własny kontrakt i celowo błędny kod. Wykonaj je na zajęciach lub dokończ w domu zgodnie z ustaleniem prowadzącego.

## Oddanie pracy

Zachowaj źródła i niezbędne pliki danych. W `testy.md` opisz rzeczywiście wykonane próby: dane, oczekiwany wynik, wynik otrzymany i wniosek. Własną instrukcję uruchomienia zapisz w `URUCHOMIENIE.md`, aby zachować treść zadań w tym README. Dołącz dokumentację wskazaną w poleceniu. Zadania oznaczone jako dodatkowe są dla chętnych.

[Spis lekcji](../README.md)
