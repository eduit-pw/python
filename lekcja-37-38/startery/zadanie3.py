# Temat 19. Zadanie 3. Różne figury w jednym raporcie
# Starter do uzupełnienia, bez rozwiązania.
# Pełne polecenie: README lekcji.
# TODO: Utwórz Trojkat(Figura). Konstruktor przyjmuje nieujemną podstawę a i wysokość h. pole() zwraca a * h / 2.
# TODO: Napisz funkcję suma_pol(figury), która w jednej klasycznej pętli dodaje wyniki figura.pole() i zwraca sumę. Funkcja nie rozgałęzia działania według typu figury.
# TODO: Wyświetl pola i sumę dla [Prostokat(3, 4), Trojkat(4, 3), Prostokat(0, 5)].
# TODO: Sprawdź pustą listę i listę z jednym trójkątem.

from abc import ABC, abstractmethod

class Zwierze:

    def glos(self):
        raise NotImplementedError('Uzupełnij rozwiązanie według polecenia.')

class Pies(Zwierze):

    def glos(self):
        raise NotImplementedError('Uzupełnij rozwiązanie według polecenia.')

class Kot(Zwierze):

    def glos(self):
        raise NotImplementedError('Uzupełnij rozwiązanie według polecenia.')

class Figura(ABC):

    @abstractmethod
    def pole(self):
        raise NotImplementedError('Uzupełnij rozwiązanie według polecenia.')

class Prostokat(Figura):

    def __init__(self, a, b):
        raise NotImplementedError('Uzupełnij rozwiązanie według polecenia.')

    def pole(self):
        raise NotImplementedError('Uzupełnij rozwiązanie według polecenia.')

class Trojkat(Figura):

    def __init__(self, a, h):
        raise NotImplementedError('Uzupełnij rozwiązanie według polecenia.')

    def pole(self):
        raise NotImplementedError('Uzupełnij rozwiązanie według polecenia.')

def suma_pol(figury):
    raise NotImplementedError('Uzupełnij rozwiązanie według polecenia.')
