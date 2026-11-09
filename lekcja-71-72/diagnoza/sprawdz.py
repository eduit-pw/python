import unittest
from napraw import srednia


class TestSrednia(unittest.TestCase):
    def test_wynik_ulamkowy(self):
        self.assertAlmostEqual(srednia([2, 3]), 2.5)

    def test_pusta_lista(self):
        with self.assertRaises(ValueError):
            srednia([])


if __name__ == "__main__":
    unittest.main()
