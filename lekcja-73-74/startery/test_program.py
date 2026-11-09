import unittest
from program import przywitanie


class TestPrzywitanie(unittest.TestCase):
    def test_imie(self):
        self.assertEqual(przywitanie("Ala"), "Cześć, Ala!")
