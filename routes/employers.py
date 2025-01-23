import json

from fastapi import APIRouter, Depends
from starlette import status
from starlette.responses import JSONResponse

from config import RedisSettings
from middleware import RedisCache
from models import Employer
from postgres import PostgresEmployersAccessor
from routes import get_current_user

employers_router = APIRouter(tags=["Employers"],
                             dependencies=[Depends(get_current_user)])
postgres_employers_accessor = PostgresEmployersAccessor()
redis_cache = RedisCache()


@employers_router.get("/")
async def get_employers(filter_text: str, page: int = 1):
    cache_key = f"{filter_text}_{page}_employers"
    cache = redis_cache.server.get(cache_key)
    if cache:
        return json.loads(cache)
    employers = postgres_employers_accessor.search(filter_text, page)
    redis_cache.server.setex(cache_key, RedisSettings.EXPIRE_SECONDS, json.dumps(employers))
    return employers


@employers_router.post("/")
async def insert_employer(new_employer: Employer):
    was_insertion_successful = postgres_employers_accessor.insert(new_employer)
    if was_insertion_successful:
        return JSONResponse(status_code=status.HTTP_201_CREATED,
                            content=dict(message="Employer was created successfully",
                                         employee=new_employer.dict()))
    return JSONResponse(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                        content=dict(message="Employer was not created, check the payload",
                                     employee=new_employer.dict()))
