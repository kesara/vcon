from pydantic import BaseModel
from typing import List, Optional, Union
from datetime import datetime
from enum import Enum


class BaseObject(BaseModel):
    uuid: str
    type: Optional[str] = None


class EncodingType(str, Enum):
    base64url = "base64url"
    json = "json"
    none = "none"


class InlineFile(BaseModel):
    body: str
    encoding: EncodingType


class ExternallyReferencedFile(BaseModel):
    url: str
    alg: str
    signature: str


Object = Union[BaseObject, InlineFile, ExternallyReferencedFile]


class vCon(BaseModel):
    vcon: str
    uuid: str
    created_at: datetime
    updated_at: datetime
    subject: Optional[str] = None
    redacted: Optional[Object] = None
    appended: Optional[Object] = None
    group: List[Object]
