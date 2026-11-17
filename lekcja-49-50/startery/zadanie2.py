# Temat 25. Zadanie 2. Metoda Wytwórcza - cztery testy
# Starter do uzupełnienia, bez rozwiązania.
# Pełne polecenie: README lekcji.
# TODO: Zdefiniuj klasy produktów: Powiadomienie, Email, SMS.
# TODO: Utwórz bazowego twórcę Nadawca z abstrakcyjną metodą utworz.
# TODO: W przygotuj_wiadomosc wywołaj metodę wytwórczą i metodę produktu.
# TODO: W podklasach twórcy zwracaj odpowiednio Email() i SMS().

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
