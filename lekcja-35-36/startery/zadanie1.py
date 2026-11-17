# Temat 18. Zadanie 1. Odziedziczone metody i dwa obiekty
# Starter do uzupełnienia, bez rozwiązania.
# Pełne polecenie: README lekcji.
# TODO: Utwórz p1 = Pralka("Pralka A") i p2 = Pralka("Pralka B").
# TODO: Przed uruchomieniem zapisz wyniki p1.opis() oraz p2.opis().
# TODO: Włącz tylko p1, wyświetl opisy obu obiektów, a następnie wyłącz p1 i ponownie wyświetl jego opis.
# TODO: Wyjaśnij, skąd Pralka bierze metody i dlaczego zmiana p1 nie włącza p2.

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
    pass
