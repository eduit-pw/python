# Zadanie 2. Szkielet, temat 19.
# Kontrakt i wyniki kontrolne są w README lekcji.
# pass oznacza miejsce na własną implementację.

from abc import ABC, abstractmethod

class Zwierze:

    def glos(self):
        """TODO: uzupełnij zgodnie z kontraktem w README."""
        pass

class Pies(Zwierze):

    def glos(self):
        """TODO: uzupełnij zgodnie z kontraktem w README."""
        pass

class Kot(Zwierze):

    def glos(self):
        """TODO: uzupełnij zgodnie z kontraktem w README."""
        pass

class Figura(ABC):

    @abstractmethod
    def pole(self):
        """TODO: uzupełnij zgodnie z kontraktem w README."""
        pass

class Prostokat(Figura):

    def __init__(self, a, b):
        """TODO: uzupełnij zgodnie z kontraktem w README."""
        pass

    def pole(self):
        """TODO: uzupełnij zgodnie z kontraktem w README."""
        pass
