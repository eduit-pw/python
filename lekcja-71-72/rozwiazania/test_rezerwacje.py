import unittest
from rezerwacje import RezerwacjaMiejsc


class TestRezerwacja(unittest.TestCase):
    def test_poprawna_rezerwacja(self):
        rezerwacja = RezerwacjaMiejsc(5)
        rezerwacja.zarezerwuj(2)
        self.assertEqual(rezerwacja.wolne, 3)

    def test_odrzucona_rezerwacja_zachowuje_stan(self):
        rezerwacja = RezerwacjaMiejsc(5)
        with self.assertRaises(ValueError):
            rezerwacja.zarezerwuj(6)
        self.assertEqual(rezerwacja.wolne, 5)
