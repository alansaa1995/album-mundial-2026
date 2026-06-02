from sqlalchemy import Column, Integer, ForeignKey, Boolean, DateTime, UniqueConstraint
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.db.database import Base


class UserSticker(Base):
    """
    Association table between User and Sticker.
    quantity > 1 means the user has duplicates available for trade.
    is_pasted = True means it's already in the album.
    """
    __tablename__ = "user_stickers"
    __table_args__ = (
        UniqueConstraint("user_id", "sticker_id", name="uq_user_sticker"),
    )

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False, index=True)
    sticker_id = Column(Integer, ForeignKey("stickers.id"), nullable=False, index=True)
    quantity = Column(Integer, default=1, nullable=False)
    is_pasted = Column(Boolean, default=False)  # pegada en el álbum
    obtained_at = Column(DateTime(timezone=True), server_default=func.now())

    user = relationship("User", back_populates="stickers")
    sticker = relationship("Sticker", back_populates="owners")
