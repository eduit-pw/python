# Temat 60. Zadanie 2. Granice danych
# Starter do uzupełnienia, bez rozwiązania.
# Pełne polecenie: README lekcji.
# TODO: Sprawdź tytuł długości 80 i 81 znaków, pusty tekst oraz same spacje.
# TODO: Dla pobrania sprawdź 0, -1, "3" i true.
# TODO: Zapisz, które pole wskazuje detail w odpowiedzi 422.

from fastapi import FastAPI
from schematy import AlbumWejscie, AlbumOdczyt
app = FastAPI()

@app.post('/sprawdz')
def sprawdz(album: AlbumWejscie):
    raise NotImplementedError('Uzupełnij rozwiązanie według polecenia.')

@app.post('/podglad', response_model=AlbumOdczyt)
def podglad(album: AlbumWejscie):
    raise NotImplementedError('Uzupełnij rozwiązanie według polecenia.')
