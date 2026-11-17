# Temat 59. Zadanie 4. Dla chętnych: Różne błędy HTTP
# Starter do uzupełnienia, bez rozwiązania.
# Pełne polecenie: README lekcji.
# TODO: Wyślij GET /brak, POST /status i GET /kwadrat/abc.
# TODO: Zapisz metodę, URL, status i krótki opis przyczyny każdego wyniku.

from fastapi import FastAPI
app = FastAPI()

@app.get('/status')
def status():
    raise NotImplementedError('Uzupełnij rozwiązanie według polecenia.')

@app.get('/kwadrat/{liczba}')
def kwadrat(liczba: int):
    raise NotImplementedError('Uzupełnij rozwiązanie według polecenia.')

@app.get('/powitanie')
def powitanie(imie: str='Uczeń'):
    raise NotImplementedError('Uzupełnij rozwiązanie według polecenia.')
