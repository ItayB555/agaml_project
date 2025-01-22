from pydantic_settings import BaseSettings


class RedisSettings(BaseSettings):
    HOST: str = "localhost"
    PORT: int = 6379


RedisSettings = RedisSettings()
