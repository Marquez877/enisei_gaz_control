from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..database import SessionLocal
from ..models import Client, first_of_them
from ..schemas import ClientOut, ClientCreate

router = APIRouter(prefix="/clients", tags=["Clients"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

from fastapi import HTTPException

@router.get("/", response_model=list[ClientOut])
def get_clients(db: Session = Depends(get_db)):
    return db.query(first_of_them).all()

@router.post("/", response_model=ClientOut)
def create_client(client: ClientCreate, db: Session = Depends(get_db)):
    new_client = first_of_them(**client.model_dump(), balance=0.0)
    db.add(new_client)
    db.commit()
    db.refresh(new_client)
    return new_client