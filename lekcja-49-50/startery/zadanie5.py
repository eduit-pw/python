# Temat 25. Zadanie 5. Dla chętnych: Trzeci produkt - dodatkowe
# Starter do uzupełnienia, bez rozwiązania.
# Pełne polecenie: README lekcji.

from powiadomienia import Powiadomienie, Nadawca

class Push(Powiadomienie):

    def przygotuj(self, tekst):
        raise NotImplementedError('Uzupełnij rozwiązanie według polecenia.')

class NadawcaPush(Nadawca):

    def utworz(self):
        raise NotImplementedError('Uzupełnij rozwiązanie według polecenia.')
