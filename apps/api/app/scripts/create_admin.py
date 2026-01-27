import os

from sqlalchemy import select

from app.auth.password import hash_password
from app.db.session import SessionLocal
from app.models.user import User


def main() -> None:
    email = os.getenv('ADMIN_EMAIL')
    password = os.getenv('ADMIN_PASSWORD')

    if not email or not password:
        raise SystemExit('ADMIN_EMAIL and ADMIN_PASSWORD must be set')

    db = SessionLocal()
    try:
        existing = db.execute(select(User).where(User.email == email)).scalar_one_or_none()
        if existing:
            print(f'Admin user already exists: {existing.email}')
            return

        user = User(email=email, password_hash=hash_password(password))
        db.add(user)
        db.commit()
        db.refresh(user)
        print(f'Created admin user: {user.email} ({user.id})')
    finally:
        db.close()


if __name__ == '__main__':
    main()
