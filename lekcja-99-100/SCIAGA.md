# Temat 48. Wyjaśnienia do praktyki

## Pakowanie aplikacji

PyInstaller zbiera interpreter, moduły i zasoby. onedir tworzy katalog paczki, onefile pojedynczy plik z rozpakowaniem przy starcie. Buduj dla docelowego systemu i architektury.

## Diagnostyka

Najpierw sprawdź zwykłe uruchomienie źródeł. W pierwszej paczce zachowaj konsolę, aby odczytać błąd startu. Przetestuj z katalogu innego niż źródłowy.

## Zasoby i add-data

Plik .ui musi zostać dołączony jawnie. Ścieżkę zasobu wyznacz względem modułu. Nie zakładaj, że odbiorca ma Twoje foldery i bezwzględne ścieżki.

## Dane użytkownika

Baza i ustawienia wymagają trwałego, zapisywalnego katalogu. Tymczasowy katalog onefile nie jest miejscem trwałej bazy. AppDataLocation wskazuje lokalizację danych aplikacji.

## Przekazanie

Dla onedir przekaż cały katalog, nie sam plik .exe. Sprawdź start, zapis, restart i odczyt na oddanej kopii. Zapisz wersje oraz miejsce przechowywania danych.

[Zadania i wyniki kontrolne](README.md)

To uzupełnienie przykładów z prezentacji. Definicje i kontrakty zadań czytaj łącznie. Szczegółowe przykłady są również w tekście prezentacji dołączonym do paczki.
