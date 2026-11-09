import unittest
from rabaty import cena_po_rabacie


class TestRabaty(unittest.TestCase):
    def test_rabat_pietnascie_procent(self):
        self.assertEqual(cena_po_rabacie(20000, 15), 17000)

    def test_brak_rabatu(self):
        self.assertEqual(cena_po_rabacie(20000, 0), 20000)

    def test_rabat_sto_procent(self):
        self.assertEqual(cena_po_rabacie(20000, 100), 0)
