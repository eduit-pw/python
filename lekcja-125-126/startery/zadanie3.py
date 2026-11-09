# Zadanie 3. Brak rekordu
# Pełne wymagania i wyniki kontrolne: ../README.md
# Najpierw ustal wejście i wynik. Uzupełnij kod; ten plik jest starterem.

from pydantic import BaseModel, ConfigDict, Field, field_validator

class AlbumWejscie(BaseModel):
    tytul: str
    pobrania: int

    @field_validator('tytul')
    @classmethod
    def sprawdz_tytul(cls, wartosc):
        """TODO: uzupełnij zgodnie z kontraktem w README."""
        pass

class AlbumOdczyt(AlbumWejscie):
    id: int
