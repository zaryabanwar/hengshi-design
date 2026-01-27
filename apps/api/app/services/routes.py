from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy import or_, select
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.models.service import Service
from app.services.schemas import ServiceCategory, ServiceOut

router = APIRouter()


@router.get('/services', response_model=list[ServiceOut])
def list_services(
    category: ServiceCategory | None = None,
    featured: bool | None = None,
    q: str | None = None,
    limit: int = Query(default=50, ge=0),
    offset: int = Query(default=0, ge=0),
    db: Session = Depends(get_db)
) -> list[ServiceOut]:
    stmt = select(Service)

    if category is not None:
        stmt = stmt.where(Service.category == category.value)

    if featured is not None:
        stmt = stmt.where(Service.is_featured == featured)

    if q and q.strip():
        pattern = f"%{q.strip()}%"
        stmt = stmt.where(
            or_(
                Service.title.ilike(pattern),
                Service.summary.ilike(pattern),
                Service.body.ilike(pattern)
            )
        )

    stmt = (
        stmt.order_by(Service.sort_order.asc(), Service.title.asc())
        .limit(limit)
        .offset(offset)
    )

    services = db.execute(stmt).scalars().all()
    return services


@router.get('/services/{slug}', response_model=ServiceOut)
def get_service(slug: str, db: Session = Depends(get_db)) -> ServiceOut:
    service = db.execute(
        select(Service).where(Service.slug == slug)
    ).scalar_one_or_none()

    if not service:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Service not found')

    return service
