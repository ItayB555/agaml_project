from pydantic_settings import BaseSettings


class ServerSettings(BaseSettings):
    APP: str = "app:app"
    HOST: str = "localhost"
    PORT: int = 8050


ServerSettings = ServerSettings()
