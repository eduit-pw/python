class RezerwacjaMiejsc:
    def __init__(self, wolne):
        if wolne < 0:
            raise ValueError("Liczba miejsc nie może być ujemna.")
        self.wolne = wolne

    def zarezerwuj(self, liczba):
        if liczba <= 0:
            raise ValueError("Rezerwuj co najmniej jedno miejsce.")
        self.wolne -= liczba
        if self.wolne < 0:
            raise ValueError("Za mało wolnych miejsc.")
