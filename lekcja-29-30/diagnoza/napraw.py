class Produkt:
    def __init__(self, nazwa):
        self.nazwa = nazwa
    @classmethod
    def z_tekstu(cls, tekst):
        return Produkt(tekst.strip())
class Ksiazka(Produkt):
    pass
