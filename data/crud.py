from sqlalchemy.orm import Session
from . import models, schemas, config, database
import hashlib


def get_user(user_id: int, db: Session = database.db):
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_username(username: str, db: Session = database.db) -> models.User:
    return db.query(models.User).filter(models.User.username == username).first()


def get_users(db: Session = database.db) -> list[models.User]:
    return db.query(models.User).all()


def create_user(user: schemas.User, db: Session = database.db) -> models.User:
    fake_hashed_password = hashlib.sha224(user.password + config.SALT).hexdigest()
    db_user = models.User(email=user.username, hashed_password=fake_hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
