import uuid
from datetime import datetime
from typing import Any

import sqlalchemy as sa
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base import Base


class Lead(Base):
    __tablename__ = 'leads'

    id: Mapped[str] = mapped_column(
        sa.String(36), primary_key=True, default=lambda: str(uuid.uuid4())
    )
    name: Mapped[str] = mapped_column(sa.String(120), nullable=False)
    email: Mapped[str] = mapped_column(sa.String(320), nullable=False)
    company: Mapped[str | None] = mapped_column(sa.String(160), nullable=True)
    phone: Mapped[str | None] = mapped_column(sa.String(40), nullable=True)
    subject: Mapped[str | None] = mapped_column(sa.String(160), nullable=True)
    message: Mapped[str] = mapped_column(sa.Text, nullable=False)
    source_url: Mapped[str | None] = mapped_column(sa.String(500), nullable=True)
    metadata_: Mapped[dict[str, Any] | None] = mapped_column(
        'metadata',
        sa.JSON,
        nullable=True
    )
    created_at: Mapped[datetime] = mapped_column(
        sa.DateTime(timezone=True),
        nullable=False,
        server_default=sa.func.now()
    )
