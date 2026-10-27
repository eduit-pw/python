class BladWieku(ValueError):
    pass
class Osoba:
    def __init__(self, wiek):
        self.wiek = wiek
    def ustaw_wiek(self, wiek):
        self.wiek = wiek
        if type(wiek) is not int or not 0 <= wiek <= 120:
            raise BladWieku("Niepoprawny wiek")
