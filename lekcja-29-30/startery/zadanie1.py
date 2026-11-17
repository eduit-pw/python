# Temat 15. Zadanie 1. Dwa konta
# Starter do uzupełnienia, bez rozwiązania.
# Pełne polecenie: README lekcji.
# TODO: Utwórz Konto(wlasciciel, saldo) i metodę wplac(kwota).
# TODO: Dodaj wyplac(kwota): przy wystarczającym saldzie odejmij kwotę i zwróć True; w przeciwnym razie zwróć False, zachowując saldo.
# TODO: Utwórz konto Ali z 100 zł i Jana z 50 zł. Wpłać Ali 30 zł, wypłać 80 zł, następnie spróbuj wypłacić 60 zł.
# TODO: Wyświetl oba wyniki wypłat i oba salda. Zakładamy dodatnie kwoty.

class Konto:

    def __init__(self, wlasciciel, saldo):
        raise NotImplementedError('Uzupełnij rozwiązanie według polecenia.')

    def wplac(self, kwota):
        raise NotImplementedError('Uzupełnij rozwiązanie według polecenia.')

    def wyplac(self, kwota):
        raise NotImplementedError('Uzupełnij rozwiązanie według polecenia.')
