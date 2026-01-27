from __future__ import annotations

from datetime import datetime
from typing import Annotated, Any

from pydantic import BaseModel, ConfigDict, EmailStr, Field

NameStr = Annotated[str, Field(min_length=2, max_length=120)]
EmailField = Annotated[EmailStr, Field(max_length=320)]
CompanyStr = Annotated[str, Field(max_length=160)]
PhoneStr = Annotated[str, Field(max_length=40)]
SubjectStr = Annotated[str, Field(max_length=160)]
MessageStr = Annotated[str, Field(min_length=20, max_length=4000)]
SourceUrlStr = Annotated[str, Field(max_length=500)]


class LeadCreate(BaseModel):
    model_config = ConfigDict(str_strip_whitespace=True)

    name: NameStr
    email: EmailField
    company: CompanyStr | None = None
    phone: PhoneStr | None = None
    subject: SubjectStr | None = None
    message: MessageStr
    source_url: SourceUrlStr | None = None
    metadata: dict[str, Any] | None = None


class LeadCreated(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: str
    created_at: datetime


class LeadOut(BaseModel):
    model_config = ConfigDict(from_attributes=True, str_strip_whitespace=True)

    id: str
    name: str
    email: str
    company: str | None
    phone: str | None
    subject: str | None
    message: str
    source_url: str | None
    metadata: dict[str, Any] | None = Field(default=None, validation_alias='metadata_')
    created_at: datetime
