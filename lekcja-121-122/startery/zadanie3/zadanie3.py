# Temat 61. Zadanie 3. Usunięcie i kolejny zapis
# Starter do uzupełnienia, bez rozwiązania.
# Pełne polecenie: README lekcji.
# TODO: Usuń pierwszy album. Ponownie wyślij DELETE dla tego samego ID.
# TODO: Dodaj trzeci album Noc z pobrania=0.
# TODO: Sprawdź, czy Wieczór zachował ID, a nowy album nie przejął usuniętego ID.

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
