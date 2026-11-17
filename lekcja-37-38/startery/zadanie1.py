# Temat 19. Zadanie 1. Kolejne głosy
# Starter do uzupełnienia, bez rozwiązania.
# Pełne polecenie: README lekcji.
# TODO: Przed uruchomieniem pętli dla [Pies(), Kot(), Zwierze()] zapisz przewidywane wyniki i klasy, których metody zostaną wykonane.
# TODO: Dodaj klasę Krowa(Zwierze) z metodą glos() zwracającą "muu".
# TODO: Uruchom tę samą pętlę dla [Kot(), Krowa(), Pies()], a następnie dla pustej listy.
# TODO: Wyjaśnij, dlaczego dodanie krowy nie wymaga zmiany wnętrza pętli.

from abc import ABC, abstractmethod

class Zwierze:

    def glos(self):
        raise NotImplementedError('Uzupełnij rozwiązanie według polecenia.')

class Pies(Zwierze):

    def glos(self):
        raise NotImplementedError('Uzupełnij rozwiązanie według polecenia.')

class Kot(Zwierze):

    def glos(self):
        raise NotImplementedError('Uzupełnij rozwiązanie według polecenia.')

class Figura(ABC):

    @abstractmethod
    def pole(self):
        raise NotImplementedError('Uzupełnij rozwiązanie według polecenia.')

class Krowa(Zwierze):

    def glos(self):
        raise NotImplementedError('Uzupełnij rozwiązanie według polecenia.')
