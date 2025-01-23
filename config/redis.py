from pydantic_settings import BaseSettings


class RedisSettings(BaseSettings):
    HOST: str = "redis-cache"
    PORT: int = 6379
    EXPIRE_SECONDS: int = 60


RedisSettings = RedisSettings()
