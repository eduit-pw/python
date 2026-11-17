# Temat 61. Zadanie 1. Dodawanie i lista
# Starter do uzupełnienia, bez rozwiązania.
# Pełne polecenie: README lekcji.
# TODO: Połącz schemat z tematu 60 z kodem GET i POST z tej lekcji.
# TODO: Od pustego stanu dodaj Poranek=120 i Wieczór=80. Pobierz listę.

from fastapi import FastAPI, HTTPException, Response
from schematy import AlbumWejscie, AlbumOdczyt
app = FastAPI()

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
