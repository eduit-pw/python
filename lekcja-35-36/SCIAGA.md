# Temat 18. Wyjaśnienia do praktyki

## Klasa bazowa i pochodna

class Pralka(Urzadzenie) tworzy klasę pochodną. Obiekt dziedziczy dostępne metody bazy. Dziedziczenie opisuje relację, w której obiekt pochodny jest rodzajem obiektu bazowego.

## Odziedziczone __init__

Klasa bez własnego __init__ może korzystać z inicjalizacji odziedziczonej. Definicja własnego __init__ zastępuje odziedziczone wywołanie, więc inicjalizację bazy trzeba świadomie uruchomić.

## super

super().__init__(nazwa) wykorzystuje dalszą inicjalizację w kolejności dziedziczenia. W prostym pojedynczym dziedziczeniu jest to baza. Nie przekazuj self drugi raz.

## Nadpisanie metody

Metoda o tej samej nazwie w klasie pochodnej nadpisuje zachowanie odziedziczone. super().opis() pozwala wykorzystać opis bazy i dopisać własne informacje.

## Spójność stanu

Po nieudanej zmianie programu pralki poprzednia wartość powinna pozostać. Sprawdź granice i dwa niezależne obiekty. self.opis() wewnątrz opis może wywoływać metodę rekurencyjnie.

[Zadania i wyniki kontrolne](README.md)

To uzupełnienie przykładów z prezentacji. Definicje i kontrakty zadań czytaj łącznie. Szczegółowe przykłady są również w tekście prezentacji dołączonym do paczki.
