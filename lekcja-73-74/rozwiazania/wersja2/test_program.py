import unittest
from program import przywitanie


class TestPrzywitanie(unittest.TestCase):
    def test_imie(self):
        self.assertEqual(przywitanie("Ala"), "Cześć, Ala!")

    def test_spacje(self):
        self.assertEqual(przywitanie("  Ala  "), "Cześć, Ala!")
