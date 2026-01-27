from fastapi.testclient import TestClient
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.auth.password import hash_password
from app.leads import routes as leads_routes
from app.models.lead import Lead
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


def _login(client: TestClient) -> str:
    response = client.post(
        '/api/auth/login',
        json={'email': 'admin@example.com', 'password': 'password123'}
    )
    return response.json()['access_token']


def test_public_lead_create(client: TestClient, db_session: Session) -> None:
    payload = {
        'name': 'Ada Lovelace',
        'email': 'ada@example.com',
        'company': 'Analytical Engines',
        'phone': '+1-555-0100',
        'subject': 'Project inquiry',
        'message': 'We need a platform rebuild for a new product launch.',
        'source_url': 'https://hengshi.design/contact',
        'metadata': {'user_agent': 'pytest'}
    }

    response = client.post('/api/leads', json=payload)

    assert response.status_code == 201
    data = response.json()
    assert data['id']
    assert data['created_at']

    lead = db_session.execute(
        select(Lead).where(Lead.email == 'ada@example.com')
    ).scalar_one_or_none()
    assert lead is not None


def test_lead_rate_limit(client: TestClient) -> None:
    original_max = leads_routes.RATE_LIMIT_MAX_REQUESTS
    original_window = leads_routes.RATE_LIMIT_WINDOW_SECONDS

    leads_routes.RATE_LIMIT_MAX_REQUESTS = 1
    leads_routes.RATE_LIMIT_WINDOW_SECONDS = 600
    leads_routes.reset_rate_limiter()

    payload = {
        'name': 'Grace Hopper',
        'email': 'grace@example.com',
        'message': 'We want to explore an AI-assisted workflow for compliance.'
    }

    try:
        first = client.post('/api/leads', json=payload)
        second = client.post('/api/leads', json=payload)
    finally:
        leads_routes.RATE_LIMIT_MAX_REQUESTS = original_max
        leads_routes.RATE_LIMIT_WINDOW_SECONDS = original_window
        leads_routes.reset_rate_limiter()

    assert first.status_code == 201
    assert second.status_code == 429


def test_admin_leads_requires_auth(client: TestClient) -> None:
    response = client.get('/api/admin/leads')

    assert response.status_code == 401


def test_admin_leads_list_with_token(client: TestClient, db_session: Session) -> None:
    _create_admin_user(db_session)

    lead = Lead(
        name='Linus Torvalds',
        email='linus@example.com',
        company='Kernel Labs',
        phone=None,
        subject='Platform roadmap',
        message='We need a long-term engineering roadmap for scaling.',
        source_url=None,
        metadata_={'referrer': 'newsletter'}
    )
    db_session.add(lead)
    db_session.commit()

    token = _login(client)
    response = client.get(
        '/api/admin/leads',
        headers={'Authorization': f'Bearer {token}'}
    )

    assert response.status_code == 200
    data = response.json()
    assert len(data) == 1
    assert data[0]['email'] == 'linus@example.com'
