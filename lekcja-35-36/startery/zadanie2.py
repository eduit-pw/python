# Temat 18. Zadanie 2. Program pralki
# Starter do uzupełnienia, bez rozwiązania.
# Pełne polecenie: README lekcji.
# TODO: Dodaj do Pralka własne __init__(self, nazwa). Użyj inicjalizacji bazy i ustaw program = 1.
# TODO: Napisz ustaw_program(self, numer). Dla całkowitego numeru z zakresu 1-5 ustawia program i zwraca True. Poza zakresem zwraca False i zachowuje dotychczasowy program. Przyjmujemy liczby całkowite; nie testujemy napisów, None ani bool.
# TODO: Sprawdź stan początkowy i wywołania kolejno z wartościami 5, 0, 6, 1.
# TODO: Sprawdź, że odziedziczone wlacz() nadal działa.

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
