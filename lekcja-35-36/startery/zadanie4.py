# Temat 18. Zadanie 4. Dla chętnych: Drugie urządzenie i raport
# Starter do uzupełnienia, bez rozwiązania.
# Pełne polecenie: README lekcji.
# TODO: Zdefiniuj Odkurzacz(Urzadzenie). Inicjalizuj stan bazy i własny atrybut moc = 1.
# TODO: Napisz ustaw_moc(self, poziom). Dopuszcza całkowite wartości 1-3. Poprawna wartość daje True i aktualizuje moc; błędna daje False bez zmiany mocy.
# TODO: Nadpisz opis(), wykorzystując super().opis(). Dopisz ", moc " oraz bieżącą moc.
# TODO: Utwórz pralkę z zadania 3 i odkurzacz. Ustaw pralce program 5 i odkurzaczowi moc 3. Włącz tylko odkurzacz.

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

class Odkurzacz(Urzadzenie):

    def __init__(self, nazwa):
        raise NotImplementedError('Uzupełnij rozwiązanie według polecenia.')

    def ustaw_moc(self, poziom):
        raise NotImplementedError('Uzupełnij rozwiązanie według polecenia.')

    def opis(self):
        raise NotImplementedError('Uzupełnij rozwiązanie według polecenia.')
