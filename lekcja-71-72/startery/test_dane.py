import unittest
from dane import ostatni_element


class TestOstatniElement(unittest.TestCase):
    def test_lista_niepusta(self):
        self.assertEqual(ostatni_element([4, 7, 9]), 9)

    def test_lista_pusta(self):
        with self.assertRaises(ValueError):
            ostatni_element([])
