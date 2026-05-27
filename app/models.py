from pydantic import BaseModel, Field
from typing import List


class Aeroporto(BaseModel):
    id: int
    codice: str
    citta: str

class AeroportoCreate(BaseModel):
    codice: str = Field(min_length=3, max_length=3)
    citta: str = Field(min_length=1)


class PaginatedResponse(BaseModel):
    page: int
    size: int
    total: int
    data: List[Aeroporto]
