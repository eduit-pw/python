# Zadanie 2. Filtr query
# Pełne wymagania i wyniki kontrolne: ../README.md
# Najpierw ustal wejście i wynik. Uzupełnij kod; ten plik jest starterem.

import json
import time
from http.server import ThreadingHTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs

class Obsluga(BaseHTTPRequestHandler):

    def odpowiedz(self, status, dane, typ='application/json'):
        """TODO: uzupełnij zgodnie z kontraktem w README."""
        pass

    def do_GET(self):
        """TODO: uzupełnij zgodnie z kontraktem w README."""
        pass

    def do_POST(self):
        """TODO: uzupełnij zgodnie z kontraktem w README."""
        pass
