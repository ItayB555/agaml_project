from pydantic_settings import BaseSettings


class PostgresSettings(BaseSettings):
    HOST: str = "localhost"
    PORT: int = 5432
    DATABASE_NAME: str = "agaml_project"
    USERNAME = "agaml"
    PASSWORD = "default_secret"


PostgresSettings = PostgresSettings()
