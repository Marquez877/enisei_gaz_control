from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models import User
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
SECRET_KEY = "supersecret"

def add_admin(username: str, password: str):
    db: Session = SessionLocal()
    try:
        hashed_password = pwd_context.hash(password)
        new_admin = User(username=username, password_hash=hashed_password, is_admin=True)
        db.add(new_admin)
        db.commit()
        db.refresh(new_admin)
        print(f"Admin user {username} added successfully.")
    except Exception as e:
        db.rollback()
        print(f"Error adding admin user: {e}")
    finally:
        db.close()

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 3:
        print("Usage: python add_admin.py <username> <password>")
    else:
        add_admin(sys.argv[1], sys.argv[2])