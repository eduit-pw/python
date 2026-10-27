# Temat 15. Wyjaśnienia do praktyki

## Pole obiektu i klasy

Pole zapisane przez self należy do instancji. Pole zapisane w ciele klasy jest wspólne w odczycie, dopóki instancja go nie przesłoni. Wspólna mutowalna lista może połączyć dane wielu obiektów.

## Metoda klasowa

@classmethod przekazuje klasę jako cls. Przydaje się do wspólnych danych i alternatywnego tworzenia przez cls(...). Nie dostaje automatycznie konkretnej instancji.

## Metoda statyczna

@staticmethod nie dodaje self ani cls. Otrzymuje tylko podane argumenty. Użyj jej dla narzędzia związanego tematycznie z klasą, które nie potrzebuje stanu obiektu.

## Wspólny licznik

Zwiększaj Klasa.licznik i zapisuj nadany numer w self.numer. self.licznik += 1 może utworzyć pole instancji zamiast zmienić wspólną liczbę. del zmiennej sam nie zmniejsza licznika.

## Osobna lista

Utwórz self.wpisy = [] w __init__, jeśli każdy obiekt ma mieć własną listę. Sprawdź dwa obiekty i mutację jednego. Przy metodach obliczeniowych zwracaj wynik, nie wyłącznie print.

[Zadania i wyniki kontrolne](README.md)

To uzupełnienie przykładów z prezentacji. Definicje i kontrakty zadań czytaj łącznie. Szczegółowe przykłady są również w tekście prezentacji dołączonym do paczki.
