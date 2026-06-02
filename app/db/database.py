from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from app.core.config import get_settings

settings = get_settings()

# Railway provee DATABASE_URL con prefijo postgres://, SQLAlchemy necesita postgresql://
db_url = settings.DATABASE_URL.replace("postgres://", "postgresql://", 1)

# SQLite necesita check_same_thread=False; PostgreSQL no acepta ese argumento
connect_args = {"check_same_thread": False} if db_url.startswith("sqlite") else {}

engine = create_engine(db_url, connect_args=connect_args)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
