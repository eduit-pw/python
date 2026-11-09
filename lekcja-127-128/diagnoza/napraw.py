from fastapi import FastAPI, HTTPException
app = FastAPI()
@app.get("/stan")
def stan():
    return {"ok": True}
def sprawdz(client):
    response = client.get("/stan")
    return response.status_code == 200
