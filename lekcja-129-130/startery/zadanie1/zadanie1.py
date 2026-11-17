from contextlib import asynccontextmanager
from fastapi import FastAPI,HTTPException,Response
import baza
from schematy import AlbumWejscie,AlbumOdczyt
@asynccontextmanager
async def lifespan(app):
    baza.inicjalizuj()
    yield
app=FastAPI(lifespan=lifespan)
@app.get("/status")
def status():return {"stan":"ok"}
@app.get("/albumy",response_model=list[AlbumOdczyt])
def lista():return baza.wszystkie()
@app.get("/albumy/{identyfikator}",response_model=AlbumOdczyt)
def odczyt(identyfikator:int):
    wynik=baza.znajdz(identyfikator)
    if wynik is None:raise HTTPException(404,"Brak albumu")
    return wynik
@app.post("/albumy",status_code=201,response_model=AlbumOdczyt)
def dodaj(album:AlbumWejscie):
    return baza.dodaj(album.tytul,album.pobrania)
@app.put("/albumy/{identyfikator}",response_model=AlbumOdczyt)
def zmien(identyfikator:int,album:AlbumWejscie):
    if not baza.zmien(identyfikator,album.tytul,album.pobrania):raise HTTPException(404,"Brak albumu")
    return {"id":identyfikator,**album.model_dump()}
@app.delete("/albumy/{identyfikator}",status_code=204,response_class=Response)
def usun(identyfikator:int):
    if not baza.usun(identyfikator):raise HTTPException(404,"Brak albumu")
    return Response(status_code=204)
