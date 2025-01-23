from pydantic_settings import BaseSettings


class ServerSettings(BaseSettings):
    APP: str = "app:app"
    HOST: str = "0.0.0.0"
    PORT: int = 8050


ServerSettings = ServerSettings()
