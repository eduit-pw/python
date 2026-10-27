# Zadanie 2. Szkielet, temat 25.
# Kontrakt i wyniki kontrolne są w README lekcji.
# pass oznacza miejsce na własną implementację.

from abc import ABC, abstractmethod

class Powiadomienie(ABC):

    @abstractmethod
    def przygotuj(self, tekst):
        """TODO: uzupełnij zgodnie z kontraktem w README."""
        pass

class Email(Powiadomienie):

    def przygotuj(self, tekst):
        """TODO: uzupełnij zgodnie z kontraktem w README."""
        pass

class SMS(Powiadomienie):

    def przygotuj(self, tekst):
        """TODO: uzupełnij zgodnie z kontraktem w README."""
        pass

class Nadawca(ABC):

    @abstractmethod
    def utworz(self):
        """TODO: uzupełnij zgodnie z kontraktem w README."""
        pass

    def przygotuj_wiadomosc(self, tekst):
        """TODO: uzupełnij zgodnie z kontraktem w README."""
        pass

class NadawcaEmail(Nadawca):

    def utworz(self):
        """TODO: uzupełnij zgodnie z kontraktem w README."""
        pass

class NadawcaSMS(Nadawca):

    def utworz(self):
        """TODO: uzupełnij zgodnie z kontraktem w README."""
        pass
