from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy import or_, select
from sqlalchemy.orm import Session, selectinload

from app.auth.deps import get_current_user, require_admin
from app.auth.schemas import AdminMeResponse
from app.db.session import get_db
from app.leads.schemas import LeadOut
from app.models.lead import Lead
from app.models.project import Project, ProjectMedia
from app.models.service import Service
from app.models.user import User
from app.models.world import WorldHotspot, WorldNode
from app.projects.schemas import (
    ProjectCreate,
    ProjectMediaCreate,
    ProjectMediaOut,
    ProjectMediaUpdate,
    ProjectOut,
    ProjectUpdate
)
from app.services.schemas import ServiceCreate, ServiceOut, ServiceUpdate
from app.world.schemas import (
    WorldHotspotCreate,
    WorldHotspotOut,
    WorldHotspotUpdate,
    WorldNodeCreate,
    WorldNodeOut,
    WorldNodeUpdate
)

router = APIRouter()


@router.get('/me', response_model=AdminMeResponse)
def read_me(current_user: User = Depends(get_current_user)) -> AdminMeResponse:
    return AdminMeResponse(
        id=current_user.id,
        email=current_user.email,
        role=current_user.role,
        is_active=current_user.is_active
    )


@router.get('/world/nodes', response_model=list[WorldNodeOut])
def list_world_nodes(
    db: Session = Depends(get_db),
    current_user: User = Depends(require_admin)
) -> list[WorldNodeOut]:
    nodes = db.execute(
        select(WorldNode)
        .options(selectinload(WorldNode.hotspots))
        .order_by(WorldNode.sort_order.asc(), WorldNode.title.asc())
    ).scalars().all()
    return nodes


@router.post('/world/nodes', response_model=WorldNodeOut, status_code=status.HTTP_201_CREATED)
def create_world_node(
    payload: WorldNodeCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_admin)
) -> WorldNodeOut:
    existing = db.execute(
        select(WorldNode).where(WorldNode.key == payload.key)
    ).scalar_one_or_none()
    if existing:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail='World node key already exists'
        )

    node = WorldNode(**payload.model_dump(mode='json'))
    db.add(node)
    db.commit()
    db.refresh(node)
    return node


@router.put('/world/nodes/{node_id}', response_model=WorldNodeOut)
def update_world_node(
    node_id: str,
    payload: WorldNodeUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_admin)
) -> WorldNodeOut:
    node = db.get(WorldNode, node_id)
    if not node:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='World node not found'
        )

    data = payload.model_dump(mode='json', exclude_unset=True)
    if 'key' in data:
        existing = db.execute(
            select(WorldNode).where(
                WorldNode.key == data['key'],
                WorldNode.id != node_id
            )
        ).scalar_one_or_none()
        if existing:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail='World node key already exists'
            )

    for key, value in data.items():
        setattr(node, key, value)

    db.commit()
    db.refresh(node)
    return node


@router.delete('/world/nodes/{node_id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_world_node(
    node_id: str,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_admin)
) -> None:
    node = db.get(WorldNode, node_id)
    if not node:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='World node not found'
        )

    db.delete(node)
    db.commit()
    return None


@router.get('/world/hotspots', response_model=list[WorldHotspotOut])
def list_world_hotspots(
    node_key: str | None = None,
    node_id: str | None = None,
    limit: int = Query(default=100, ge=0),
    offset: int = Query(default=0, ge=0),
    db: Session = Depends(get_db),
    current_user: User = Depends(require_admin)
) -> list[WorldHotspotOut]:
    stmt = select(WorldHotspot)

    if node_key:
        node = db.execute(
            select(WorldNode).where(WorldNode.key == node_key)
        ).scalar_one_or_none()
        if not node:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail='World node not found'
            )
        stmt = stmt.where(WorldHotspot.node_id == node.id)
    elif node_id:
        stmt = stmt.where(WorldHotspot.node_id == node_id)

    stmt = stmt.order_by(WorldHotspot.sort_order.asc(), WorldHotspot.title.asc())
    if limit:
        stmt = stmt.limit(limit)
    stmt = stmt.offset(offset)

    hotspots = db.execute(stmt).scalars().all()
    return hotspots


