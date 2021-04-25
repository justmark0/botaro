from sqlalchemy.orm import Session
from . import models, schemas, config, database


def get_user(user_id: int, db: Session = database.db) -> models.User:
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_username(username: str, db: Session = database.db) -> models.User:
    return db.query(models.User).filter(models.User.username == username).first()


def get_users(db: Session = database.db) -> list[models.User]:
    return db.query(models.User).all()


def get_bots(db: Session = database.db) -> list[models.Bot]:
    return db.query(models.Bot).all()


def delete_bot(user_id, bot_token, db: Session = database.db):
    bot = db.query(models.Bot).filter(models.Bot.token == bot_token,
                                      models.Bot.user_id == user_id).first()
    if bot is None:
        raise Exception("No such bot")
    db.delete(bot)
    db.commit()


def create_user(user: schemas.User, db: Session = database.db):
    fake_hashed_password = config.pwd_context.hash((user.password + config.SALT))
    if db.query(models.User).filter(models.User.username == user.username).first() is not None:
        raise Exception("Username already exists")
    db_user = models.User(username=user.username, hashed_password=fake_hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)


def create_bot(bot: schemas.Bot, user: models.User, db: Session = database.db):
    if db.query(models.Bot).filter(models.Bot.token == bot.token).first() is not None:
        raise Exception("Bot already stored")
    bot_db = models.Bot(token=bot.token, user_id=user.id)
    db.add(bot_db)
    db.commit()
    db.refresh(bot_db)
