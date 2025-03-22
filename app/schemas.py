from pydantic import BaseModel, ConfigDict
from typing import Optional

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

class ClientCreate(ClientBase):
    pass

class ClientOut(ClientBase):
    id: int
    balance: float

    model_config = ConfigDict(from_attributes=True)

class PaymentBase(BaseModel):
    client_id: int
    amount: float

class PaymentCreate(PaymentBase):
    pass

class PaymentOut(PaymentBase):
    id: int

    model_config = ConfigDict(from_attributes=True)