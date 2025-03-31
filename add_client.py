from app.database import SessionLocal
from app.models import Client
from app.schemas import ClientCreate
from datetime import datetime, timezone

def add_client():
    name = input("Введите имя клиента: ")
    address = input("Введите адрес клиента: ")
    account_number = input("Введите лицевой счёт клиента: ")
    phone_number = int(input("Введите номер телефона клиента: "))
    balance = float(input("Введите начальный баланс (по умолчанию 0.0): ") or 0.0)
    subscription_fee = float(input("Введите абонентскую плату (по умолчанию 100.0): ") or 100.0)

    client_data = {
        "name": name,
        "address": address,
        "account_number": account_number,
        "phone_number": phone_number,
    }

    try:
        client_create = ClientCreate(**client_data)
    except ValueError as e:
        print(f"Ошибка валидации данных: {e}")
        return

    db = SessionLocal()

    new_client = Client(
        **client_create.model_dump(),
        balance=balance,
        subscription_fee=subscription_fee,
        last_fee_date=datetime.now(timezone.utc),
    )

    db.add(new_client)
    db.commit()
    db.close()
    print(f"Клиент {name} успешно добавлен!")

if __name__ == "__main__":
    add_client()