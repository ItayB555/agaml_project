import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from config import ServerSettings, CORSSettings
from exceptions import DatabaseConnectionError
from exceptions.handlers import database_connection_error_handler
from routes import auth_router, employees_router, employers_router

app = FastAPI()

# Middlewares
app.add_middleware(
    CORSMiddleware,
    allow_origins=CORSSettings.ALLOW_ORIGINS,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*']
)

# Exception handling
app.add_exception_handler(DatabaseConnectionError, handler=database_connection_error_handler)

# Routers
app.include_router(router=auth_router, prefix="/auth")
app.include_router(router=employees_router, prefix="/employees")
app.include_router(router=employers_router, prefix="/employers")


@app.get("/health")
async def healthcheck():
    return {"health": True}


if __name__ == '__main__':
    uvicorn.run(
        app=ServerSettings.APP,
        host=ServerSettings.HOST,
        port=ServerSettings.PORT
    )
