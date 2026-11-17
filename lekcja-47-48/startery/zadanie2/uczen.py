class OcenaError(ValueError):
    pass

def sprawdz_ocene(ocena):
    if type(ocena) is not int:
        raise TypeError("Ocena musi być typu int.")
    if ocena < 1 or ocena > 6:
        raise OcenaError("Zakres: 1-6.")
    return ocena

class Uczen:
    def __init__(self, imie, ocena):
        if type(imie) is not str:
            raise TypeError("Imię musi być napisem.")
        imie = imie.strip()
        if imie == "":
            raise ValueError("Imię nie może być puste.")
        sprawdz_ocene(ocena)
        self.imie = imie
        self.ocena = ocena

    @property
    def ocena(self):
        return self._ocena

    @ocena.setter
    def ocena(self, nowa_ocena):
        sprawdz_ocene(nowa_ocena)
        self._ocena = nowa_ocena
