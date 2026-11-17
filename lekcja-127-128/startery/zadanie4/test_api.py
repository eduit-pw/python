import unittest, tempfile
from pathlib import Path
from fastapi.testclient import TestClient
import baza
from zadanie4 import app

class TestAPI(unittest.TestCase):

    def setUp(self):
        self.katalog = tempfile.TemporaryDirectory()
        self.stara = baza.SCIEZKA
        baza.SCIEZKA = Path(self.katalog.name) / 'test.db'
        self.kontekst = TestClient(app)
        self.klient = self.kontekst.__enter__()

    def tearDown(self):
        self.kontekst.__exit__(None, None, None)
        baza.SCIEZKA = self.stara
        self.katalog.cleanup()

    def test_start_i_izolacja(self):
        raise NotImplementedError('Dodaj własne żądania i asercje z polecenia.')
if __name__ == '__main__':
    unittest.main()
