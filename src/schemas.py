from pydantic import BaseModel
from typing import Optional

class RoleCreate(BaseModel):
    name: str

class RoleRead(RoleCreate):
    id: int
    created_at: Optional[str]

    class Config:
        orm_mode = True

class PermissionCreate(BaseModel):
    name: str

class UserCreate(BaseModel):
    username: str
    password: str
    role_id: Optional[int]

class UserRead(UserCreate):
    id: int
    created_at: Optional[str]
    updated_at: Optional[str]

    class Config:
        orm_mode = True

class PostCreate(BaseModel):
    title: str
    content: str
    user_id: int
