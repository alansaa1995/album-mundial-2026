from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from app.schemas.inventory import AlbumProgressResponse, StickerActionRequest
from app.models.inventory import UserSticker
from app.repositories import inventory_repository, sticker_repository, user_repository


def process_sticker_action(
    db: Session, user_id: int, request: StickerActionRequest
) -> UserSticker:
    user = user_repository.get_user_by_id(db, user_id)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Usuario no encontrado")

    sticker = sticker_repository.get_sticker_by_code(db, request.sticker_code)
    if not sticker:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Figurita '{request.sticker_code}' no encontrada en el catálogo",
        )

    if request.action not in ("obtained", "repeated"):
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail="La acción debe ser 'obtained' o 'repeated'",
        )

    mark_as_repeated = request.action == "repeated"
    return inventory_repository.upsert_user_sticker(db, user_id, sticker.id, mark_as_repeated)


def get_album_progress(db: Session, user_id: int) -> AlbumProgressResponse:
    user = user_repository.get_user_by_id(db, user_id)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Usuario no encontrado")

    total_stickers = sticker_repository.count_stickers(db)
    pasted_count = inventory_repository.get_pasted_count(db, user_id)
    duplicates = inventory_repository.get_user_duplicates(db, user_id)

    percentage = (pasted_count / total_stickers * 100) if total_stickers > 0 else 0.0

    return AlbumProgressResponse(
        user_id=user.id,
        username=user.username,
        total_stickers=total_stickers,
        pasted_stickers=pasted_count,
        completion_percentage=round(percentage, 2),
        duplicates=duplicates,
    )