@router.post('/world/hotspots', response_model=WorldHotspotOut, status_code=status.HTTP_201_CREATED)
def create_world_hotspot(
    payload: WorldHotspotCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_admin)
) -> WorldHotspotOut:
    node = db.get(WorldNode, payload.node_id)
    if not node:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='World node not found'
        )

    existing = db.execute(
        select(WorldHotspot).where(
            WorldHotspot.node_id == payload.node_id,
            WorldHotspot.key == payload.key
        )
    ).scalar_one_or_none()
    if existing:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail='World hotspot key already exists for node'
        )

    hotspot = WorldHotspot(**payload.model_dump(mode='json'))
    db.add(hotspot)
    db.commit()
    db.refresh(hotspot)
    return hotspot


@router.put('/world/hotspots/{hotspot_id}', response_model=WorldHotspotOut)
def update_world_hotspot(
    hotspot_id: str,
    payload: WorldHotspotUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_admin)
) -> WorldHotspotOut:
    hotspot = db.get(WorldHotspot, hotspot_id)
    if not hotspot:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='World hotspot not found'
        )

    data = payload.model_dump(mode='json', exclude_unset=True)
    if 'key' in data:
        existing = db.execute(
            select(WorldHotspot).where(
                WorldHotspot.node_id == hotspot.node_id,
                WorldHotspot.key == data['key'],
                WorldHotspot.id != hotspot_id
            )
        ).scalar_one_or_none()
        if existing:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail='World hotspot key already exists for node'
            )

    for key, value in data.items():
        setattr(hotspot, key, value)

    db.commit()
    db.refresh(hotspot)
    return hotspot


@router.delete('/world/hotspots/{hotspot_id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_world_hotspot(
    hotspot_id: str,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_admin)
) -> None:
    hotspot = db.get(WorldHotspot, hotspot_id)
    if not hotspot:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='World hotspot not found'
        )

    db.delete(hotspot)
    db.commit()
    return None


@router.get('/leads', response_model=list[LeadOut])
def list_leads(
    q: str | None = None,
    limit: int = Query(default=50, ge=0),
    offset: int = Query(default=0, ge=0),
    db: Session = Depends(get_db),
    current_user: User = Depends(require_admin)
) -> list[LeadOut]:
    stmt = select(Lead)

    if q and q.strip():
        pattern = f"%{q.strip()}%"
        stmt = stmt.where(
            or_(
                Lead.name.ilike(pattern),
                Lead.email.ilike(pattern),
                Lead.company.ilike(pattern),
                Lead.subject.ilike(pattern),
                Lead.message.ilike(pattern)
            )
        )

    stmt = stmt.order_by(Lead.created_at.desc()).offset(offset)
    if limit:
        stmt = stmt.limit(limit)

    leads = db.execute(stmt).scalars().all()
    return leads


@router.get('/services', response_model=list[ServiceOut])
def list_services(
    db: Session = Depends(get_db),
    current_user: User = Depends(require_admin)
) -> list[ServiceOut]:
    services = db.execute(
        select(Service).order_by(Service.sort_order.asc(), Service.title.asc())
    ).scalars().all()
    return services


@router.post('/services', response_model=ServiceOut, status_code=status.HTTP_201_CREATED)
def create_service(
    payload: ServiceCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_admin)
) -> ServiceOut:
    existing = db.execute(
        select(Service).where(Service.slug == payload.slug)
    ).scalar_one_or_none()
    if existing:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail='Service slug already exists'
        )

    data = payload.model_dump(mode='json')
    service = Service(**data)
    db.add(service)
    db.commit()
    db.refresh(service)
    return service


