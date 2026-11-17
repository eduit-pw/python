# Temat 60. Zadanie 1. Model i poprawny POST
# Starter do uzupełnienia, bez rozwiązania.
# Pełne polecenie: README lekcji.
# TODO: Dodaj AlbumWejscie, walidator tytułu i POST /sprawdz.
# TODO: Wyślij {"tytul":" Poranek ","pobrania":0} przez /docs.

from fastapi import FastAPI
from schematy import AlbumWejscie, AlbumOdczyt
app = FastAPI()

@app.post('/sprawdz')
def sprawdz(album: AlbumWejscie):
    raise NotImplementedError('Uzupełnij rozwiązanie według polecenia.')

@app.post('/podglad', response_model=AlbumOdczyt)
def podglad(album: AlbumWejscie):
    raise NotImplementedError('Uzupełnij rozwiązanie według polecenia.')
