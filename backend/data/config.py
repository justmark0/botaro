from passlib.context import CryptContext
from dotenv import load_dotenv
import os

load_dotenv()

# Security

# to get a string like this run:
# openssl rand -hex 32
SECRET_KEY = os.getenv("SECRET_KEY") or "a63d04c31b4145d4d027481c919cd5d0dfba5ac3839676d7b2f441b9cba3bad4"
SALT = os.getenv("SALT") or SECRET_KEY[:len(SECRET_KEY) // 2:]
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Database
# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/data"
SQLALCHEMY_DATABASE_URL = os.getenv("SQLALCHEMY_DATABASE_URL") or "sqlite:///./db.sqlite3"

bot_processes = []
