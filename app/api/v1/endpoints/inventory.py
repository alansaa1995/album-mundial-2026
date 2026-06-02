from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from app.db.database import get_db
from app.schemas.inventory import StickerActionRequest, UserStickerResponse, AlbumProgressResponse
from app.services import inventory_service
from app.repositories import inventory_repository

router = APIRouter(prefix="/inventory", tags=["Inventario"])


@router.post("/{user_id}/sticker", response_model=UserStickerResponse, status_code=200)
def add_sticker_to_inventory(
    user_id: int,
    request: StickerActionRequest,
    db: Session = Depends(get_db),
):
    return inventory_service.process_sticker_action(db, user_id, request)


@router.get("/{user_id}/stickers", response_model=List[UserStickerResponse])
def get_user_stickers(user_id: int, db: Session = Depends(get_db)):
    return inventory_repository.get_user_inventory(db, user_id)


@router.get("/{user_id}/progress", response_model=AlbumProgressResponse)
def get_album_progress(user_id: int, db: Session = Depends(get_db)):
    return inventory_service.get_album_progress(db, user_id)