@router.put('/services/{service_id}', response_model=ServiceOut)
def update_service(
    service_id: str,
    payload: ServiceUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_admin)
) -> ServiceOut:
    service = db.get(Service, service_id)
    if not service:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Service not found'
        )

    data = payload.model_dump(mode='json', exclude_unset=True)
    if 'slug' in data:
        existing = db.execute(
            select(Service).where(
                Service.slug == data['slug'],
                Service.id != service_id
            )
        ).scalar_one_or_none()
        if existing:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail='Service slug already exists'
            )

    for key, value in data.items():
        setattr(service, key, value)

    db.commit()
    db.refresh(service)
    return service


@router.delete('/services/{service_id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_service(
    service_id: str,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_admin)
) -> None:
    service = db.get(Service, service_id)
    if not service:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Service not found'
        )

    db.delete(service)
    db.commit()
    return None


@router.get('/projects', response_model=list[ProjectOut])
def list_projects(
    db: Session = Depends(get_db),
    current_user: User = Depends(require_admin)
) -> list[ProjectOut]:
    projects = db.execute(
        select(Project)
        .options(selectinload(Project.media))
        .order_by(Project.sort_order.asc(), Project.title.asc())
    ).scalars().all()
    return projects


@router.post('/projects', response_model=ProjectOut, status_code=status.HTTP_201_CREATED)
def create_project(
    payload: ProjectCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_admin)
) -> ProjectOut:
    existing = db.execute(
        select(Project).where(Project.slug == payload.slug)
    ).scalar_one_or_none()
    if existing:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail='Project slug already exists'
        )

    project = Project(**payload.model_dump(mode='json'))
    db.add(project)
    db.commit()
    db.refresh(project)
    return project


@router.put('/projects/{project_id}', response_model=ProjectOut)
def update_project(
    project_id: str,
    payload: ProjectUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_admin)
) -> ProjectOut:
    project = db.get(Project, project_id)
    if not project:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Project not found'
        )

    data = payload.model_dump(mode='json', exclude_unset=True)
    if 'slug' in data:
        existing = db.execute(
            select(Project).where(
                Project.slug == data['slug'],
                Project.id != project_id
            )
        ).scalar_one_or_none()
        if existing:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail='Project slug already exists'
            )

    for key, value in data.items():
        setattr(project, key, value)

    db.commit()
    db.refresh(project)
    return project


@router.delete('/projects/{project_id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_project(
    project_id: str,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_admin)
) -> None:
    project = db.get(Project, project_id)
    if not project:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Project not found'
        )

    db.delete(project)
    db.commit()
    return None


@router.post(
    '/projects/{project_id}/media',
    response_model=ProjectMediaOut,
    status_code=status.HTTP_201_CREATED
)
def create_project_media(
    project_id: str,
    payload: ProjectMediaCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_admin)
) -> ProjectMediaOut:
    project = db.get(Project, project_id)
    if not project:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Project not found'
        )

    media = ProjectMedia(project_id=project_id, **payload.model_dump(mode='json'))
    db.add(media)
    db.commit()
    db.refresh(media)
    return media


@router.put('/projects/{project_id}/media/{media_id}', response_model=ProjectMediaOut)
def update_project_media(
    project_id: str,
    media_id: str,
    payload: ProjectMediaUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_admin)
) -> ProjectMediaOut:
    media = db.get(ProjectMedia, media_id)
    if not media or media.project_id != project_id:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Media not found'
        )

    data = payload.model_dump(mode='json', exclude_unset=True)
    for key, value in data.items():
        setattr(media, key, value)

    db.commit()
    db.refresh(media)
    return media


@router.delete('/projects/{project_id}/media/{media_id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_project_media(
    project_id: str,
    media_id: str,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_admin)
) -> None:
    media = db.get(ProjectMedia, media_id)
    if not media or media.project_id != project_id:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Media not found'
        )

    db.delete(media)
    db.commit()
    return None
