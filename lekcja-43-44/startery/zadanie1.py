# Temat 22. Zadanie 1. Walidator oceny
# Starter do uzupełnienia, bez rozwiązania.
# Pełne polecenie: README lekcji.
# TODO: Zdefiniuj OcenaError(ValueError).
# TODO: Napisz sprawdz_ocene(ocena): wymagaj dokładnie int i zakresu 1-6 włącznie. Zły typ: TypeError("Ocena musi być typu int."); zły zakres: OcenaError("Zakres: 1-6.").
# TODO: Funkcja zwraca poprawną ocenę; nie wykonuje input() ani print().
# TODO: W programie głównym pobieraj ocenę przez int(input()). Po błędnym zapisie: Podaj liczbę całkowitą.. Po złym zakresie wyświetl komunikat wyjątku. Ponawiaj pytanie, aż przyjmiesz ocenę; potem wyświetl Ocena: i wartość.

class OcenaError(ValueError):
    pass

def sprawdz_ocene(ocena):
    raise NotImplementedError('Uzupełnij rozwiązanie według polecenia.')
