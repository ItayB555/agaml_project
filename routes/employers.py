from fastapi import APIRouter, Depends
from starlette import status
from starlette.responses import JSONResponse

from models import Employer
from postgres import PostgresEmployersAccessor
from routes import get_current_user

employers_router = APIRouter(tags=["Employees"],
                             dependencies=[Depends(get_current_user)])
postgres_employers_accessor = PostgresEmployersAccessor()


@employers_router.get("/")
async def get_employees(filter_text: str):
    return postgres_employers_accessor.search(filter_text)


@employers_router.post("/")
async def insert_employee(new_employee: Employer):
    was_insertion_successful = postgres_employers_accessor.insert(new_employee)
    if was_insertion_successful:
        return JSONResponse(status_code=status.HTTP_201_CREATED,
                            content=dict(message="Employee was created successfully",
                                         employee=new_employee.dict()))
    return JSONResponse(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                        content=dict(message="Employee was not created, check the payload",
                                     employee=new_employee.dict()))
