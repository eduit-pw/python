# Temat 14. Wyjaśnienia do praktyki

## Klasa i instancja

class opisuje dane i zachowanie. Wywołanie Klasa(...) tworzy instancję. Dwa wywołania zwykle tworzą dwa niezależne obiekty, przypisanie b = a tylko drugą nazwę tego samego.

## __init__

__init__(self, ...) inicjalizuje utworzony obiekt. Parametry po self przekazuje wywołujący. Metoda nie zwraca tworzonej instancji i powinna zakończyć się None.

## self i pole

self wskazuje bieżący obiekt. self.imie = imie zapisuje pole instancji z parametru. Sam zapis imie = ... tworzy lub zmienia nazwę lokalną, nie pole.

## Metoda instancji

obj.opis() wywołuje metodę i przekazuje obj jako self. Metoda może zwracać wynik albo zmieniać stan. Nawiasy wykonują metodę, ich pominięcie daje obiekt metody.

## Aktualny stan

Pole i obwód obliczaj z aktualnych wymiarów. Po zmianie szerokości wynik metody ma odzwierciedlać nowe dane. Nie trzymaj nieaktualnej kopii wyniku bez potrzeby.

[Zadania i wyniki kontrolne](README.md)

To uzupełnienie przykładów z prezentacji. Definicje i kontrakty zadań czytaj łącznie. Szczegółowe przykłady są również w tekście prezentacji dołączonym do paczki.
