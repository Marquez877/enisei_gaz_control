from pydantic import BaseModel, ConfigDict, validator
from typing import Optional
from datetime import datetime, timezone

class UserBase(BaseModel):
    username: str

class UserCreate(UserBase):
    password: str

class UserOut(UserBase):
    id: int
    is_admin: bool

    model_config = ConfigDict(from_attributes=True)

class ClientBase(BaseModel):
    name: str
    address: str
    account_number: str
    phone_number: int

    @validator('name')
    def name_must_not_be_empty(cls, v):
        if not v.strip():
            raise ValueError('Имя не должно быть пустым')
        return v

    @validator('account_number')
    def account_number_must_be_valid(cls, v):
        if not v.isdigit() or len(v) != 10:
            raise ValueError('Лицевой счёт должен состоять из 10 цифр')
        return v

class ClientCreate(ClientBase):
    pass

class ClientOut(ClientBase):
    id: int
    balance: float
    subscription_fee: float
    last_fee_date: datetime

    model_config = ConfigDict(from_attributes=True)

class PaymentBase(BaseModel):
    client_id: int
    amount: float

class PaymentCreate(PaymentBase):
    pass

class PaymentOut(PaymentBase):
    id: int

    model_config = ConfigDict(from_attributes=True)