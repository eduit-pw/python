# Temat 19. Zadanie 2. Prostokąt bez pola
# Starter do uzupełnienia, bez rozwiązania.
# Pełne polecenie: README lekcji.
# TODO: Spróbuj utworzyć Prostokat(3, 4). Zapisz typ i przyczynę błędu.
# TODO: Uzupełnij pole(self), aby zwracało iloczyn boków.
# TODO: Wyświetl wyniki dla (3, 4), (0, 5) oraz (2.5, 4).
# TODO: Sprawdź, że po poprawieniu Prostokat sama Figura nadal nie pozwala utworzyć instancji.

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
