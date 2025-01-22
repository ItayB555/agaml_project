from typing import Annotated

from fastapi import APIRouter, Depends, Query
from starlette import status
from starlette.responses import JSONResponse

from models import Employee
from postgres import PostgresEmployeesAccessor
from routes import get_current_user

employees_router = APIRouter(tags=["Employees"],
                             dependencies=[Depends(get_current_user)])
postgres_employees_accessor = PostgresEmployeesAccessor()


@employees_router.get("/")
async def get_employees(filter_text: str, page: int):
    return postgres_employees_accessor.search(filter_text, page)


@employees_router.post("/")
async def insert_employee(new_employee: Employee):
    was_insertion_successful = postgres_employees_accessor.insert(new_employee)
    if was_insertion_successful:
        return JSONResponse(status_code=status.HTTP_201_CREATED,
                            content=dict(message="Employee was created successfully",
                                         employee=new_employee.dict()))
    return JSONResponse(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                        content=dict(message="Employee was not created, check the payload",
                                     employee=new_employee.dict()))
