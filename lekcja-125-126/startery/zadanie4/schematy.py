from pydantic import BaseModel

class AlbumWejscie(BaseModel):
    tytul: str
    pobrania: int
    # TODO: uzupełnij ograniczenia i pozostałe pola opisane w zadaniu.

class AlbumOdczyt(BaseModel):
    id: int
    tytul: str
    pobrania: int
    # TODO: uzupełnij ograniczenia i pozostałe pola opisane w zadaniu.

