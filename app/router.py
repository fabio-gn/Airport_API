from fastapi import APIRouter, HTTPException
from typing import List
from .models import Aeroporto, AeroportoCreate, PaginatedResponse
from . import crud

router = APIRouter(prefix="/aeroporti", tags=["Aeroporti"])


@router.get("", response_model=PaginatedResponse)
def list_airports(page: int = 1, size: int = 5):
    return crud.get_airports(page, size)


@router.get("/{airport_id}", response_model=Aeroporto)
def get_airport(airport_id: int):
    airport = crud.get_airport(airport_id)
    if not airport:
        raise HTTPException(status_code=404, detail="Aeroporto non trovato")
    return airport


@router.post("", response_model=Aeroporto, status_code=201)
def create_airport(airport: AeroportoCreate):
    return crud.create_airport(airport.model_dump())


@router.delete("/{airport_id}", status_code=204)
def delete_airport(airport_id: int):
    deleted = crud.delete_airport(airport_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Aeroporto non trovato")