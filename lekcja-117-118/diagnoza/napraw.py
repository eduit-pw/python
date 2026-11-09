from fastapi import FastAPI, HTTPException
app = FastAPI()
@app.get("/suma")
def suma(a: str, b: str):
    return {"wynik": a + b}
