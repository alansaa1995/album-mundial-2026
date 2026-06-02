from pydantic import BaseModel
from typing import Optional


class StickerBase(BaseModel):
    code: str
    section: str
    player_name: Optional[str] = None
    description: Optional[str] = None
    is_special: bool = False


class StickerCreate(StickerBase):
    pass


class StickerResponse(StickerBase):
    id: int

    model_config = {"from_attributes": True}
