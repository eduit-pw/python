# Temat 25. Wyjaśnienia do praktyki

## Singleton

Singleton zwraca tę samą instancję przy kolejnych wywołaniach klasy. __new__ odpowiada za tworzenie, __init__ może działać ponownie. Nie zeruj zmienionych ustawień przy każdym wywołaniu.

## Metoda wytwórcza

Twórca korzysta z utworz(), a podklasa wybiera klasę produktu. Wspólna operacja pracuje przez interfejs produktu. Dodanie nowego produktu nie powinno wymagać if po typach we wspólnej operacji.

## Dekorator funkcji

Dekorator przyjmuje funkcję i zwraca funkcję opakowującą. @loguj nad def jest skrótem zastosowania dekoratora do tej funkcji. Nie wykonuj funkcji w momencie dekorowania bez potrzeby.

## Argumenty i wynik

Opakowanie przekazuje *args i **kwargs oraz zwraca wynik wywołania. Brak return gubi wynik. functools.wraps pomaga zachować nazwę i docstring funkcji.

## Oddzielenie rozszerzenia

Czysta funkcja obliczeniowa zachowuje wymagany kontrakt bez I/O. Logowanie dołącz jako osobne opakowanie. Testuj sukces, wyjątek, argumenty nazwane i metadane.

[Zadania i wyniki kontrolne](README.md)

To uzupełnienie przykładów z prezentacji. Definicje i kontrakty zadań czytaj łącznie. Szczegółowe przykłady są również w tekście prezentacji dołączonym do paczki.
