# Temat 59. Zadanie 2. Parametr liczbowy
# Starter do uzupełnienia, bez rozwiązania.
# Pełne polecenie: README lekcji.
# TODO: Dodaj /kwadrat/{liczba} z parametrem int. Zwróć liczbę i jej kwadrat.
# TODO: Wyślij wartości 5, -3 i abc. Nie przechwytuj błędu typu ręcznie.

from fastapi import FastAPI
app = FastAPI()

@app.get('/status')
def status():
    raise NotImplementedError('Uzupełnij rozwiązanie według polecenia.')

@app.get('/kwadrat/{liczba}')
def kwadrat(liczba: int):
    raise NotImplementedError('Uzupełnij rozwiązanie według polecenia.')
