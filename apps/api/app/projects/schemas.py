from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import Annotated

from pydantic import BaseModel, ConfigDict, Field

KebabStr = Annotated[
    str,
    Field(min_length=1, pattern=r'^[a-z0-9]+(?:-[a-z0-9]+)*$')
]
TitleStr = Annotated[str, Field(min_length=2, max_length=160)]
SummaryStr = Annotated[str, Field(min_length=10, max_length=300)]
BodyStr = Annotated[str, Field(min_length=20)]
NonEmptyStr = Annotated[str, Field(min_length=1)]
TagsList = Annotated[list[NonEmptyStr], Field(max_length=20)]


class ProjectMediaType(str, Enum):
    IMAGE = 'image'
    VIDEO = 'video'


class ProjectMediaBase(BaseModel):
    type: ProjectMediaType
    url: NonEmptyStr
    caption: str | None = None
    sort_order: int = Field(default=0, ge=0)


class ProjectMediaCreate(ProjectMediaBase):
    pass


class ProjectMediaUpdate(BaseModel):
    type: ProjectMediaType | None = None
    url: NonEmptyStr | None = None
    caption: str | None = None
    sort_order: int | None = Field(default=None, ge=0)


class ProjectMediaOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: str
    type: ProjectMediaType
    url: str
    caption: str | None
    sort_order: int
    created_at: datetime


class ProjectBase(BaseModel):
    slug: KebabStr
    title: TitleStr
    summary: SummaryStr
    body: BodyStr
    tags: TagsList | None = None
    is_featured: bool = False
    sort_order: int = Field(default=0, ge=0)


class ProjectCreate(ProjectBase):
    pass


class ProjectUpdate(BaseModel):
    slug: KebabStr | None = None
    title: TitleStr | None = None
    summary: SummaryStr | None = None
    body: BodyStr | None = None
    tags: TagsList | None = None
    is_featured: bool | None = None
    sort_order: int | None = Field(default=None, ge=0)


class ProjectOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: str
    slug: str
    title: str
    summary: str
    body: str
    tags: list[str] | None
    is_featured: bool
    sort_order: int
    created_at: datetime
    updated_at: datetime
    media: list[ProjectMediaOut]
