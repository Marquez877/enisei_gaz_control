from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..database import SessionLocal
from ..models import Client
from ..schemas import ClientOut, ClientCreate
from ..dependencies import admin_required

router = APIRouter(prefix="/clients", tags=["Clients"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=list[ClientOut], dependencies=[Depends(admin_required)])
def get_clients(db: Session = Depends(get_db)):
    return db.query(Client).all()

@router.post("/", response_model=ClientOut, dependencies=[Depends(admin_required)])
def create_client(client: ClientCreate, db: Session = Depends(get_db)):
    new_client = Client(**client.model_dump(), balance=0.0)
    db.add(new_client)
    db.commit()
    db.refresh(new_client)
    return new_client