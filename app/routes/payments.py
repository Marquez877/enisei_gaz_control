from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..database import SessionLocal
from ..models import Client, Payment
from ..schemas import PaymentCreate, PaymentOut

router = APIRouter(prefix="/payments", tags=["Payments"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=PaymentOut)
def make_payment(payment: PaymentCreate, db: Session = Depends(get_db)):
    client = db.query(Client).filter(Client.id == payment.client_id).first()
    if client:
        client.balance += payment.amount
        new_payment = Payment(client_id=payment.client_id, amount=payment.amount)
        db.add(new_payment)
        db.add(client)
        db.commit()
        db.refresh(new_payment)
        return new_payment
    return {"error": "Client not found"}