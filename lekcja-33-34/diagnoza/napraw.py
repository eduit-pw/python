class Konto:
    def __init__(self, saldo):
        self.saldo = saldo
    @property
    def saldo(self):
        return self.saldo
    @saldo.setter
    def saldo(self, wartosc):
        self.saldo = wartosc
