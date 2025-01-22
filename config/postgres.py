from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class PostgresSettings(BaseSettings):
    HOST: str = "localhost"
    PORT: int = 5432

    POSTGRES_USERNAME: str = "postgres"
    POSTGRES_PASSWORD: str = "postgres_password"
    POSTGRES_DATABASE: str = "agaml_db"

    model_config = SettingsConfigDict(case_sensitive=False, env_file='.env')


PostgresSettings = PostgresSettings()
