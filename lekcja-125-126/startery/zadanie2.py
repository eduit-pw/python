# Zadanie 2. Błąd startu
# Pełne wymagania i wyniki kontrolne: ../README.md
# Najpierw ustal wejście i wynik. Uzupełnij kod; ten plik jest starterem.

from contextlib import asynccontextmanager
from fastapi import FastAPI, HTTPException, Response
import baza
from schematy import AlbumWejscie, AlbumOdczyt

@asynccontextmanager
async def lifespan(app):
    """TODO: uzupełnij zgodnie z kontraktem w README."""
    pass

@app.get('/status')
def status():
    """TODO: uzupełnij zgodnie z kontraktem w README."""
    pass

@app.get('/albumy', response_model=list[AlbumOdczyt])
def lista():
    """TODO: uzupełnij zgodnie z kontraktem w README."""
    pass

@app.get('/albumy/{identyfikator}', response_model=AlbumOdczyt)
def odczyt(identyfikator: int):
    """TODO: uzupełnij zgodnie z kontraktem w README."""
    pass

@app.post('/albumy', status_code=201, response_model=AlbumOdczyt)
def dodaj(album: AlbumWejscie):
    """TODO: uzupełnij zgodnie z kontraktem w README."""
    pass

@app.put('/albumy/{identyfikator}', response_model=AlbumOdczyt)
def zmien(identyfikator: int, album: AlbumWejscie):
    """TODO: uzupełnij zgodnie z kontraktem w README."""
    pass

@app.delete('/albumy/{identyfikator}', status_code=204, response_class=Response)
def usun(identyfikator: int):
    """TODO: uzupełnij zgodnie z kontraktem w README."""
    pass
