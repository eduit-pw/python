import unittest
class TestLista(unittest.TestCase):
    dane = []
    def test_a(self):
        self.dane.append(1)
        self.assertEqual(self.dane, [1])
    def test_b(self):
        self.assertEqual(self.dane, [])
