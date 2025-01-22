from pydantic import BaseModel


class User(BaseModel):
    username: str
    password: str


class UserInDB(BaseModel):
    user_id: str
    username: str
    hashed_password: str
