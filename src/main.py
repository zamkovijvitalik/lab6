from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database import SessionLocal, engine, Base
import crud, schemas
from typing import List
from models import Role, Permission, User, Post
from schemas import RoleCreate, PermissionCreate, UserCreate, PostCreate


app = FastAPI()
Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.on_event("startup")
def seed_data():
    db = SessionLocal()

    # Додати ролі
    if db.query(Role).count() == 0:
        crud.add_role(db, schemas.RoleCreate(name="admin"))
        crud.add_role(db, schemas.RoleCreate(name="user"))

    # Додати дозволи
    if db.query(Permission).count() == 0:
        crud.add_permission(db, schemas.PermissionCreate(name="read"))
        crud.add_permission(db, schemas.PermissionCreate(name="write"))

    # Додати користувачів
    if db.query(User).count() == 0:
        admin_role = db.query(Role).filter_by(name="admin").first()
        user_role = db.query(Role).filter_by(name="user").first()
        crud.add_user(db, schemas.UserCreate(username="admin", password="adminpass", role_id=admin_role.id))
        crud.add_user(db, schemas.UserCreate(username="john", password="johnpass", role_id=user_role.id))

    # Додати пости
    if db.query(Post).count() == 0:
        admin = db.query(User).filter_by(username="admin").first()
        john = db.query(User).filter_by(username="john").first()
        crud.add_post(db, schemas.PostCreate(title="Welcome", content="Welcome to the blog!", user_id=admin.id))
        crud.add_post(db, schemas.PostCreate(title="Post by John", content="Hello from John!", user_id=john.id))

    db.close()

@app.post("/roles/")
def create_role(data: schemas.RoleCreate, db: Session = Depends(get_db)):
    return crud.add_role(db, data)

@app.post("/permissions/")
def create_permission(data: schemas.PermissionCreate, db: Session = Depends(get_db)):
    return crud.add_permission(db, data)

@app.post("/users/")
def create_user(data: schemas.UserCreate, db: Session = Depends(get_db)):
    return crud.add_user(db, data)

@app.post("/posts/")
def create_post(data: schemas.PostCreate, db: Session = Depends(get_db)):
    return crud.add_post(db, data)

@app.get("/roles/", response_model=List[RoleCreate])
def get_roles(db: Session = Depends(get_db)):
    return db.query(Role).all()

@app.get("/permissions/", response_model=List[PermissionCreate])
def get_permissions(db: Session = Depends(get_db)):
    return db.query(Permission).all()

@app.get("/users/", response_model=List[UserCreate])
def get_users(db: Session = Depends(get_db)):
    return db.query(User).all()

@app.get("/posts/", response_model=List[PostCreate])
def get_posts(db: Session = Depends(get_db)):
    return db.query(Post).all()