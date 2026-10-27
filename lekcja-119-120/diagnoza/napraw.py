from fastapi import FastAPI, HTTPException
app = FastAPI()
@app.post("/produkty", status_code=200)
def dodaj():
    return {"id": 1}
