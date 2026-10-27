class Urzadzenie:
    def __init__(self, nazwa):
        self.nazwa = nazwa
        self.wlaczone = False

    def wlacz(self):
        self.wlaczone = True

    def wylacz(self):
        self.wlaczone = False

    def opis(self):
        stan = "włączone" if self.wlaczone else "wyłączone"
        return f"{self.nazwa}: {stan}"
