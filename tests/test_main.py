import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.database import SessionLocal, Base, engine
from app.models import Client
from sqlalchemy.orm import Session

client = TestClient(app)

@pytest.fixture(scope="function")
def db_session():
    """Создаёт чистую тестовую БД перед каждым тестом."""
    Base.metadata.drop_all(bind=engine)  # Очистка БД
    Base.metadata.create_all(bind=engine)  # Пересоздание БД
    db = SessionLocal()
    yield db
    db.close()

def test_create_client(db_session: Session):
    response = client.post("/clients/", json={"name": "Иван", "address": "ул. Ленина", "account_number": "1234567890", "phone_number": "+79991234567"})
    assert response.status_code == 200
    assert response.json()["name"] == "Иван"

def test_get_clients(db_session: Session):
    response = client.get("/clients/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)