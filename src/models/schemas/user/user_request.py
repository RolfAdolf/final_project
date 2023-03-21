from typing import Literal
from pydantic import BaseModel
from enum import Enum


class RoleType(Enum):
    admin = "admin"
    viewer = "viewer"


class UserRequest(BaseModel):
    username: str
    password_text: str
    role: RoleType
