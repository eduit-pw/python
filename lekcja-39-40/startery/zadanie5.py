# Temat 20. Zadanie 5. Dla chętnych: Iterator parzystych
# Starter do uzupełnienia, bez rozwiązania.
# Pełne polecenie: README lekcji.
# TODO: __init__ zapisuje limit i bieżącą wartość 0.
# TODO: __iter__ zwraca self i **nie resetuje** wartości bieżącej.
# TODO: __next__ przy wyczerpaniu zgłasza StopIteration; w innym przypadku zapisuje wynik, zwiększa bieżącą wartość o 2 i oddaje wynik.
# TODO: Przetestuj list(ParzysteDo(5)) == [0, 2, 4], limit 0, limit -1 i dwa przejścia po tej samej instancji. Po wyczerpaniu drugie przejście daje [].

class ParzysteDo:

    def __init__(self, limit):
        raise NotImplementedError('Uzupełnij rozwiązanie według polecenia.')

    def __iter__(self):
        raise NotImplementedError('Uzupełnij rozwiązanie według polecenia.')

    def __next__(self):
        raise NotImplementedError('Uzupełnij rozwiązanie według polecenia.')
