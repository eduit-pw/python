# Temat 19. Zadanie 5. Dla chętnych: Walidacja wymiarów
# Starter do uzupełnienia, bez rozwiązania.
# Pełne polecenie: README lekcji.

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
