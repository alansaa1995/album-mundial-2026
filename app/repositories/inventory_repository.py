from sqlalchemy.orm import Session, joinedload
from typing import List
from app.models.inventory import UserSticker


def get_user_inventory(db: Session, user_id: int) -> List[UserSticker]:
    return (
        db.query(UserSticker)
        .options(joinedload(UserSticker.sticker))
        .filter(UserSticker.user_id == user_id)
        .all()
    )


def get_user_sticker(db: Session, user_id: int, sticker_id: int) -> UserSticker | None:
    return (
        db.query(UserSticker)
        .filter(UserSticker.user_id == user_id, UserSticker.sticker_id == sticker_id)
        .first()
    )


def get_user_duplicates(db: Session, user_id: int) -> List[UserSticker]:
    """Returns stickers available for trade: either not pasted, or pasted with extras."""
    return (
        db.query(UserSticker)
        .options(joinedload(UserSticker.sticker))
        .filter(
            UserSticker.user_id == user_id,
            (UserSticker.is_pasted == False) | (UserSticker.quantity > 1),
        )
        .all()
    )


def get_pasted_count(db: Session, user_id: int) -> int:
    return (
        db.query(UserSticker)
        .filter(UserSticker.user_id == user_id, UserSticker.is_pasted == True)
        .count()
    )


def upsert_user_sticker(
    db: Session, user_id: int, sticker_id: int, mark_as_repeated: bool = False
) -> UserSticker:
    existing = get_user_sticker(db, user_id, sticker_id)

    if existing:
        existing.quantity += 1
        if not mark_as_repeated:
            existing.is_pasted = True
    else:
        existing = UserSticker(
            user_id=user_id,
            sticker_id=sticker_id,
            quantity=1,
            is_pasted=not mark_as_repeated,
        )
        db.add(existing)

    db.commit()
    db.refresh(existing)
    return existing
