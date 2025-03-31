from sqlalchemy import Column, Integer, String, Float, ForeignKey, Boolean, DateTime
from sqlalchemy.orm import relationship
from .database import Base
from datetime import datetime, timezone

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    password_hash = Column(String)
    is_admin = Column(Boolean, default=False)

class Client(Base):
    __tablename__ = "clients"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    address = Column(String)
    account_number = Column(String, unique=True, index=True)
    phone_number = Column(Integer)  # Изменено с Integer на String
    balance = Column(Float, default=0.0)
    subscription_fee = Column(Float, default=100.0)
    last_fee_date = Column(DateTime, default=lambda: datetime.now(timezone.utc))

class first_of_them(Base):
    __tablename__ = "Gaz Control Services"
    id = Column(Integer, primary_key=True, index=True)
    owner = Column(String)
    address = Column(String)
    number_of_apps = Column(Integer)
    subs = Column(String)
    subs_fee = Column(Integer, default=0.0)
    balance = Column(Float, default=0.0)
    last_fee_date = Column(DateTime, default=lambda: datetime.now(timezone.utc))

class Payment(Base):
    __tablename__ = "payments"
    id = Column(Integer, primary_key=True, index=True)
    client_id = Column(Integer, ForeignKey("clients.id"))
    amount = Column(Float)
    client = relationship("Client")