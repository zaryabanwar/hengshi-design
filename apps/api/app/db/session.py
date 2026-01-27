import os
from collections.abc import Generator
from pathlib import Path
from typing import Any

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.engine import Engine
from sqlalchemy.orm import Session, sessionmaker

load_dotenv(Path(__file__).resolve().parents[2] / '.env')


def get_database_url() -> str:
    return os.getenv('DATABASE_URL', 'sqlite:///./app.db')


def _get_connect_args(database_url: str) -> dict[str, Any]:
    if database_url.startswith('sqlite'):
        return {'check_same_thread': False}
    return {}


def create_db_engine() -> Engine:
    database_url = get_database_url()
    connect_args = _get_connect_args(database_url)
    return create_engine(database_url, pool_pre_ping=True, connect_args=connect_args)


engine = create_db_engine()
SessionLocal = sessionmaker(bind=engine, class_=Session, expire_on_commit=False)


def get_db() -> Generator[Session, None, None]:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
