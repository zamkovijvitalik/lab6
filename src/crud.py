from sqlalchemy.orm import Session
from models import Role, Permission, RolePermission, User, Post
from schemas import *

def add_role(db: Session, data: RoleCreate):
    role = Role(name=data.name)
    db.add(role)
    db.commit()
    db.refresh(role)
    return role

def add_permission(db: Session, data: PermissionCreate):
    perm = Permission(name=data.name)
    db.add(perm)
    db.commit()
    db.refresh(perm)
    return perm

def add_user(db: Session, data: UserCreate):
    user = User(**data.dict())
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def add_post(db: Session, data: PostCreate):
    post = Post(**data.dict())
    db.add(post)
    db.commit()
    db.refresh(post)
    return post
