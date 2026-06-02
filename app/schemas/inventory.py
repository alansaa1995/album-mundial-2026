from pydantic import BaseModel
from datetime import datetime
from typing import List
from app.schemas.sticker import StickerResponse


class StickerActionRequest(BaseModel):
    sticker_code: str
    action: str  # "obtained" | "repeated"


class UserStickerResponse(BaseModel):
    id: int
    sticker: StickerResponse
    quantity: int
    is_pasted: bool
    obtained_at: datetime

    model_config = {"from_attributes": True}


class AlbumProgressResponse(BaseModel):
    user_id: int
    username: str
    total_stickers: int
    pasted_stickers: int
    completion_percentage: float
    duplicates: List[UserStickerResponse]
