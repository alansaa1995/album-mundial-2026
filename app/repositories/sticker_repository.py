from sqlalchemy.orm import Session
from typing import List
from app.models.sticker import Sticker
from app.schemas.sticker import StickerCreate


def get_all_stickers(db: Session) -> List[Sticker]:
    return db.query(Sticker).all()


def get_sticker_by_code(db: Session, code: str) -> Sticker | None:
    return db.query(Sticker).filter(Sticker.code == code.upper()).first()


def get_sticker_by_id(db: Session, sticker_id: int) -> Sticker | None:
    return db.query(Sticker).filter(Sticker.id == sticker_id).first()


def create_sticker(db: Session, sticker_data: StickerCreate) -> Sticker:
    db_sticker = Sticker(
        code=sticker_data.code.upper(),
        section=sticker_data.section,
        player_name=sticker_data.player_name,
        description=sticker_data.description,
        is_special=sticker_data.is_special,
    )
    db.add(db_sticker)
    db.commit()
    db.refresh(db_sticker)
    return db_sticker


def bulk_create_stickers(db: Session, stickers_data: List[StickerCreate]) -> List[Sticker]:
    db_stickers = [
        Sticker(
            code=s.code.upper(),
            section=s.section,
            player_name=s.player_name,
            description=s.description,
            is_special=s.is_special,
        )
        for s in stickers_data
    ]
    db.add_all(db_stickers)
    db.commit()
    for s in db_stickers:
        db.refresh(s)
    return db_stickers


def count_stickers(db: Session) -> int:
    return db.query(Sticker).count()
