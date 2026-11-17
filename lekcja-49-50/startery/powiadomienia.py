from abc import ABC, abstractmethod

class Powiadomienie(ABC):

    @abstractmethod
    def przygotuj(self, tekst):
        raise NotImplementedError('Uzupełnij rozwiązanie według polecenia.')

class Email(Powiadomienie):

    def przygotuj(self, tekst):
        raise NotImplementedError('Uzupełnij rozwiązanie według polecenia.')

class SMS(Powiadomienie):

    def przygotuj(self, tekst):
        raise NotImplementedError('Uzupełnij rozwiązanie według polecenia.')

class Nadawca(ABC):

    @abstractmethod
    def utworz(self):
        raise NotImplementedError('Uzupełnij rozwiązanie według polecenia.')

    def przygotuj_wiadomosc(self, tekst):
        raise NotImplementedError('Uzupełnij rozwiązanie według polecenia.')

class NadawcaEmail(Nadawca):

    def utworz(self):
        raise NotImplementedError('Uzupełnij rozwiązanie według polecenia.')

class NadawcaSMS(Nadawca):

    def utworz(self):
        raise NotImplementedError('Uzupełnij rozwiązanie według polecenia.')
