from typing import List, Optional
from pydantic import BaseModel


class UserBasic(BaseModel):
    username: str


class User(UserBasic):
    password: str


class Token(BaseModel):
    access_token: str
