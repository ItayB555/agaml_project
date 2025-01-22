import uvicorn
from fastapi import FastAPI

from config import ServerSettings

app = FastAPI()


@app.get("/health")
async def healthcheck():
    return {"health": True}


if __name__ == '__main__':
    uvicorn.run(
        app=ServerSettings.APP,
        host=ServerSettings.HOST,
        port=ServerSettings.PORT
    )
