from pydantic_settings import BaseSettings


class PostgresSettings(BaseSettings):
    HOST: str = "localhost"
    PORT: int = 5432
    DATABASE_NAME: str = "al_project"
    POSTGRES_USERNAME: str = "postgres"
    POSTGRES_PASSWORD: str = "default_password"


PostgresSettings = PostgresSettings()
