from sqlalchemy.orm import Session
from datetime import datetime, timedelta
from ..models import Client

def add_subscription_fees(db: Session):
    today = datetime.utcnow()
    clients = db.query(Client).all()

    for client in clients:
        if client.last_fee_date + timedelta(days=30) <= today:
            client.balance -= client.subscription_fee
            client.last_fee_date = today
            db.add(client)

    db.commit()