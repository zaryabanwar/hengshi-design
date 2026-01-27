from fastapi.testclient import TestClient
from sqlalchemy.orm import Session

from app.auth.password import hash_password
from app.models.project import Project, ProjectMedia
from app.models.user import User
from app.scripts.seed_projects import seed_projects


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


def test_public_projects_list(client: TestClient, db_session: Session) -> None:
    project = Project(
        slug='project-list',
        title='Project List',
        summary='A summary that is long enough for tests.',
        body='A body that is definitely long enough to satisfy validation.',
        tags=['demo'],
        is_featured=True,
        sort_order=0
    )
    db_session.add(project)
    db_session.commit()

    response = client.get('/api/projects')

    assert response.status_code == 200
    data = response.json()
    assert len(data) == 1
    assert data[0]['slug'] == 'project-list'


def test_public_project_detail_includes_media(client: TestClient, db_session: Session) -> None:
    project = Project(
        slug='project-detail',
        title='Project Detail',
        summary='A summary that is long enough for tests.',
        body='A body that is definitely long enough to satisfy validation.',
        tags=None,
        is_featured=False,
        sort_order=1
    )
    db_session.add(project)
    db_session.flush()

    db_session.add_all([
        ProjectMedia(
            project_id=project.id,
            type='image',
            url='https://example.com/image.jpg',
            caption='Hero',
            sort_order=1
        ),
        ProjectMedia(
            project_id=project.id,
            type='video',
            url='https://example.com/video.mp4',
            caption='Walkthrough',
            sort_order=0
        )
    ])
    db_session.commit()

    response = client.get('/api/projects/project-detail')

    assert response.status_code == 200
    data = response.json()
    assert data['slug'] == 'project-detail'
    assert len(data['media']) == 2
    assert data['media'][0]['url'] == 'https://example.com/video.mp4'


def test_admin_project_create_requires_auth(client: TestClient) -> None:
    payload = {
        'slug': 'admin-project',
        'title': 'Admin Project',
        'summary': 'A summary that is long enough for tests.',
        'body': 'A body that is definitely long enough to satisfy validation.',
        'tags': ['admin'],
        'is_featured': True,
        'sort_order': 0
    }

    response = client.post('/api/admin/projects', json=payload)

    assert response.status_code == 401


def test_admin_project_create_with_token(client: TestClient, db_session: Session) -> None:
    _create_admin_user(db_session)
    token = _login(client)

    payload = {
        'slug': 'admin-project',
        'title': 'Admin Project',
        'summary': 'A summary that is long enough for tests.',
        'body': 'A body that is definitely long enough to satisfy validation.',
        'tags': ['admin'],
        'is_featured': True,
        'sort_order': 0
    }

    response = client.post(
        '/api/admin/projects',
        json=payload,
        headers={'Authorization': f'Bearer {token}'}
    )

    assert response.status_code == 201
    data = response.json()
    assert data['slug'] == 'admin-project'


def test_admin_project_media_crud(client: TestClient, db_session: Session) -> None:
    _create_admin_user(db_session)
    token = _login(client)

    project = Project(
        slug='media-project',
        title='Media Project',
        summary='A summary that is long enough for tests.',
        body='A body that is definitely long enough to satisfy validation.',
        tags=None,
        is_featured=False,
        sort_order=0
    )
    db_session.add(project)
    db_session.commit()

    media_payload = {
        'type': 'image',
        'url': 'https://example.com/media.jpg',
        'caption': 'First',
        'sort_order': 0
    }

    create_response = client.post(
        f'/api/admin/projects/{project.id}/media',
        json=media_payload,
        headers={'Authorization': f'Bearer {token}'}
    )
    assert create_response.status_code == 201
    media_id = create_response.json()['id']

    update_response = client.put(
        f'/api/admin/projects/{project.id}/media/{media_id}',
        json={'caption': 'Updated', 'sort_order': 1},
        headers={'Authorization': f'Bearer {token}'}
    )
    assert update_response.status_code == 200
    assert update_response.json()['caption'] == 'Updated'

    delete_response = client.delete(
        f'/api/admin/projects/{project.id}/media/{media_id}',
        headers={'Authorization': f'Bearer {token}'}
    )
    assert delete_response.status_code == 204


def test_seed_projects(client: TestClient, db_session: Session) -> None:
    created = seed_projects(db_session)
    assert created == 6

    response = client.get('/api/projects')
    assert response.status_code == 200
    assert len(response.json()) >= 6
