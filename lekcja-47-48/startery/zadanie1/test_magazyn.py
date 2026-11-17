import unittest
from magazyn import Magazyn, BrakTowaruError

class TestMagazyn(unittest.TestCase):

    def setUp(self):
        raise NotImplementedError('Przygotuj lub posprzątaj dane testu według zadania.')

    def test_stan_poczatkowy(self):
        raise NotImplementedError('Napisz asercje opisane w poleceniu tego testu.')

    def test_pobranie_dwoch(self):
        raise NotImplementedError('Napisz asercje opisane w poleceniu tego testu.')

    def test_caly_stan(self):
        raise NotImplementedError('Napisz asercje opisane w poleceniu tego testu.')

    def test_brak_towaru(self):
        raise NotImplementedError('Napisz asercje opisane w poleceniu tego testu.')

    def test_pobranie_zera(self):
        raise NotImplementedError('Napisz asercje opisane w poleceniu tego testu.')

    def test_pobranie_ujemne(self):
        raise NotImplementedError('Napisz asercje opisane w poleceniu tego testu.')

    def test_pobranie_napisu(self):
        raise NotImplementedError('Napisz asercje opisane w poleceniu tego testu.')
if __name__ == '__main__':
    unittest.main()
