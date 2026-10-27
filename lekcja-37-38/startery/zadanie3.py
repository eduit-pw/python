# Zadanie 3. Szkielet, temat 19.
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

class Trojkat(Figura):

    def __init__(self, a, h):
        """TODO: uzupełnij zgodnie z kontraktem w README."""
        pass

    def pole(self):
        """TODO: uzupełnij zgodnie z kontraktem w README."""
        pass

def suma_pol(figury):
    """TODO: uzupełnij zgodnie z kontraktem w README."""
    pass
