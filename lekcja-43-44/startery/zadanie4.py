# Temat 22. Zadanie 4. Dla chętnych: Format PESEL w obiekcie i funkcje z arkusza
# Starter do uzupełnienia, bez rozwiązania.
# Pełne polecenie: README lekcji.
# TODO: Zdefiniuj PeselFormatError(ValueError) i walidator sprawdz_format(pesel). Wymagaj dokładnie str, długości 11 i znaków ASCII od "0" do "9".
# TODO: Zły typ: TypeError("PESEL musi być napisem."). Zła długość: PeselFormatError("PESEL musi mieć 11 znaków."). Błędny znak: PeselFormatError("PESEL musi zawierać cyfry 0-9."). Najpierw sprawdzaj typ, potem długość, potem znaki. Nie normalizuj numeru przez strip() ani konwersję całości do liczby.
# TODO: W NumerPesel(pesel) sprawdź format przed zapisaniem _wartosc. Getter wartosc udostępnia napis tylko do odczytu; nie definiuj settera.
# TODO: Zachowaj osobną funkcję plec(pesel), która zwraca K dla parzystej cyfry o indeksie 9 i M dla nieparzystej. Zachowaj sprawdz_sume(pesel), zwracającą True albo False.

class PeselFormatError(ValueError):
    pass

def sprawdz_format(pesel):
    raise NotImplementedError('Uzupełnij rozwiązanie według polecenia.')

class NumerPesel:

    def __init__(self, pesel):
        raise NotImplementedError('Uzupełnij rozwiązanie według polecenia.')

    @property
    def wartosc(self):
        raise NotImplementedError('Uzupełnij rozwiązanie według polecenia.')

def plec(pesel):
    raise NotImplementedError('Uzupełnij rozwiązanie według polecenia.')

def sprawdz_sume(pesel):
    raise NotImplementedError('Uzupełnij rozwiązanie według polecenia.')
