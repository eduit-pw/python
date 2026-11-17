# Temat 59. Zadanie 3. Opcjonalne query
# Starter do uzupełnienia, bez rozwiązania.
# Pełne polecenie: README lekcji.
# TODO: Dodaj /powitanie z parametrem imie: str = "Uczeń".
# TODO: Zwróć {"tekst": "Cześć, ..."}. Sprawdź brak parametru i imie=Anna.

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
