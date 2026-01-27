from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy import or_, select
from sqlalchemy.dialects import postgresql
from sqlalchemy.orm import Session, selectinload

from app.db.session import get_db
from app.models.project import Project
from app.projects.schemas import ProjectOut

router = APIRouter()


def _apply_tag_filter(projects: list[Project], tag: str) -> list[Project]:
    return [project for project in projects if project.tags and tag in project.tags]


@router.get('/projects', response_model=list[ProjectOut])
def list_projects(
    tag: str | None = None,
    featured: bool | None = None,
    q: str | None = None,
    limit: int = Query(default=50, ge=0),
    offset: int = Query(default=0, ge=0),
    db: Session = Depends(get_db)
) -> list[ProjectOut]:
    stmt = select(Project).options(selectinload(Project.media))
    apply_tag_in_python = False
    trimmed_tag = tag.strip() if tag else None

    if featured is not None:
        stmt = stmt.where(Project.is_featured == featured)

    if q and q.strip():
        pattern = f"%{q.strip()}%"
        stmt = stmt.where(
            or_(
                Project.title.ilike(pattern),
                Project.summary.ilike(pattern),
                Project.body.ilike(pattern)
            )
        )

    if trimmed_tag:
        if db.bind and db.bind.dialect.name == 'postgresql':
            stmt = stmt.where(
                Project.tags.cast(postgresql.JSONB).contains([trimmed_tag])
            )
        else:
            apply_tag_in_python = True

    stmt = stmt.order_by(Project.sort_order.asc(), Project.title.asc())

    if apply_tag_in_python:
        projects = db.execute(stmt).scalars().all()
        projects = _apply_tag_filter(projects, trimmed_tag)
        return projects[offset:offset + limit] if limit else projects[offset:]

    projects = (
        db.execute(stmt.limit(limit).offset(offset)).scalars().all()
        if limit
        else db.execute(stmt.offset(offset)).scalars().all()
    )
    return projects


@router.get('/projects/{slug}', response_model=ProjectOut)
def get_project(slug: str, db: Session = Depends(get_db)) -> ProjectOut:
    project = db.execute(
        select(Project)
        .options(selectinload(Project.media))
        .where(Project.slug == slug)
    ).scalar_one_or_none()

    if not project:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Project not found')

    return project
