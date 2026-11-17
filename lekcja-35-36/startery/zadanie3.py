# Temat 18. Zadanie 3. Rozszerzony opis pralki
# Starter do uzupełnienia, bez rozwiązania.
# Pełne polecenie: README lekcji.
# TODO: W klasie Pralka z zadania 2 nadpisz opis(self).
# TODO: Wywołaj opis z bazy przez super().opis() i dopisz ", program " oraz numer programu.
# TODO: Metoda ma zwracać napis. Nie powielaj warunku włączenia z klasy bazowej.
# TODO: Sprawdź opis początkowy, następnie ustaw program 5, włącz pralkę i ponownie wyświetl opis. Zmień nazwę obiektu na "Łazienka" i sprawdź trzeci wynik.

class Urzadzenie:

    def __init__(self, nazwa):
        raise NotImplementedError('Uzupełnij rozwiązanie według polecenia.')

    def wlacz(self):
        raise NotImplementedError('Uzupełnij rozwiązanie według polecenia.')

    def wylacz(self):
        raise NotImplementedError('Uzupełnij rozwiązanie według polecenia.')

    def opis(self):
        raise NotImplementedError('Uzupełnij rozwiązanie według polecenia.')

class Pralka(Urzadzenie):

    def __init__(self, nazwa):
        raise NotImplementedError('Uzupełnij rozwiązanie według polecenia.')

    def ustaw_program(self, numer):
        raise NotImplementedError('Uzupełnij rozwiązanie według polecenia.')

    def opis(self):
        raise NotImplementedError('Uzupełnij rozwiązanie według polecenia.')
