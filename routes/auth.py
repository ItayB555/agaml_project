from datetime import datetime, timezone, timedelta
from typing import Annotated

import jwt
from fastapi import APIRouter, Body
from fastapi.security import OAuth2PasswordBearer
from passlib.context import CryptContext
from starlette import status
from starlette.responses import JSONResponse

from config import AuthenticationSettings
from models import User
from postgres import PostgresAuthenticationAccessor

auth_router = APIRouter(tags=["Authentication"])
password_context = CryptContext(schemes=["bcrypt"])
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
postgres_authentication_accessor = PostgresAuthenticationAccessor()


def create_access_token(data: dict) -> str:
    data_to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(minutes=AuthenticationSettings.JWT_EXPIRE_MINUTES)
    data_to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(payload=data_to_encode,
                             key=AuthenticationSettings.JWT_SECRET_KEY,
                             algorithm=AuthenticationSettings.JWT_ALGORITHM)
    return encoded_jwt


@auth_router.post("/register",
                  response_class=JSONResponse)
async def register(new_user: Annotated[User, Body(..., embed=False)]):
    username, password = new_user.username, new_user.password
    fetched_user = postgres_authentication_accessor.get_user(username)
    if fetched_user:
        return JSONResponse(status_code=status.HTTP_409_CONFLICT, content=dict(content="User already exists"))
    hashed_password = password_context.hash(password)
    was_register_successful = postgres_authentication_accessor.insert_new_user(username, hashed_password)
    if was_register_successful:
        return JSONResponse(status_code=status.HTTP_201_CREATED,
                            content=dict(message="User created successfully",
                                         jwt=create_access_token(dict(username=username))))
    else:
        return JSONResponse(status_code=status.HTTP_406_NOT_ACCEPTABLE, content={"message": "User creation failed"})


@auth_router.post("/login",
                  response_class=JSONResponse)
async def login(user: Annotated[User, Body(..., embed=False)]):
    username, password = user.username, user.password
    fetched_user = postgres_authentication_accessor.get_user(username)
    if not fetched_user:
        return JSONResponse(status_code=status.HTTP_401_UNAUTHORIZED,
                            content=dict(message=f"Invalid username or password"))
    is_password_valid = password_context.verify(password, fetched_user.hashed_password)
    if not is_password_valid:
        return JSONResponse(status_code=status.HTTP_401_UNAUTHORIZED,
                            content=dict(message=f"Invalid username or password"))
    return JSONResponse(status_code=status.HTTP_200_OK,
                        content=dict(message="Login successful",
                                     jwt=create_access_token(dict(username=username)))
                        )
