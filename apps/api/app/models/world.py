import uuid
from datetime import datetime
from typing import Any

import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base

JSONType = sa.JSON().with_variant(JSONB, 'postgresql')


class WorldNode(Base):
    __tablename__ = 'world_nodes'

    id: Mapped[str] = mapped_column(
        sa.String(36), primary_key=True, default=lambda: str(uuid.uuid4())
    )
    key: Mapped[str] = mapped_column(
        sa.String(64), unique=True, index=True, nullable=False
    )
    title: Mapped[str] = mapped_column(sa.String(120), nullable=False)
    description: Mapped[str | None] = mapped_column(sa.String(400), nullable=True)
    is_entry: Mapped[bool] = mapped_column(
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
    camera_position: Mapped[list[float]] = mapped_column(
        JSONType,
        nullable=False
    )
    camera_target: Mapped[list[float]] = mapped_column(
        JSONType,
        nullable=False
    )
    camera_fov: Mapped[int] = mapped_column(
        sa.Integer,
        nullable=False,
        default=50,
        server_default=sa.text('50')
    )
    environment: Mapped[dict[str, Any] | None] = mapped_column(
        JSONType,
        nullable=True
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

    hotspots: Mapped[list['WorldHotspot']] = relationship(
        'WorldHotspot',
        back_populates='node',
        cascade='all, delete-orphan',
        passive_deletes=True,
        order_by='WorldHotspot.sort_order'
    )


class WorldHotspot(Base):
    __tablename__ = 'world_hotspots'
    __table_args__ = (
        sa.UniqueConstraint('node_id', 'key', name='uq_world_hotspots_node_key'),
    )

    id: Mapped[str] = mapped_column(
        sa.String(36), primary_key=True, default=lambda: str(uuid.uuid4())
    )
    node_id: Mapped[str] = mapped_column(
        sa.String(36),
        sa.ForeignKey('world_nodes.id', ondelete='CASCADE'),
        nullable=False,
        index=True
    )
    key: Mapped[str] = mapped_column(sa.String(80), nullable=False)
    title: Mapped[str] = mapped_column(sa.String(120), nullable=False)
    description: Mapped[str | None] = mapped_column(sa.String(400), nullable=True)
    kind: Mapped[str] = mapped_column(sa.String(32), nullable=False)
    position: Mapped[list[float]] = mapped_column(JSONType, nullable=False)
    normal: Mapped[list[float] | None] = mapped_column(JSONType, nullable=True)
    radius: Mapped[float] = mapped_column(
        sa.Float,
        nullable=False,
        default=0.35,
        server_default=sa.text('0.35')
    )
    icon: Mapped[str | None] = mapped_column(sa.String(64), nullable=True)
    payload: Mapped[dict[str, Any] | None] = mapped_column(JSONType, nullable=True)
    sort_order: Mapped[int] = mapped_column(
        sa.Integer,
        nullable=False,
        default=0,
        server_default=sa.text('0')
    )
    is_enabled: Mapped[bool] = mapped_column(
        sa.Boolean,
        nullable=False,
        default=True,
        server_default=sa.true()
    )
    created_at: Mapped[datetime] = mapped_column(
        sa.DateTime(timezone=True),
        nullable=False,
        server_default=sa.func.now()
    )

    node: Mapped[WorldNode] = relationship('WorldNode', back_populates='hotspots')
