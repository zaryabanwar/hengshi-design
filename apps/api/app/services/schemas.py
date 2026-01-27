from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import Annotated

from pydantic import BaseModel, ConfigDict, Field

KebabStr = Annotated[
    str,
    Field(min_length=1, pattern=r'^[a-z0-9]+(?:-[a-z0-9]+)*$')
]
TitleStr = Annotated[str, Field(min_length=2, max_length=120)]
SummaryStr = Annotated[str, Field(min_length=10, max_length=240)]
BodyStr = Annotated[str, Field(min_length=20)]
NonEmptyStr = Annotated[str, Field(min_length=1)]
DeliverablesList = Annotated[list[NonEmptyStr], Field(min_length=1, max_length=20)]
TagsList = Annotated[list[NonEmptyStr], Field(max_length=20)]


class ServiceCategory(str, Enum):
    STRATEGY_ARCHITECTURE = 'strategy_architecture'
    PLATFORM_ENGINEERING = 'platform_engineering'
    AI_SYSTEMS = 'ai_systems'
    SPATIAL_IMMERSIVE = 'spatial_immersive'
    PRODUCT_DESIGN = 'product_design'
    CLOUD_DEVOPS = 'cloud_devops'
    SECURITY_TRUST = 'security_trust'
    DATA_PLATFORMS = 'data_platforms'
    COMMERCE_GROWTH = 'commerce_growth'


class ServiceBase(BaseModel):
    slug: KebabStr
    title: TitleStr
    category: ServiceCategory
    summary: SummaryStr
    body: BodyStr
    deliverables: DeliverablesList
    tags: TagsList | None = None
    is_featured: bool = False
    sort_order: int = Field(default=0, ge=0)


class ServiceCreate(ServiceBase):
    pass


class ServiceUpdate(BaseModel):
    slug: KebabStr | None = None
    title: TitleStr | None = None
    category: ServiceCategory | None = None
    summary: SummaryStr | None = None
    body: BodyStr | None = None
    deliverables: DeliverablesList | None = None
    tags: TagsList | None = None
    is_featured: bool | None = None
    sort_order: int | None = Field(default=None, ge=0)


class ServiceOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: str
    slug: str
    title: str
    category: ServiceCategory
    summary: str
    body: str
    deliverables: list[str]
    tags: list[str] | None
    is_featured: bool
    sort_order: int
    created_at: datetime
    updated_at: datetime
