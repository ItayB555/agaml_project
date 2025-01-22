from pydantic import BaseModel, Field
from uuid import uuid4


class User(BaseModel):
    user_id: int = Field(default=uuid4().hex)
    username: str
    hashed_password: str


class UserLogin(BaseModel):
    username: str
    password: str
