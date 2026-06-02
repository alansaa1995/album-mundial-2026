from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from app.db.database import get_db
from app.schemas.sticker import StickerResponse
from app.repositories import sticker_repository

router = APIRouter(prefix="/stickers", tags=["Figuritas"])


@router.get("/", response_model=List[StickerResponse])
def list_stickers(db: Session = Depends(get_db)):
    return sticker_repository.get_all_stickers(db)


@router.get("/{code}", response_model=StickerResponse)
def get_sticker(code: str, db: Session = Depends(get_db)):
    sticker = sticker_repository.get_sticker_by_code(db, code)
    if not sticker:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Figurita '{code}' no encontrada",
        )
    return sticker
