from fastapi import APIRouter, Depends
from sqlalchemy import select
from sqlalchemy.orm import Session, selectinload, with_loader_criteria

from app.db.session import get_db
from app.models.world import WorldHotspot, WorldNode
from app.world.schemas import WorldResponse

router = APIRouter()


@router.get('/world', response_model=WorldResponse)
def get_world(db: Session = Depends(get_db)) -> WorldResponse:
    stmt = (
        select(WorldNode)
        .options(
            selectinload(WorldNode.hotspots),
            with_loader_criteria(WorldHotspot, WorldHotspot.is_enabled.is_(True))
        )
        .order_by(WorldNode.sort_order.asc(), WorldNode.title.asc())
    )
    nodes = db.execute(stmt).scalars().all()
    return WorldResponse(nodes=nodes)
