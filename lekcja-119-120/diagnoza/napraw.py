from pydantic import BaseModel, Field, ValidationError
class Produkt(BaseModel):
    cena: float = Field(ge=0)
