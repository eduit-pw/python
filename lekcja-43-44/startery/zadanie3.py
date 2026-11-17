# Temat 22. Zadanie 3. Magazyn i odrzucona operacja
# Starter do uzupełnienia, bez rozwiązania.
# Pełne polecenie: README lekcji.
# TODO: Utwórz BrakTowaruError(Exception) i klasę Magazyn(stan).
# TODO: Stan początkowy ma być dokładnie int i nieujemny. Zły typ: TypeError("Wymagany typ int."); ujemny stan: ValueError("Stan nie może być ujemny.").
# TODO: Właściwość stan ma tylko getter zwracający _stan.
# TODO: Metoda pobierz(sztuki) wymaga dokładnie int, wartości większej od 0 oraz nie większej od aktualnego stanu. Komunikaty: Wymagany typ int., Ilość musi być dodatnia., Za mało towaru.. Ostatni komunikat ma pochodzić z BrakTowaruError.

class BrakTowaruError(Exception):
    pass

class Magazyn:

    def __init__(self, stan):
        raise NotImplementedError('Uzupełnij rozwiązanie według polecenia.')

    @property
    def stan(self):
        raise NotImplementedError('Uzupełnij rozwiązanie według polecenia.')

    def pobierz(self, sztuki):
        raise NotImplementedError('Uzupełnij rozwiązanie według polecenia.')
