import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

from app.db.database import Base, get_db
from app.main import app

TEST_DATABASE_URL = "sqlite:///:memory:"

engine = create_engine(
    TEST_DATABASE_URL,
    connect_args={"check_same_thread": False},
    poolclass=StaticPool,
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


@pytest.fixture(scope="function", autouse=True)
def setup_db():
    Base.metadata.create_all(bind=engine)
    yield
    Base.metadata.drop_all(bind=engine)


@pytest.fixture(scope="function")
def db_session():
    session = TestingSessionLocal()
    try:
        yield session
    finally:
        session.close()


@pytest.fixture(scope="function")
def client(db_session):
    def override_get_db():
        try:
            yield db_session
        finally:
            pass

    app.dependency_overrides[get_db] = override_get_db
    with TestClient(app) as c:
        yield c
    app.dependency_overrides.clear()


@pytest.fixture
def seed_stickers(db_session):
    from app.models.sticker import Sticker
    stickers = [
        Sticker(code="ARG1", section="Argentina", player_name="Lionel Messi"),
        Sticker(code="ARG2", section="Argentina", player_name="Ángel Di María"),
        Sticker(code="BRA1", section="Brasil", player_name="Vinicius Jr."),
        Sticker(code="EST1", section="Estadios", description="MetLife Stadium", is_special=True),
    ]
    db_session.add_all(stickers)
    db_session.commit()
    return stickers


@pytest.fixture
def registered_user(client):
    response = client.post("/api/v1/users/", json={
        "username": "testuser",
        "email": "test@example.com",
        "password": "secret123",
    })
    assert response.status_code == 201
    return response.json()
