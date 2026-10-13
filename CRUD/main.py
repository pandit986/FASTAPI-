
from typing import Annotated

from fastapi import FastAPI, Depends, HTTPException, Query, status
from sqlalchemy.orm import Session

import crud
import models
import schemas
from database import engine, get_db

# Create tables if they do not already exist
models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="FastAPI MySQL CRUD",
    description="User Management API with SQLAlchemy and Pydantic",
    version="1.0.0",
)

# Reusable database dependency
DBSession = Annotated[Session, Depends(get_db)]


@app.get("/")
def home():
    return {"message": "FastAPI MySQL CRUD API is running"}


# CREATE USER
@app.post(
    "/users/",
    response_model=schemas.UserResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_user(user: schemas.UserCreate, db: DBSession):
    try:
        return crud.create_user(db, user)
    except ValueError as exc:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=str(exc),
        ) from exc


# GET ALL USERS
@app.get("/users/", response_model=list[schemas.UserResponse])
def get_users(
    db: DBSession,
    skip: int = Query(default=0, ge=0),
    limit: int = Query(default=100, ge=1, le=100),
):
    return crud.get_users(db, skip=skip, limit=limit)


# GET ONE USER
@app.get("/users/{user_id}", response_model=schemas.UserResponse)
def get_user(user_id: int, db: DBSession):
    user = crud.get_user(db, user_id)

    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found",
        )

    return user


# UPDATE USER
@app.put("/users/{user_id}", response_model=schemas.UserResponse)
def update_user(
    user_id: int,
    user_data: schemas.UserUpdate,
    db: DBSession,
):
    try:
        user = crud.update_user(db, user_id, user_data)
    except ValueError as exc:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=str(exc),
        ) from exc

    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found",
        )

    return user


# DELETE USER
@app.delete("/users/{user_id}")
def delete_user(user_id: int, db: DBSession):
    user = crud.delete_user(db, user_id)

    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found",
        )

    return {
        "message": "User deleted successfully",
        "user": schemas.UserResponse.model_validate(user),
    }
