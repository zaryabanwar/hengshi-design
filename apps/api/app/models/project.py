import uuid
from datetime import datetime

import sqlalchemy as sa
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base


class Project(Base):
    __tablename__ = 'projects'

    id: Mapped[str] = mapped_column(
        sa.String(36), primary_key=True, default=lambda: str(uuid.uuid4())
    )
    slug: Mapped[str] = mapped_column(
        sa.String(160), unique=True, index=True, nullable=False
    )
    title: Mapped[str] = mapped_column(sa.String(160), nullable=False)
    summary: Mapped[str] = mapped_column(sa.String(300), nullable=False)
    body: Mapped[str] = mapped_column(sa.Text, nullable=False)
    tags: Mapped[list[str] | None] = mapped_column(sa.JSON, nullable=True)
    is_featured: Mapped[bool] = mapped_column(
        sa.Boolean,
        nullable=False,
        default=False,
        server_default=sa.false()
    )
    sort_order: Mapped[int] = mapped_column(
        sa.Integer,
        nullable=False,
        default=0,
        server_default=sa.text('0')
    )
    created_at: Mapped[datetime] = mapped_column(
        sa.DateTime(timezone=True),
        nullable=False,
        server_default=sa.func.now()
    )
    updated_at: Mapped[datetime] = mapped_column(
        sa.DateTime(timezone=True),
        nullable=False,
        server_default=sa.func.now(),
        onupdate=sa.func.now()
    )

    media: Mapped[list['ProjectMedia']] = relationship(
        'ProjectMedia',
        back_populates='project',
        cascade='all, delete-orphan',
        passive_deletes=True,
        order_by='ProjectMedia.sort_order'
    )


class ProjectMedia(Base):
    __tablename__ = 'project_media'

    id: Mapped[str] = mapped_column(
        sa.String(36), primary_key=True, default=lambda: str(uuid.uuid4())
    )
    project_id: Mapped[str] = mapped_column(
        sa.String(36),
        sa.ForeignKey('projects.id', ondelete='CASCADE'),
        nullable=False,
        index=True
    )
    type: Mapped[str] = mapped_column(sa.String(16), nullable=False)
    url: Mapped[str] = mapped_column(sa.String(500), nullable=False)
    caption: Mapped[str | None] = mapped_column(sa.String(240), nullable=True)
    sort_order: Mapped[int] = mapped_column(
        sa.Integer,
        nullable=False,
        default=0,
        server_default=sa.text('0')
    )
    created_at: Mapped[datetime] = mapped_column(
        sa.DateTime(timezone=True),
        nullable=False,
        server_default=sa.func.now()
    )

    project: Mapped[Project] = relationship('Project', back_populates='media')
