from app.database import Base, engine

def reset_database():
    Base.metadata.drop_all(bind=engine)  # Удаление всех таблиц
    Base.metadata.create_all(bind=engine)  # Создание всех таблиц

if __name__ == "__main__":
    reset_database()