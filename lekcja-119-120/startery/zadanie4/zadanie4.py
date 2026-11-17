# Temat 60. Zadanie 4. Dla chętnych: Wynik opisany schematem
# Starter do uzupełnienia, bez rozwiązania.
# Pełne polecenie: README lekcji.
# TODO: Dodaj AlbumOdczyt i POST /podglad zgodnie z umową powyżej.
# TODO: Wyślij poprawny album. Sprawdź schemat odpowiedzi w /docs.
# TODO: Wyjaśnij, kto nadaje id i dlaczego klient nie wysyła go w AlbumWejscie.

from fastapi import FastAPI
from schematy import AlbumWejscie, AlbumOdczyt
app = FastAPI()

@app.post('/sprawdz')
def sprawdz(album: AlbumWejscie):
    raise NotImplementedError('Uzupełnij rozwiązanie według polecenia.')

@app.post('/podglad', response_model=AlbumOdczyt)
def podglad(album: AlbumWejscie):
    raise NotImplementedError('Uzupełnij rozwiązanie według polecenia.')
