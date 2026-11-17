from pydantic import BaseModel,ConfigDict,Field,field_validator
class AlbumWejscie(BaseModel):
    model_config=ConfigDict(extra="forbid")
    tytul:str=Field(min_length=1,max_length=80)
    pobrania:int=Field(ge=0,strict=True)
    @field_validator("tytul")
    @classmethod
    def sprawdz_tytul(cls,wartosc):
        wartosc=wartosc.strip()
        if not wartosc:raise ValueError("Tytuł jest pusty")
        return wartosc
class AlbumOdczyt(AlbumWejscie):
    id:int
