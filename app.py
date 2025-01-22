import uvicorn
from fastapi import FastAPI

from config import ServerSettings
from exceptions import DatabaseConnectionError
from exceptions.handlers import database_connection_error_handler
from routes import auth_router, employees_router

app = FastAPI()


@app.get("/health")
async def healthcheck():
    return {"health": True}


# Exception handling
app.add_exception_handler(DatabaseConnectionError, handler=database_connection_error_handler)

# Routers
app.include_router(router=auth_router, prefix="/auth")
app.include_router(router=employees_router, prefix="/employees")

if __name__ == '__main__':
    uvicorn.run(
        app=ServerSettings.APP,
        host=ServerSettings.HOST,
        port=ServerSettings.PORT
    )
