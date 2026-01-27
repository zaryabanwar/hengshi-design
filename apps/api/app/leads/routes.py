from __future__ import annotations

import os
import time
from collections import defaultdict
from threading import Lock

from fastapi import APIRouter, Depends, HTTPException, Request, status
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.leads.schemas import LeadCreate, LeadCreated
from app.models.lead import Lead

router = APIRouter()

RATE_LIMIT_MAX_REQUESTS = int(os.getenv('LEAD_RATE_LIMIT_MAX_REQUESTS', '5'))
RATE_LIMIT_WINDOW_SECONDS = int(os.getenv('LEAD_RATE_LIMIT_WINDOW_SECONDS', '600'))
_RATE_LIMIT_BUCKETS: dict[str, list[float]] = defaultdict(list)
_RATE_LIMIT_LOCK = Lock()


def _get_client_key(request: Request) -> str:
    forwarded = request.headers.get('x-forwarded-for')
    if forwarded:
        ip = forwarded.split(',')[0].strip()
        if ip:
            return ip

    if request.client and request.client.host:
        return request.client.host

    return 'shared'


def _allow_request(key: str) -> bool:
    now = time.monotonic()
    window_start = now - RATE_LIMIT_WINDOW_SECONDS

    with _RATE_LIMIT_LOCK:
        timestamps = _RATE_LIMIT_BUCKETS.get(key, [])
        timestamps = [ts for ts in timestamps if ts > window_start]
        if len(timestamps) >= RATE_LIMIT_MAX_REQUESTS:
            _RATE_LIMIT_BUCKETS[key] = timestamps
            return False

        timestamps.append(now)
        _RATE_LIMIT_BUCKETS[key] = timestamps

    return True


def reset_rate_limiter() -> None:
    with _RATE_LIMIT_LOCK:
        _RATE_LIMIT_BUCKETS.clear()


@router.post('/leads', response_model=LeadCreated, status_code=status.HTTP_201_CREATED)
def create_lead(
    payload: LeadCreate,
    request: Request,
    db: Session = Depends(get_db)
) -> LeadCreated:
    key = _get_client_key(request)
    if not _allow_request(key):
        raise HTTPException(
            status_code=status.HTTP_429_TOO_MANY_REQUESTS,
            detail='Rate limit exceeded. Please try again later.'
        )

    data = payload.model_dump(mode='json', exclude_none=True)
    metadata = data.pop('metadata', None)
    lead = Lead(**data, metadata_=metadata)
    db.add(lead)
    db.commit()
    db.refresh(lead)
    return LeadCreated(id=lead.id, created_at=lead.created_at)

