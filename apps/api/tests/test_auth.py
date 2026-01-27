from fastapi.testclient import TestClient
from sqlalchemy.orm import Session

from app.auth.password import hash_password
from app.models.user import User


def _create_admin_user(db: Session) -> User:
    user = User(
        email='admin@example.com',
        password_hash=hash_password('password123'),
        role='admin',
        is_active=True
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


def test_login_success(client: TestClient, db_session: Session) -> None:
    _create_admin_user(db_session)

    response = client.post(
        '/api/auth/login',
        json={'email': 'admin@example.com', 'password': 'password123'}
    )

    assert response.status_code == 200
    payload = response.json()
    assert payload['token_type'] == 'bearer'
    assert payload['access_token']


def test_admin_me_with_token(client: TestClient, db_session: Session) -> None:
    _create_admin_user(db_session)

    login_response = client.post(
        '/api/auth/login',
        json={'email': 'admin@example.com', 'password': 'password123'}
    )
    token = login_response.json()['access_token']

    response = client.get(
        '/api/admin/me',
        headers={'Authorization': f'Bearer {token}'}
    )

    assert response.status_code == 200
    data = response.json()
    assert data['email'] == 'admin@example.com'
    assert data['role'] == 'admin'
    assert data['is_active'] is True


def test_admin_me_without_token(client: TestClient) -> None:
    response = client.get('/api/admin/me')

    assert response.status_code == 401
