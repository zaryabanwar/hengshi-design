from fastapi.testclient import TestClient
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.auth.password import hash_password
from app.models.service import Service
from app.models.user import User
from app.scripts.seed_services import seed_services


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


def test_public_services_list(client: TestClient, db_session: Session) -> None:
    service = Service(
        slug='sample-service',
        title='Sample Service',
        category='strategy_architecture',
        summary='A summary that is long enough.',
        body='A body that is definitely long enough to pass validation.',
        deliverables=['Deliverable one'],
        tags=['sample'],
        is_featured=True,
        sort_order=0
    )
    db_session.add(service)
    db_session.commit()

    response = client.get('/api/services')

    assert response.status_code == 200
    data = response.json()
    assert len(data) == 1
    assert data[0]['slug'] == 'sample-service'


def test_public_service_detail(client: TestClient, db_session: Session) -> None:
    service = Service(
        slug='detail-service',
        title='Detail Service',
        category='platform_engineering',
        summary='A summary that is long enough.',
        body='A body that is definitely long enough to pass validation.',
        deliverables=['Deliverable one'],
        tags=None,
        is_featured=False,
        sort_order=1
    )
    db_session.add(service)
    db_session.commit()

    response = client.get('/api/services/detail-service')

    assert response.status_code == 200
    data = response.json()
    assert data['slug'] == 'detail-service'


def test_admin_create_requires_auth(client: TestClient) -> None:
    payload = {
        'slug': 'admin-created',
        'title': 'Admin Created Service',
        'category': 'ai_systems',
        'summary': 'A summary that is long enough.',
        'body': 'A body that is definitely long enough to pass validation.',
        'deliverables': ['Deliverable one'],
        'tags': ['admin'],
        'is_featured': True,
        'sort_order': 0
    }

    response = client.post('/api/admin/services', json=payload)

    assert response.status_code == 401


def test_admin_create_with_token(client: TestClient, db_session: Session) -> None:
    _create_admin_user(db_session)
    login_response = client.post(
        '/api/auth/login',
        json={'email': 'admin@example.com', 'password': 'password123'}
    )
    token = login_response.json()['access_token']

    payload = {
        'slug': 'admin-created',
        'title': 'Admin Created Service',
        'category': 'ai_systems',
        'summary': 'A summary that is long enough.',
        'body': 'A body that is definitely long enough to pass validation.',
        'deliverables': ['Deliverable one'],
        'tags': ['admin'],
        'is_featured': True,
        'sort_order': 0
    }

    response = client.post(
        '/api/admin/services',
        json=payload,
        headers={'Authorization': f'Bearer {token}'}
    )

    assert response.status_code == 201
    data = response.json()
    assert data['slug'] == 'admin-created'


def test_seed_services(db_session: Session) -> None:
    created = seed_services(db_session)
    services = db_session.execute(select(Service)).scalars().all()

    assert created == 9
    assert len(services) == 9
