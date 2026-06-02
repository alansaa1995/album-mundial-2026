from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship
from app.db.database import Base


class Sticker(Base):
    __tablename__ = "stickers"

    id = Column(Integer, primary_key=True, index=True)
    code = Column(String(20), unique=True, nullable=False, index=True)  # e.g. ARG1, BRA5
    section = Column(String(50), nullable=False)                        # e.g. Argentina, Brasil, Estadios
    player_name = Column(String(100), nullable=True)
    description = Column(String(255), nullable=True)
    is_special = Column(Boolean, default=False)                         # foil/brillante

    owners = relationship("UserSticker", back_populates="sticker", cascade="all, delete-orphan")
