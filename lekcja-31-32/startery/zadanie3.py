# Temat 16. Zadanie 3. Porównywanie punktów
# Starter do uzupełnienia, bez rozwiązania.
# Pełne polecenie: README lekcji.
# TODO: Napisz Punkt(x, y). Równe punkty mają równe obie współrzędne.
# TODO: Dodaj __eq__. Dla argumentu innego niż Punkt zwróć NotImplemented.
# TODO: Utwórz a = Punkt(2, 3), b = Punkt(2, 3), c = Punkt(2, 4) i d = a.
# TODO: Sprawdź a == b, a == c, a is b, a is d, a == (2, 3).

class Punkt:

    def __init__(self, x, y):
        raise NotImplementedError('Uzupełnij rozwiązanie według polecenia.')

    def __eq__(self, inny):
        raise NotImplementedError('Uzupełnij rozwiązanie według polecenia.')
