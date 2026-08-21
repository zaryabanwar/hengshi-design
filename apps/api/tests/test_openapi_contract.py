from fastapi.testclient import TestClient


def test_openapi_schema_exposes_core_routes(client: TestClient) -> None:
    response = client.get('/openapi.json')

    assert response.status_code == 200
    schema = response.json()
    paths = schema['paths']

    assert '/health' in paths
    assert '/api/auth/login' in paths
    assert '/api/services' in paths
    assert '/api/projects' in paths
    assert '/api/world' in paths
    assert '/api/leads' in paths


def test_admin_routes_require_security_scheme(client: TestClient) -> None:
    response = client.get('/openapi.json')

    assert response.status_code == 200
    schema = response.json()
    paths = schema['paths']

    assert paths['/api/admin/me']['get']['security']
    assert paths['/api/admin/services']['post']['security']
    assert paths['/api/admin/projects']['post']['security']
    assert paths['/api/admin/world/nodes']['post']['security']
