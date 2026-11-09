import unittest
from napraw import wynik


class TestImport(unittest.TestCase):
    def test_wynik(self):
        self.assertEqual(wynik(), 12)


if __name__ == "__main__":
    unittest.main()
