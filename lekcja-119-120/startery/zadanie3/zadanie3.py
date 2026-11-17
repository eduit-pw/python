# Temat 60. Zadanie 3. Brakujące i dodatkowe pola
# Starter do uzupełnienia, bez rozwiązania.
# Pełne polecenie: README lekcji.
# TODO: Wyślij JSON bez pobrania, potem z pobrania=2 i dodatkowym id=99.
# TODO: Zmień deklarację pobrania na Field(default=0, ge=0, strict=True).
# TODO: Ponownie wyślij tylko tytul i porównaj wyniki.

from fastapi import FastAPI
from schematy import AlbumWejscie, AlbumOdczyt
app = FastAPI()

@app.post('/sprawdz')
def sprawdz(album: AlbumWejscie):
    raise NotImplementedError('Uzupełnij rozwiązanie według polecenia.')

@app.post('/podglad', response_model=AlbumOdczyt)
def podglad(album: AlbumWejscie):
    raise NotImplementedError('Uzupełnij rozwiązanie według polecenia.')
