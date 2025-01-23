from pydantic_settings import BaseSettings


class CORSSettings(BaseSettings):
    ALLOW_ORIGINS: list[str] = [
        "http://localhost",
    ]


CORSSettings = CORSSettings()
