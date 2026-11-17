# Temat 22. Zadanie 2. Uczeń z walidowaną właściwością
# Starter do uzupełnienia, bez rozwiązania.
# Pełne polecenie: README lekcji.
# TODO: Umieść w pliku klasę OcenaError i walidator z zadania 1.
# TODO: Napisz Uczen(imie, ocena). Imię ma być dokładnie str; po strip() nie może być puste. Zły typ: TypeError("Imię musi być napisem."); puste imię: ValueError("Imię nie może być puste.").
# TODO: W konstruktorze sprawdź obie wartości przed ich zapisaniem. Przechowuj imię po usunięciu spacji z początku i końca. Ustaw ocenę przez właściwość ocena.
# TODO: Getter zwraca _ocena. Setter korzysta z sprawdz_ocene(nowa_ocena) przed przypisaniem do _ocena.

class OcenaError(ValueError):
    pass

def sprawdz_ocene(ocena):
    raise NotImplementedError('Uzupełnij rozwiązanie według polecenia.')

class Uczen:

    def __init__(self, imie, ocena):
        raise NotImplementedError('Uzupełnij rozwiązanie według polecenia.')

    @property
    def ocena(self):
        raise NotImplementedError('Uzupełnij rozwiązanie według polecenia.')

    @ocena.setter
    def ocena(self, nowa_ocena):
        raise NotImplementedError('Uzupełnij rozwiązanie według polecenia.')
