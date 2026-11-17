# Temat 17. Zadanie 3. Liczba wypożyczeń tylko do odczytu
# Starter do uzupełnienia, bez rozwiązania.
# Pełne polecenie: README lekcji.
# TODO: Konstruktor ustawia _liczba_wypozyczen = 0.
# TODO: Właściwość liczba_wypozyczen ma getter i nie ma settera.
# TODO: wypozycz() zwiększa wewnętrzny licznik o 1 i nie zwraca wyniku.
# TODO: Utwórz dwa egzemplarze. Pierwszy wypożycz dwukrotnie, drugi pozostaw bez zmian. Odczytaj ich właściwości: oczekiwane wartości 2 0.

class Egzemplarz:

    def __init__(self):
        raise NotImplementedError('Uzupełnij rozwiązanie według polecenia.')

    @property
    def liczba_wypozyczen(self):
        raise NotImplementedError('Uzupełnij rozwiązanie według polecenia.')

    def wypozycz(self):
        raise NotImplementedError('Uzupełnij rozwiązanie według polecenia.')
