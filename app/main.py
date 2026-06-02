from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from contextlib import asynccontextmanager
from app.core.config import get_settings
from app.db.database import Base, engine
from app.api.v1.router import api_router
import app.models  # noqa: F401
import os

settings = get_settings()


def run_seed_if_empty():
    """Carga el catálogo solo si la tabla de figuritas está vacía."""
    try:
        from app.db.database import SessionLocal
        from app.models.sticker import Sticker
        db = SessionLocal()
        try:
            if db.query(Sticker).count() == 0:
                from scripts.seed_full import build_catalog
                stickers = [
                    Sticker(
                        code=s["code"].upper(),
                        section=s["section"],
                        player_name=s.get("player_name"),
                        description=s.get("description"),
                        is_special=s.get("is_special", False),
                    )
                    for s in build_catalog()
                ]
                db.add_all(stickers)
                db.commit()
                print(f"Seed: {len(stickers)} figuritas cargadas.")
            else:
                print("Seed: catálogo ya cargado, omitido.")
        finally:
            db.close()
    except Exception as e:
        print(f"Seed error (no crítico): {e}")


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Crear tablas y cargar seed al iniciar
    Base.metadata.create_all(bind=engine)
    run_seed_if_empty()
    yield


app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    description="Backend para gestión de figuritas del Mundial 2026",
    docs_url="/docs",
    redoc_url="/redoc",
    lifespan=lifespan,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router)

FRONTEND_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "frontend")
if os.path.isdir(FRONTEND_DIR):
    app.mount("/static", StaticFiles(directory=FRONTEND_DIR), name="static")


@app.get("/", tags=["Frontend"])
def serve_frontend():
    index = os.path.join(FRONTEND_DIR, "index.html")
    if os.path.isfile(index):
        return FileResponse(index)
    return {"status": "ok", "app": settings.APP_NAME}


@app.get("/health", tags=["Health"])
def health_check():
    return {"status": "healthy"}
