import unittest
def podwoj(x):
    return x * 2
class TestPodwoj(unittest.TestCase):
    def sprawdz_wynik(self):
        self.assertEqual(podwoj(3), 6)
