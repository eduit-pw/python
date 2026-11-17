# Temat 15. Zadanie 3. Produkt tworzony na dwa sposoby
# Starter do uzupełnienia, bez rozwiązania.
# Pełne polecenie: README lekcji.
# TODO: Utwórz Produkt(nazwa, cena) z polami instancji. Cena jest całkowitą liczbą złotych.
# TODO: Dodaj metodę klasową z_tekstu(tekst). Rozdziel tekst przez średnik, zamień cenę na int i zwróć cls(...).
# TODO: Dodaj metodę klasową darmowy(nazwa), zwracającą produkt o cenie 0.
# TODO: Sprawdź Produkt.z_tekstu("Zeszyt;12") i Produkt.darmowy("Naklejka"). Wypisz pola obu obiektów.

class Produkt:

    def __init__(self, nazwa, cena):
        raise NotImplementedError('Uzupełnij rozwiązanie według polecenia.')

    @classmethod
    def z_tekstu(cls, tekst):
        raise NotImplementedError('Uzupełnij rozwiązanie według polecenia.')

    @classmethod
    def darmowy(cls, nazwa):
        raise NotImplementedError('Uzupełnij rozwiązanie według polecenia.')
