class BrakTowaruError(Exception):
    pass

class Magazyn:
    def __init__(self, stan):
        if type(stan) is not int:
            raise TypeError("Wymagany typ int.")
        if stan < 0:
            raise ValueError("Stan nie może być ujemny.")
        self._stan = stan

    @property
    def stan(self):
        return self._stan

    def pobierz(self, sztuki):
        if type(sztuki) is not int:
            raise TypeError("Wymagany typ int.")
        if sztuki <= 0:
            raise ValueError("Ilość musi być dodatnia.")
        if sztuki > self._stan:
            raise BrakTowaruError("Za mało towaru.")
        self._stan -= sztuki
