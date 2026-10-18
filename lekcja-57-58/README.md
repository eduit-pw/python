# Ćwiczenia: Sprawdzanie obecności plików, tworzenie folderów i porządkowanie dysku z poziomu Pythona (os, pathlib)

**Temat 28 | Lekcje 57-58**

## Przygotowanie

Środowisko i polecenia uruchamiania opisano w [instrukcji głównej](../README.md#uruchamianie). Wystarcza biblioteka standardowa Pythona.

Utwórz pliki wskazane w zadaniach wewnątrz bieżącego folderu lekcji. Kod uruchamiaj w terminalu z tego folderu. Zadania wprowadzają kolejne zmiany; zachowuj wcześniejsze wersje w podfolderach, jeśli wymaga tego polecenie.

## Przygotowanie plików

Pracuj wyłącznie na podfolderze `cwiczenia`. Dołączone pliki `cwiczenia/dane/a.txt` i `b.txt` mają odpowiednio zawartość `ABC` i `DE`, bez końcowej nowej linii. W README używamy nazwy `cwiczenia` bez polskich znaków. Utwórz też `cwiczenia/dane/inne`. W zadaniu 3 użyj pliku `dane/liczby.txt` obok własnego skryptu. Przy zapisie i odczycie tekstu używaj UTF-8.

## Zadanie 1. Inwentaryzacja folderu

- Utwórz cwiczenia/dane: a.txt z „ABC”, b.txt z „DE” (oba bez końcowej nowej linii) oraz pusty folder inne.
- Wypisz nazwy zwykłych plików, ich rozszerzenia i rozmiary w bajtach.
- Użyj stat().st_size. Posortuj wynik według nazw.

**Wynik kontrolny:** a.txt: 3 bajty, b.txt: 2 bajty. Folder pominięty.

## Zadanie 2. Kopia tekstów

- Dodaj do danych foto.png jako dowolny plik i podfolder inne/c.txt.
- Skopiuj tylko zwykłe pliki *.txt z danych do cwiczenia/kopie.
- Pomiń plik docelowy, jeśli już istnieje, i wypisz komunikat.

**Wynik kontrolny:** pierwszy przebieg: 2 kopie. Drugi: 2 pominięcia.

## Zadanie 3. Raport niezależny od cwd

- W folderze skryptu utwórz dane/liczby.txt z liczbami 4, 7, -2.
- Zbuduj ścieżkę do tego pliku na podstawie __file__. Oblicz sumę.
- Uruchom skrypt z jego folderu oraz z folderu nadrzędnego.

**Wynik kontrolny:** suma 9 w obu uruchomieniach.

## Zadanie 4. Porządkowanie bez nadpisywania

- W cwiczenia utwórz roboczy.txt i zmień nazwę na gotowy.txt.
- Przed rename sprawdź obecność nazwy docelowej. Przy konflikcie odmów zmiany.
- Sprawdź udaną zmianę, brak źródła i istniejący plik docelowy.

**Wynik kontrolny:** przy konflikcie oba istniejące pliki zachowują zawartość.

## Oddanie pracy

Zachowaj źródła i niezbędne pliki danych. W `testy.md` opisz rzeczywiście wykonane próby: dane, oczekiwany wynik, wynik otrzymany i wniosek. Własną instrukcję uruchomienia zapisz w `URUCHOMIENIE.md`, aby zachować treść zadań w tym README. Dołącz dokumentację wskazaną w poleceniu. Zadania oznaczone jako dodatkowe są dla chętnych.

[Spis lekcji](../README.md)
