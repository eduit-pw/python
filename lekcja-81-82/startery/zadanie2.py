# Temat 41. Zadanie 2. Testy jednostkowe
# Starter do uzupełnienia, bez rozwiązania.
# Pełne polecenie: README lekcji.
# TODO: Napisz pięć osobnych metod unittest dla tabeli przypadków Cezara.
# TODO: Nadaj nazwy opisujące przypadki. Użyj assertEqual.
# TODO: Uruchom python -m unittest -v. Dodaj osobny test klucza 0. Adaptacja INF.04-02-25.06-SG, III: dodatkowy test klucza 0.

import unittest
from cezar import cezar

class TestCezar(unittest.TestCase):

    def test_przesuniecie(self):
        raise NotImplementedError('Uzupełnij rozwiązanie według polecenia.')

    def test_zawijanie(self):
        raise NotImplementedError('Uzupełnij rozwiązanie według polecenia.')

    def test_ujemny(self):
        raise NotImplementedError('Uzupełnij rozwiązanie według polecenia.')

    def test_duzy_klucz(self):
        raise NotImplementedError('Uzupełnij rozwiązanie według polecenia.')

    def test_spacja(self):
        raise NotImplementedError('Uzupełnij rozwiązanie według polecenia.')

    def test_zero(self):
        raise NotImplementedError('Uzupełnij rozwiązanie według polecenia.')

if __name__ == "__main__":
    unittest.main()
