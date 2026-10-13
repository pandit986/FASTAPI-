
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError

from models import User
from schemas import UserCreate, UserUpdate


# CREATE
def create_user(db: Session, user_data: UserCreate):
    user = User(**user_data.model_dump())

    db.add(user)

    try:
        db.commit()
        db.refresh(user)
    except IntegrityError:
        db.rollback()
        raise ValueError("Email already exists")

    return user


# READ ALL
def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(User).offset(skip).limit(limit).all()


# READ ONE
def get_user(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()


# UPDATE
def update_user(
    db: Session,
    user_id: int,
    user_data: UserUpdate,
):
    user = get_user(db, user_id)

    if user is None:
        return None

    for field, value in user_data.model_dump().items():
        setattr(user, field, value)

    try:
        db.commit()
        db.refresh(user)
    except IntegrityError:
        db.rollback()
        raise ValueError("Email already exists")

    return user


# DELETE
def delete_user(db: Session, user_id: int):
    user = get_user(db, user_id)

    if user is None:
        return None

    db.delete(user)
    db.commit()

    return user
