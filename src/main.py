from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from database import SessionLocal, engine, Base
import crud, schemas
from models import Role, Permission, User, Post

app = FastAPI()
Base.metadata.create_all(bind=engine)

@app.on_event("startup")
def startup_event():
    db = SessionLocal()
    seed_data(db)
    db.close()
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def seed_data(db: Session):
    if db.query(Role).count() == 0:
        admin = Role(name="admin")
        user = Role(name="user")
        db.add_all([admin, user])
        db.commit()

    if db.query(Permission).count() == 0:
        perm1 = Permission(name="create_post")
        perm2 = Permission(name="delete_post")
        db.add_all([perm1, perm2])
        db.commit()

    if db.query(User).count() == 0:
        test_user = User(username="testuser", password="123456", role_id=1)
        db.add(test_user)
        db.commit()

    if db.query(Post).count() == 0:
        post = Post(title="Hello World", content="This is a seeded post.", user_id=1)
        db.add(post)
        db.commit()


@app.post("/roles/", response_model=schemas.RoleRead)
def create_role(data: schemas.RoleCreate, db: Session = Depends(get_db)):
    return crud.add_role(db, data)

@app.get("/roles/", response_model=List[schemas.RoleRead])
def read_roles(db: Session = Depends(get_db)):
    return crud.get_roles(db)

@app.get("/roles/{role_id}", response_model=schemas.RoleRead)
def read_role(role_id: int, db: Session = Depends(get_db)):
    role = crud.get_role(db, role_id)
    if not role:
        raise HTTPException(status_code=404, detail="Role not found")
    return role

@app.put("/roles/{role_id}", response_model=schemas.RoleRead)
def update_role(role_id: int, data: schemas.RoleCreate, db: Session = Depends(get_db)):
    return crud.update_role(db, role_id, data)

@app.delete("/roles/{role_id}")
def delete_role(role_id: int, db: Session = Depends(get_db)):
    return crud.delete_role(db, role_id)


@app.post("/permissions/", response_model=schemas.PermissionRead)
def create_permission(data: schemas.PermissionCreate, db: Session = Depends(get_db)):
    return crud.add_permission(db, data)

@app.get("/permissions/", response_model=List[schemas.PermissionRead])
def read_permissions(db: Session = Depends(get_db)):
    return crud.get_permissions(db)

@app.get("/permissions/{permission_id}", response_model=schemas.PermissionRead)
def read_permission(permission_id: int, db: Session = Depends(get_db)):
    permission = crud.get_permission(db, permission_id)
    if not permission:
        raise HTTPException(status_code=404, detail="Permission not found")
    return permission

@app.put("/permissions/{permission_id}", response_model=schemas.PermissionRead)
def update_permission(permission_id: int, data: schemas.PermissionCreate, db: Session = Depends(get_db)):
    return crud.update_permission(db, permission_id, data)

@app.delete("/permissions/{permission_id}")
def delete_permission(permission_id: int, db: Session = Depends(get_db)):
    return crud.delete_permission(db, permission_id)


@app.post("/users/", response_model=schemas.UserRead)
def create_user(data: schemas.UserCreate, db: Session = Depends(get_db)):
    return crud.add_user(db, data)

@app.get("/users/", response_model=List[schemas.UserRead])
def read_users(db: Session = Depends(get_db)):
    return crud.get_users(db)

@app.get("/users/{user_id}", response_model=schemas.UserRead)
def read_user(user_id: int, db: Session = Depends(get_db)):
    user = crud.get_user(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@app.put("/users/{user_id}", response_model=schemas.UserRead)
def update_user(user_id: int, data: schemas.UserCreate, db: Session = Depends(get_db)):
    return crud.update_user(db, user_id, data)

@app.delete("/users/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    return crud.delete_user(db, user_id)


@app.post("/posts/", response_model=schemas.PostRead)
def create_post(data: schemas.PostCreate, db: Session = Depends(get_db)):
    return crud.add_post(db, data)

@app.get("/posts/", response_model=List[schemas.PostRead])
def read_posts(db: Session = Depends(get_db)):
    return crud.get_posts(db)

@app.get("/posts/{post_id}", response_model=schemas.PostRead)
def read_post(post_id: int, db: Session = Depends(get_db)):
    post = crud.get_post(db, post_id)
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    return post

@app.put("/posts/{post_id}", response_model=schemas.PostRead)
def update_post(post_id: int, data: schemas.PostCreate, db: Session = Depends(get_db)):
    return crud.update_post(db, post_id, data)

@app.delete("/posts/{post_id}")
def delete_post(post_id: int, db: Session = Depends(get_db)):
    return crud.delete_post(db, post_id)


