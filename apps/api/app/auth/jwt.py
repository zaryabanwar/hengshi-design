import os
from datetime import datetime, timedelta, timezone

import jwt


def get_jwt_secret() -> str:
    secret = os.getenv('JWT_SECRET')
    if not secret:
        raise RuntimeError('JWT_SECRET is not set')
    return secret


def get_jwt_expires_minutes() -> int:
    raw = os.getenv('JWT_EXPIRES_MINUTES', '120')
    try:
        return int(raw)
    except ValueError:
        return 120


def create_access_token(*, subject: str, email: str, role: str) -> str:
    expires_delta = timedelta(minutes=get_jwt_expires_minutes())
    expire_at = datetime.now(timezone.utc) + expires_delta
    payload = {
        'sub': subject,
        'email': email,
        'role': role,
        'exp': expire_at
    }
    return jwt.encode(payload, get_jwt_secret(), algorithm='HS256')


def decode_access_token(token: str) -> dict:
    return jwt.decode(token, get_jwt_secret(), algorithms=['HS256'])
