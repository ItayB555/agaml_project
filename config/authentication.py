from pydantic_settings import BaseSettings


class AuthenticationSettings(BaseSettings):
    JWT_SECRET_KEY: str = "default_secret"
    JWT_ALGORITHM: str = "HS256"
    JWT_EXPIRE_MINUTES: int = 30


AuthenticationSettings = AuthenticationSettings()
