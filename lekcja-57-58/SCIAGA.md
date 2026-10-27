# Temat 28. Wyjaśnienia do praktyki

## Path i operator /

Path reprezentuje ścieżkę. baza / "dane" / "plik.txt" łączy jej części, ale nie tworzy pliku ani folderu. Nie sklejaj separatorów systemowych ręcznie.

## Kotwica __file__

Path(__file__).resolve().parent wskazuje folder skryptu. Budowanie ścieżek od tej kotwicy pozwala uruchomić program z innego katalogu. cwd oznacza katalog procesu, niekoniecznie skryptu.

## Sprawdzenie zasobu

exists sprawdza obecność, is_file zwykły plik, is_dir folder. Stan może się zmienić po sprawdzeniu, dlatego sama operacja odczytu lub zapisu nadal wymaga obsługi błędu.

## Przeglądanie i metadane

iterdir zwraca wpisy bez rekurencji, glob wybiera wzorzec. suffix daje rozszerzenie, name nazwę, stat().st_size rozmiar w bajtach. Sortowanie ustala kolejność raportu.

## Tworzenie i zmiana

mkdir(parents=True, exist_ok=True) przygotowuje foldery. rename zmienia ścieżkę lub nazwę. Przed operacją kontroluj konflikt i zachowaj cudze dane. Nie zakładaj identycznego nadpisywania na wszystkich systemach.

[Zadania i wyniki kontrolne](README.md)

To uzupełnienie przykładów z prezentacji. Definicje i kontrakty zadań czytaj łącznie. Szczegółowe przykłady są również w tekście prezentacji dołączonym do paczki.
