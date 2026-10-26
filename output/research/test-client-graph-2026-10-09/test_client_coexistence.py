"""Prospective offline library-boundary probes; run only after native approval."""
import httpx
import httpx2
import pytest
from authlib.integrations.httpx_client import AsyncOAuth2Client
from fastapi import FastAPI
from fastapi.testclient import TestClient
from joserfc import jwt


def test_testclient_uses_httpx2_response_without_aliasing_httpx():
    app = FastAPI()

    @app.get('/synthetic')
    def synthetic():
        return {'kind': 'synthetic-library-probe'}

    with TestClient(app) as client:
        response = client.get('/synthetic')
        assert response.status_code == 200
        assert response.json() == {'kind': 'synthetic-library-probe'}
        assert isinstance(response, httpx2.Response)
        assert not isinstance(response, httpx.Response)


@pytest.mark.parametrize('name', ['HTTPError', 'TimeoutException'])
def test_exception_families_remain_distinct(name):
    new_type = getattr(httpx2, name)
    old_type = getattr(httpx, name)
    with pytest.raises(new_type) as caught:
        raise new_type('synthetic, no request sent')
    assert not isinstance(caught.value, old_type)


@pytest.mark.asyncio
async def test_authlib_prefers_httpx2_and_joserfc_imports():
    async with AsyncOAuth2Client() as client:
        assert isinstance(client, httpx2.AsyncClient)
        assert not isinstance(client, httpx.AsyncClient)
    assert callable(jwt.decode)
    # Import/type ownership only: no OIDC, token, TLS or provider interaction.
