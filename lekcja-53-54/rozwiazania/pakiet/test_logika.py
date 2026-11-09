import unittest
from notatki.logika import Notatnik


class TestNotatnik(unittest.TestCase):
    def test_pusty_notatnik(self):
        self.assertEqual(Notatnik().wszystkie(), [])

    def test_dodanie_notatki(self):
        notatnik = Notatnik()
        notatka = notatnik.dodaj("  Sprawdzić importy  ")
        self.assertEqual(notatka.tekst, "Sprawdzić importy")
        self.assertEqual(notatnik.wszystkie(), [notatka])

    def test_odrzucenie_pustej_notatki(self):
        notatnik = Notatnik()
        with self.assertRaises(ValueError):
            notatnik.dodaj("   ")
        self.assertEqual(notatnik.wszystkie(), [])


if __name__ == "__main__":
    unittest.main()
