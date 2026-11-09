# Zadanie 1. Model i poprawny POST
# Pełne wymagania i wyniki kontrolne: ../README.md
# Najpierw ustal wejście i wynik. Uzupełnij kod; ten plik jest starterem.

from fastapi import FastAPI
from schematy import AlbumWejscie, AlbumOdczyt

@app.post('/sprawdz')
def sprawdz(album: AlbumWejscie):
    """TODO: uzupełnij zgodnie z kontraktem w README."""
    pass

@app.post('/podglad', response_model=AlbumOdczyt)
def podglad(album: AlbumWejscie):
    """TODO: uzupełnij zgodnie z kontraktem w README."""
    pass
