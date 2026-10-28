# Ćwiczenia: Wizualne projektowanie wyglądu okna w programie Qt Designer i łączenie go z kodem Pythona

**Temat 40 | Lekcje 81-82**

## Przygotowanie

Środowisko i polecenia uruchamiania opisano w [instrukcji głównej](../README.md#uruchamianie). Przed pracą zainstaluj zależności z dołączonego `requirements.txt` w wybranym środowisku: `py -m pip install -r requirements.txt`.

Utwórz pliki wskazane w zadaniach wewnątrz bieżącego folderu lekcji. Kod uruchamiaj w terminalu z tego folderu. Zadania wprowadzają kolejne zmiany; zachowuj wcześniejsze wersje w podfolderach, jeśli wymaga tego polecenie.

## Specyfikacja formularza

W Qt Designer utwórz formularz typu QWidget. Dodaj QLineEdit o objectName `imieEdit`, QPushButton `powitajButton` i QLabel `wynikLabel`. Ułóż je pionowo w layoucie. QLabel ma początkowo pusty tekst. Zapisz `okno.ui` w folderze projektu. Designer musi być dostępny na stanowisku; sam pakiet PyQt6 nie gwarantuje instalacji programu Designer.

Wariant dynamiczny uruchamiaj przez `py main_load.py`, a generowany przez `py main.py`. Wygeneruj kod poleceniem:

```powershell
py -m PyQt6.uic.pyuic okno.ui -o ui_okno.py
```

Logikę powitania umieść w swojej klasie, a ścieżkę .ui w wariancie loadUi ustal względem pliku skryptu.

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

**Podczas pracy:** korzystaj z [tabel składni i krótkich wzorców](SCIAGA.md). W [starterach](startery/README.md) znajdziesz punkty wyjścia. Pełne polecenia i nazwy docelowych plików są poniżej.

## Zadanie 1. Projekt formularza

- Utwórz w Designer formularz zgodny z powyższą specyfikacją.
- Ustaw tytuł „Powitanie”, przycisk „Powitaj” i pusty wynik.
- Zapisz okno.ui i sprawdź podgląd przy zmianie rozmiaru.

**Wynik kontrolny:** trzy kontrolki w pionowym układzie, poprawne objectName.

## Zadanie 2. Wczytanie i akcja

- Wczytaj okno.ui przez loadUi. Połącz przycisk z funkcją powitania.
- Dla pustego lub białego imienia pokaż „Podaj imię”.
- Dla „ Anna ” pokaż powitanie bez zewnętrznych spacji.

**Wynik kontrolny:** „Witaj, Anna” albo „Podaj imię”.

## Zadanie 3. Wariant generowany

- Wygeneruj ui_okno.py, utwórz własną klasę Okno i dodaj metodę powitaj.
- Zachowaj działanie z zadania 2. Nie modyfikuj pliku generowanego.
- Uruchom program z main.py.

**Wynik kontrolny:** powitanie i kontrola pustego imienia działają jak wcześniej.

## Zadanie 4. Zmiana projektu

- W .ui zmień tekst przycisku na „Pokaż powitanie” i dodaj QLabel „Imię ucznia”.
- Sprawdź program z loadUi, a potem wariant generowany.
- Dla drugiego wariantu ponownie wygeneruj ui_okno.py.

**Wynik kontrolny:** nowy wygląd, własna metoda powitania zachowana.

## Diagnoza i praca domowa

Otwórz [zadanie naprawcze](diagnoza/README.md). Ma własny kontrakt i celowo błędny kod. Wykonaj je na zajęciach lub dokończ w domu zgodnie z ustaleniem prowadzącego.

## Oddanie pracy

Zachowaj źródła i niezbędne pliki danych. W `testy.md` opisz rzeczywiście wykonane próby: dane, oczekiwany wynik, wynik otrzymany i wniosek. Własną instrukcję uruchomienia zapisz w `URUCHOMIENIE.md`, aby zachować treść zadań w tym README. Dołącz dokumentację wskazaną w poleceniu. Zadania oznaczone jako dodatkowe są dla chętnych.

[Spis lekcji](../README.md)
