from app.database import SessionLocal
from app.models import Client
from datetime import datetime, timezone

# Функция для добавления клиента
def add_client():
    name = input("Введите имя клиента: ")
    address = input("Введите адрес клиента: ")
    account_number = input("Введите лицевой счёт клиента: ")
    balance = float(input("Введите начальный баланс (по умолчанию 0.0): ") or 0.0)
    subscription_fee = float(input("Введите абонентскую плату (по умолчанию 100.0): ") or 100.0)

    db = SessionLocal()

    new_client = Client(
        name=name,
        address=address,
        account_number=account_number,
        balance=balance,
        subscription_fee=subscription_fee,
        last_fee_date=datetime.now(timezone.utc),
    )

    db.add(new_client)
    db.commit()
    db.close()
    print(f"Клиент {name} успешно добавлен!")

# Запуск функции
if __name__ == "__main__":
    add_client()