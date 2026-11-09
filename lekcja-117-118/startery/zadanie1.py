# Zadanie 1. Usługa działa
# Pełne wymagania i wyniki kontrolne: ../README.md
# Najpierw ustal wejście i wynik. Uzupełnij kod; ten plik jest starterem.

from fastapi import FastAPI

@app.get('/status')
def status():
    """TODO: uzupełnij zgodnie z kontraktem w README."""
    pass

@app.get('/kwadrat/{liczba}')
def kwadrat(liczba: int):
    """TODO: uzupełnij zgodnie z kontraktem w README."""
    pass

@app.get('/powitanie')
def powitanie(imie: str='Uczeń'):
    """TODO: uzupełnij zgodnie z kontraktem w README."""
    pass
