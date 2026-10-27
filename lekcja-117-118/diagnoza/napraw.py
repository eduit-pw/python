from fastapi import FastAPI, HTTPException
app = FastAPI()
dane = {1: {"nazwa": "A"}}
@app.get("/produkty/{id}")
def pobierz(id: int):
    return dane.get(id)
