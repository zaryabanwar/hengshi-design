import uuid
from datetime import datetime

import sqlalchemy as sa
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base import Base


class Service(Base):
    __tablename__ = 'services'

    id: Mapped[str] = mapped_column(
        sa.String(36), primary_key=True, default=lambda: str(uuid.uuid4())
    )
    slug: Mapped[str] = mapped_column(
        sa.String(160), unique=True, index=True, nullable=False
    )
    title: Mapped[str] = mapped_column(sa.String(120), nullable=False)
    category: Mapped[str] = mapped_column(sa.String(64), nullable=False)
    summary: Mapped[str] = mapped_column(sa.String(240), nullable=False)
    body: Mapped[str] = mapped_column(sa.Text, nullable=False)
    deliverables: Mapped[list[str]] = mapped_column(sa.JSON, nullable=False)
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
