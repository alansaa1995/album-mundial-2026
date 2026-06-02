from fastapi import APIRouter
from app.api.v1.endpoints import users, stickers, inventory

api_router = APIRouter(prefix="/api/v1")
api_router.include_router(users.router)
api_router.include_router(stickers.router)
api_router.include_router(inventory.router)
