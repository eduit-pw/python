# Zadanie 4. Szkielet, temat 19.
# Kontrakt i wyniki kontrolne są w README lekcji.
# pass oznacza miejsce na własną implementację.

from abc import ABC, abstractmethod

class Pytanie(ABC):

    def __init__(self, tresc, poprawna):
        """TODO: uzupełnij zgodnie z kontraktem w README."""
        pass

    @abstractmethod
    def sprawdz(self, odpowiedz):
        """TODO: uzupełnij zgodnie z kontraktem w README."""
        pass

class PytanieTekstowe(Pytanie):

    def sprawdz(self, odpowiedz):
        """TODO: uzupełnij zgodnie z kontraktem w README."""
        pass

class PytanieWyboru(Pytanie):

    def sprawdz(self, odpowiedz):
        """TODO: uzupełnij zgodnie z kontraktem w README."""
        pass

def policz_poprawne(proby):
    """TODO: uzupełnij zgodnie z kontraktem w README."""
    pass
