# Temat 63. Zadanie 2. Parametry i apostrof
# Starter do uzupełnienia, bez rozwiązania.
# Pełne polecenie: README lekcji.
# TODO: Dodaj album o tytule "Anna's album" i pobrania=0.
# TODO: Odczytaj go po ID i sprawdź dokładny tytuł.
# TODO: Przejrzyj INSERT i potwierdź osobne przekazanie parametrów.

from contextlib import asynccontextmanager
from fastapi import FastAPI, HTTPException, Response
import baza
from schematy import AlbumWejscie, AlbumOdczyt

@asynccontextmanager
async def lifespan(app):
    yield
app = FastAPI(lifespan=lifespan)

@app.get('/status')
def status():
    raise NotImplementedError('Uzupełnij rozwiązanie według polecenia.')

@app.get('/albumy', response_model=list[AlbumOdczyt])
def lista():
    raise NotImplementedError('Uzupełnij rozwiązanie według polecenia.')

@app.get('/albumy/{identyfikator}', response_model=AlbumOdczyt)
def odczyt(identyfikator: int):
    raise NotImplementedError('Uzupełnij rozwiązanie według polecenia.')

@app.post('/albumy', status_code=201, response_model=AlbumOdczyt)
def dodaj(album: AlbumWejscie):
    raise NotImplementedError('Uzupełnij rozwiązanie według polecenia.')

@app.put('/albumy/{identyfikator}', response_model=AlbumOdczyt)
def zmien(identyfikator: int, album: AlbumWejscie):
    raise NotImplementedError('Uzupełnij rozwiązanie według polecenia.')

@app.delete('/albumy/{identyfikator}', status_code=204, response_class=Response)
def usun(identyfikator: int):
    raise NotImplementedError('Uzupełnij rozwiązanie według polecenia.')
