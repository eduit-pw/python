# Temat 19. Zadanie 4. Dla chętnych: Dwa rodzaje pytań do quizu
# Starter do uzupełnienia, bez rozwiązania.
# Pełne polecenie: README lekcji.
# TODO: Dodaj PytanieTekstowe(Pytanie). Porównuje odpowiedź i klucz po usunięciu białych znaków z końców i bez rozróżniania wielkości liter: strip().lower(). Nie usuwamy spacji ze środka napisu.
# TODO: Dodaj PytanieWyboru(Pytanie). Dopuszcza jedną literę A, B, C lub D, z ignorowaniem wielkości liter i białych znaków z końców. Inna wartość daje False. Poprawny klucz jest jedną z liter A-D.
# TODO: Obie klasy dziedziczą gotowe __init__. Nie definiuj kolejnego konstruktora, jeśli nie potrzebujesz nowych atrybutów.
# TODO: Funkcja policz_poprawne(proby) przyjmuje listę par (obiekt_pytania, odpowiedz). Jedną pętlą wywołuje pytanie.sprawdz(odpowiedz) i zwraca liczbę poprawnych odpowiedzi. Bez gałęzi zależnych od rodzaju pytania.

from abc import ABC, abstractmethod

class Pytanie(ABC):

    def __init__(self, tresc, poprawna):
        raise NotImplementedError('Uzupełnij rozwiązanie według polecenia.')

    @abstractmethod
    def sprawdz(self, odpowiedz):
        raise NotImplementedError('Uzupełnij rozwiązanie według polecenia.')

class PytanieTekstowe(Pytanie):

    def sprawdz(self, odpowiedz):
        raise NotImplementedError('Uzupełnij rozwiązanie według polecenia.')

class PytanieWyboru(Pytanie):

    def sprawdz(self, odpowiedz):
        raise NotImplementedError('Uzupełnij rozwiązanie według polecenia.')

def policz_poprawne(proby):
    raise NotImplementedError('Uzupełnij rozwiązanie według polecenia.')
