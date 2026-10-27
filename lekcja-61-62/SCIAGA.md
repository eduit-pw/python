# Temat 30. Wyjaśnienia do praktyki

## Wzorzec i raw string

r"..." pomaga zapisać backslash we wzorcu bez dodatkowego interpretowania przez napis Pythona. Sam wzorzec opisuje układ znaków, nie znaczenie biznesowe danych.

## fullmatch i search

fullmatch wymaga dopasowania całego napisu. search szuka wystąpienia fragmentu. Walidator kodu powinien odrzucić dopisane znaki, a nie znaleźć poprawny kawałek w środku.

## Klasy znaków i liczności

[0-9] oznacza cyfrę ASCII, {5} dokładnie pięć powtórzeń. \d może obejmować inne cyfry Unicode. Zwykły łącznik wpisany poza klasą jest dosłownym znakiem.

## Grupy i findall

Nawiasy tworzą grupę przechwytującą. findall może zwracać zawartość grup, a nie całe dopasowania. Po wyszukaniu cyfr przekształć wyniki na int do obliczeń.

## Granice walidacji

Wzorzec RRRR-MM-DD sprawdza format. 2026-02-30 nadal może pasować, mimo że nie jest datą. Poprawność kalendarzową sprawdzaj narzędziem do dat.

[Zadania i wyniki kontrolne](README.md)

To uzupełnienie przykładów z prezentacji. Definicje i kontrakty zadań czytaj łącznie. Szczegółowe przykłady są również w tekście prezentacji dołączonym do paczki.
