"""Synthetic public-library probes; import only in the authorized research venv.

These tests exercise library coupling, not Hengshi routes, identity or persistence.
"""
import asyncio
import io
import time
from datetime import UTC, datetime

import bcrypt
import jwt
import pytest
from alembic.migration import MigrationContext
from alembic.operations import Operations
from cryptography.hazmat.primitives.asymmetric import rsa
from fastapi import FastAPI
from fastapi.testclient import TestClient
from psycopg import pq
from pydantic import BaseModel, ConfigDict
from sqlalchemy import Column, Integer, create_engine, text
from uvicorn import Config


@pytest.fixture(scope="module")
def rsa_keys():
    return tuple(rsa.generate_private_key(public_exponent=65537, key_size=2048)
                 for _ in range(2))


@pytest.fixture
def synthetic_claims():
    return {"sub": "synthetic-staff", "iss": "https://issuer.example.invalid",
            "aud": "isolated-research", "exp": int(time.time()) + 120}


def decode_synthetic(token, key):
    return jwt.decode(token, key, algorithms=["RS256"],
                      issuer="https://issuer.example.invalid", audience="isolated-research",
                      options={"require": ["exp", "iss", "aud", "sub"]})


def test_rsa_signature_roundtrip(rsa_keys, synthetic_claims):
    token = jwt.encode(synthetic_claims, rsa_keys[0], algorithm="RS256")
    assert decode_synthetic(token, rsa_keys[0].public_key())["sub"] == "synthetic-staff"


def test_wrong_rsa_key_is_rejected(rsa_keys, synthetic_claims):
    token = jwt.encode(synthetic_claims, rsa_keys[0], algorithm="RS256")
    with pytest.raises(jwt.InvalidSignatureError):
        decode_synthetic(token, rsa_keys[1].public_key())


def test_wrong_audience_is_rejected(rsa_keys, synthetic_claims):
    token = jwt.encode({**synthetic_claims, "aud": "other-research"}, rsa_keys[0], algorithm="RS256")
    with pytest.raises(jwt.InvalidAudienceError):
        decode_synthetic(token, rsa_keys[0].public_key())


def test_expired_token_is_rejected(rsa_keys, synthetic_claims):
    token = jwt.encode({**synthetic_claims, "exp": 1}, rsa_keys[0], algorithm="RS256")
    with pytest.raises(jwt.ExpiredSignatureError):
        decode_synthetic(token, rsa_keys[0].public_key())


def test_unapproved_algorithm_is_rejected(rsa_keys, synthetic_claims):
    token = jwt.encode(synthetic_claims, b"synthetic-secret-for-library-probe-only", algorithm="HS256")
    with pytest.raises(jwt.InvalidAlgorithmError):
        decode_synthetic(token, rsa_keys[0].public_key())


class SyntheticInput(BaseModel):
    model_config = ConfigDict(strict=True, extra="forbid")
    count: int


class SyntheticOutput(BaseModel):
    count: int
    at: datetime


@pytest.fixture
def local_client():
    app = FastAPI()

    @app.post("/synthetic", response_model=SyntheticOutput)
    def synthetic(payload: SyntheticInput):
        return {"count": payload.count, "at": datetime(2030, 1, 1, tzinfo=UTC)}

    with TestClient(app) as client:
        yield client


def test_strict_request_and_utc_response(local_client):
    response = local_client.post("/synthetic", json={"count": 7})
    assert response.status_code == 200
    assert response.json() == {"count": 7, "at": "2030-01-01T00:00:00Z"}


@pytest.mark.parametrize("payload", [{"count": "7"}, {"count": 7, "unexpected": True}])
def test_invalid_request_is_rejected(local_client, payload):
    assert local_client.post("/synthetic", json=payload).status_code == 422


def test_sqlite_failure_rolls_back_and_next_transaction_works():
    engine = create_engine("sqlite+pysqlite:///:memory:")
    try:
        with engine.begin() as connection:
            connection.execute(text("CREATE TABLE synthetic_record (id INTEGER PRIMARY KEY)"))
        with pytest.raises(RuntimeError, match="intentional synthetic rollback"):
            with engine.begin() as connection:
                connection.execute(text("INSERT INTO synthetic_record (id) VALUES (1)"))
                raise RuntimeError("intentional synthetic rollback")
        with engine.connect() as connection:
            assert connection.execute(text("SELECT COUNT(*) FROM synthetic_record")).scalar_one() == 0
        with engine.begin() as connection:
            connection.execute(text("INSERT INTO synthetic_record (id) VALUES (2)"))
        with engine.connect() as connection:
            assert connection.execute(text("SELECT id FROM synthetic_record")).scalar_one() == 2
    finally:
        engine.dispose()


def test_alembic_offline_postgres_ddl():
    buffer = io.StringIO()
    context = MigrationContext.configure(dialect_name="postgresql",
                                         opts={"as_sql": True, "output_buffer": buffer})
    Operations(context).create_table("synthetic_record", Column("id", Integer, primary_key=True))
    ddl = buffer.getvalue()
    assert "CREATE TABLE synthetic_record" in ddl
    assert "PRIMARY KEY (id)" in ddl


def test_psycopg_binary_public_api_without_connection():
    assert pq.__impl__ == "binary"
    assert isinstance(pq.version(), int) and pq.version() > 0
    assert isinstance(pq.__build_version__, int) and pq.__build_version__ > 0


def test_bcrypt_password_verification_and_length_boundary():
    password = b"synthetic-library-password"
    hashed = bcrypt.hashpw(password, bcrypt.gensalt(rounds=4))
    assert bcrypt.checkpw(password, hashed)
    assert not bcrypt.checkpw(b"wrong-synthetic-password", hashed)
    with pytest.raises(ValueError):
        bcrypt.hashpw(b"x" * 73, bcrypt.gensalt(rounds=4))
    # Low work factor is test-only, not a production password-policy choice.


def test_uvicorn_configuration_loads_without_listener():
    config = Config(FastAPI(), loop="asyncio", http="h11", ws="none", lifespan="off",
                    log_config=None, access_log=False)
    config.load()
    assert config.loaded


@pytest.mark.asyncio
async def test_actual_async_test_plugin():
    await asyncio.sleep(0)
    assert asyncio.get_running_loop().is_running()
