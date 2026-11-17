from fastapi import FastAPI,HTTPException,Response
from schematy import AlbumWejscie,AlbumOdczyt
app=FastAPI()
albumy={}
kolejne_id=1
@app.get("/status")
def status():return {"stan":"ok"}
@app.get("/albumy",response_model=list[AlbumOdczyt])
def lista():return list(albumy.values())
@app.get("/albumy/{identyfikator}",response_model=AlbumOdczyt)
def odczyt(identyfikator:int):
    if identyfikator not in albumy:raise HTTPException(404,"Brak albumu")
    return albumy[identyfikator]
@app.post("/albumy",status_code=201,response_model=AlbumOdczyt)
def dodaj(album:AlbumWejscie):
    global kolejne_id
    wynik={"id":kolejne_id,**album.model_dump()}
    albumy[kolejne_id]=wynik
    kolejne_id+=1
    return wynik
@app.put("/albumy/{identyfikator}",response_model=AlbumOdczyt)
def zmien(identyfikator:int,album:AlbumWejscie):
    odczyt(identyfikator)
    wynik={"id":identyfikator,**album.model_dump()}
    albumy[identyfikator]=wynik
    return wynik
@app.delete("/albumy/{identyfikator}",status_code=204,response_class=Response)
def usun(identyfikator:int):
    odczyt(identyfikator)
    del albumy[identyfikator]
    return Response(status_code=204)
