# Temat 17. Zadanie 2. Cena przez właściwość
# Starter do uzupełnienia, bez rozwiązania.
# Pełne polecenie: README lekcji.
# TODO: Wewnętrzne _cena zaczyna od 0; argument konstruktora przechodzi przez setter.
# TODO: Getter zwraca aktualną cenę. Setter zapisuje wyłącznie całkowite wartości 0-1000. Inne liczby całkowite pozostawiają dotychczasowy stan.
# TODO: Utwórz produkt z ceną 40 i sprawdź przypisania z tabeli w podanej kolejności.
# TODO: Osobno utwórz Produkt(-1) i Produkt(1001). Oba mają cenę 0.

class Produkt:

    def __init__(self, cena):
        raise NotImplementedError('Uzupełnij rozwiązanie według polecenia.')

    @property
    def cena(self):
        raise NotImplementedError('Uzupełnij rozwiązanie według polecenia.')

    @cena.setter
    def cena(self, nowa_cena):
        raise NotImplementedError('Uzupełnij rozwiązanie według polecenia.')
