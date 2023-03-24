from typing import Literal
from pydantic import BaseModel
from enum import Enum


class RoleType(str, Enum):
    admin = "admin"
    viewer = "viewer"


class UserRequest(BaseModel):
    username: str
    password_text: str
    role: RoleType
