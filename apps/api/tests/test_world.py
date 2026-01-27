from fastapi.testclient import TestClient
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.auth.password import hash_password
from app.models.user import User
from app.models.world import WorldHotspot, WorldNode
from app.scripts.seed_world import seed_world


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


def test_seed_world_idempotent(db_session: Session) -> None:
    created_nodes, created_hotspots = seed_world(db_session)
    assert created_nodes == 11
    assert created_hotspots == 21

    created_nodes_again, created_hotspots_again = seed_world(db_session)
    assert created_nodes_again == 0
    assert created_hotspots_again == 0

    nodes = db_session.execute(select(WorldNode)).scalars().all()
    hotspots = db_session.execute(select(WorldHotspot)).scalars().all()
    assert len(nodes) == 11
    assert len(hotspots) == 21


def test_public_world_response(client: TestClient, db_session: Session) -> None:
    seed_world(db_session)

    response = client.get('/api/world')

    assert response.status_code == 200
    payload = response.json()
    assert len(payload['nodes']) == 11
    assert payload['nodes'][0]['hotspots']


def test_admin_world_nodes_requires_auth(client: TestClient) -> None:
    response = client.get('/api/admin/world/nodes')

    assert response.status_code == 401


def test_admin_create_world_node(client: TestClient, db_session: Session) -> None:
    _create_admin_user(db_session)
    token = _login(client)

    payload = {
        'key': 'custom_room',
        'title': 'Custom Room',
        'description': 'A custom world node for tests.',
        'is_entry': False,
        'sort_order': 10,
        'camera_position': [0.0, 1.6, 6.0],
        'camera_target': [0.0, 1.6, 0.0],
        'camera_fov': 50,
        'environment': {'preset': 'neutral'}
    }

    response = client.post(
        '/api/admin/world/nodes',
        json=payload,
        headers={'Authorization': f'Bearer {token}'}
    )

    assert response.status_code == 201
    data = response.json()
    assert data['key'] == 'custom_room'
