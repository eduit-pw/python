# Temat 59. Zadanie 1. Usługa działa
# Starter do uzupełnienia, bez rozwiązania.
# Pełne polecenie: README lekcji.
# TODO: Utwórz main.py z GET /status według powyższej umowy i uruchom Uvicorn.
# TODO: Sprawdź /status w przeglądarce oraz przez Try it out w /docs.

from fastapi import FastAPI
app = FastAPI()

@app.get('/status')
def status():
    raise NotImplementedError('Uzupełnij rozwiązanie według polecenia.')
