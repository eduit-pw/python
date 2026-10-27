# Zadanie 4. Start aplikacji i izolacja
# Pełne wymagania i wyniki kontrolne: ../README.md
# Najpierw ustal wejście i wynik. Uzupełnij kod; ten plik jest starterem.

import unittest, tempfile
from pathlib import Path
from fastapi.testclient import TestClient
import baza
from main import app

class TestAPI(unittest.TestCase):

    def setUp(self):
        """TODO: uzupełnij zgodnie z kontraktem w README."""
        pass

    def tearDown(self):
        """TODO: uzupełnij zgodnie z kontraktem w README."""
        pass

    def test_dodanie_i_odczyt(self):
        """TODO: uzupełnij zgodnie z kontraktem w README."""
        pass

    def test_blad_nie_zmienia_stanu(self):
        """TODO: uzupełnij zgodnie z kontraktem w README."""
        pass

    def test_cykl(self):
        """TODO: uzupełnij zgodnie z kontraktem w README."""
        pass

    def test_start_i_izolacja(self):
        """TODO: uzupełnij zgodnie z kontraktem w README."""
        pass
