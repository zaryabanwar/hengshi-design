from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import Annotated, Any

from pydantic import AnyUrl, BaseModel, ConfigDict, Field, ValidationError, model_validator

from app.services.schemas import ServiceCategory

KeyStr = Annotated[str, Field(pattern=r'^[a-z0-9_]+$', min_length=1, max_length=64)]
TitleStr = Annotated[str, Field(min_length=2, max_length=120)]
DescriptionStr = Annotated[str, Field(max_length=400)]
Vec3 = Annotated[list[float], Field(min_length=3, max_length=3)]


class PanelKind(str, Enum):
    SERVICE_CATEGORY = 'service_category'
    PROJECT = 'project'
    CONTACT = 'contact'


class HotspotKind(str, Enum):
    OPEN_PANEL = 'OPEN_PANEL'
    NAVIGATE_NODE = 'NAVIGATE_NODE'
    OPEN_URL = 'OPEN_URL'


class OpenPanelPayload(BaseModel):
    panel: PanelKind
    category: ServiceCategory | None = None
    project_slug: str | None = None

    @model_validator(mode='after')
    def validate_payload(self) -> 'OpenPanelPayload':
        if self.panel == PanelKind.SERVICE_CATEGORY and not self.category:
            raise ValueError('category is required for service_category panels')
        return self


class NavigateNodePayload(BaseModel):
    target_node_key: KeyStr


class OpenUrlPayload(BaseModel):
    url: AnyUrl


def _validate_hotspot_payload(kind: HotspotKind, payload: dict[str, Any] | None) -> dict[str, Any]:
    if payload is None:
        raise ValueError('payload is required for hotspot kind')

    try:
        if kind == HotspotKind.OPEN_PANEL:
            return OpenPanelPayload.model_validate(payload).model_dump()
        if kind == HotspotKind.NAVIGATE_NODE:
            return NavigateNodePayload.model_validate(payload).model_dump()
        if kind == HotspotKind.OPEN_URL:
            return OpenUrlPayload.model_validate(payload).model_dump()
    except ValidationError as exc:
        raise ValueError('payload does not match hotspot kind') from exc

    raise ValueError('Unsupported hotspot kind')


class WorldHotspotBase(BaseModel):
    key: KeyStr
    title: TitleStr
    description: DescriptionStr | None = None
    kind: HotspotKind
    position: Vec3
    normal: Vec3 | None = None
    radius: float = Field(default=0.35, ge=0.05, le=5.0)
    icon: str | None = Field(default=None, max_length=64)
    payload: dict[str, Any]
    sort_order: int = Field(default=0, ge=0)
    is_enabled: bool = True

    @model_validator(mode='after')
    def validate_payload(self) -> 'WorldHotspotBase':
        self.payload = _validate_hotspot_payload(self.kind, self.payload)
        return self


class WorldHotspotCreate(WorldHotspotBase):
    node_id: str


class WorldHotspotUpdate(BaseModel):
    key: KeyStr | None = None
    title: TitleStr | None = None
    description: DescriptionStr | None = None
    kind: HotspotKind | None = None
    position: Vec3 | None = None
    normal: Vec3 | None = None
    radius: float | None = Field(default=None, ge=0.05, le=5.0)
    icon: str | None = Field(default=None, max_length=64)
    payload: dict[str, Any] | None = None
    sort_order: int | None = Field(default=None, ge=0)
    is_enabled: bool | None = None

    @model_validator(mode='after')
    def validate_payload(self) -> 'WorldHotspotUpdate':
        if self.payload is not None and self.kind is None:
            raise ValueError('kind is required when payload is provided')
        if self.kind is not None and self.payload is None:
            raise ValueError('payload is required when kind is provided')
        if self.payload is not None and self.kind is not None:
            self.payload = _validate_hotspot_payload(self.kind, self.payload)
        return self


class WorldHotspotOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: str
    node_id: str
    key: str
    title: str
    description: str | None
    kind: HotspotKind
    position: list[float]
    normal: list[float] | None
    radius: float
    icon: str | None
    payload: dict[str, Any] | None
    sort_order: int
    is_enabled: bool
    created_at: datetime


class WorldNodeBase(BaseModel):
    key: KeyStr
    title: TitleStr
    description: DescriptionStr | None = None
    is_entry: bool = False
    sort_order: int = Field(default=0, ge=0)
    camera_position: Vec3
    camera_target: Vec3
    camera_fov: int = Field(default=50, ge=20, le=90)
    environment: dict[str, Any] | None = None


class WorldNodeCreate(WorldNodeBase):
    pass


class WorldNodeUpdate(BaseModel):
    key: KeyStr | None = None
    title: TitleStr | None = None
    description: DescriptionStr | None = None
    is_entry: bool | None = None
    sort_order: int | None = Field(default=None, ge=0)
    camera_position: Vec3 | None = None
    camera_target: Vec3 | None = None
    camera_fov: int | None = Field(default=None, ge=20, le=90)
    environment: dict[str, Any] | None = None


class WorldNodeOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: str
    key: str
    title: str
    description: str | None
    is_entry: bool
    sort_order: int
    camera_position: list[float]
    camera_target: list[float]
    camera_fov: int
    environment: dict[str, Any] | None
    created_at: datetime
    updated_at: datetime
    hotspots: list[WorldHotspotOut]


class WorldResponse(BaseModel):
    nodes: list[WorldNodeOut]
