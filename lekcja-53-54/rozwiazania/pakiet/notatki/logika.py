from notatki.model import Notatka


class Notatnik:
    def __init__(self):
        self._notatki = []

    def dodaj(self, tekst):
        notatka = Notatka(tekst)
        self._notatki.append(notatka)
        return notatka

    def wszystkie(self):
        return self._notatki.copy()
