from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from pydantic import BaseModel
from app.db.database import get_db
from app.schemas.user import UserCreate, UserResponse
from app.services import user_service
from app.repositories import user_repository
import hashlib

router = APIRouter(prefix="/users", tags=["Usuarios"])


class LoginRequest(BaseModel):
    username: str
    password: str


@router.post("/", response_model=UserResponse, status_code=201)
def register_user(user_data: UserCreate, db: Session = Depends(get_db)):
    return user_service.register_user(db, user_data)


@router.post("/login", response_model=UserResponse)
def login_user(data: LoginRequest, db: Session = Depends(get_db)):
    user = user_repository.get_user_by_username(db, data.username)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Usuario no encontrado")
    hashed = hashlib.sha256(data.password.encode()).hexdigest()
    if user.hashed_password != hashed:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail="Contraseña incorrecta")
    return user


@router.get("/{user_id}", response_model=UserResponse)
def get_user(user_id: int, db: Session = Depends(get_db)):
    return user_service.get_user_or_404(db, user_id)
