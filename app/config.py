from functools import lru_cache

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    mongodb_url: str = Field(
        default="mongodb://localhost:27017",
        title="MongoDB URL",
        description="The URL of the MongoDB database.",
    )
    db_name: str = Field(
        default="test_db",
        title="Database Name",
        description="The name of the database.",
    )
    origins: str = Field(
        default="*",
        title="Origins",
        description="The origins of the API.",
    )
    host: str = Field(
        default="localhost",
        title="Host",
        description="The hostname to bind the server to.",
    )
    port: int = Field(
        default=8000,
        gt=0,
        lt=65536,
        title="Port",
        description="The port on which to run the server.",
    )
    reload: bool = Field(
        default=False,
        title="Reload",
        description="Enable or disable automatic reloading of the server.",
    )

    # Load settings from a .env file.
    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()


def set_settings(new_settings: Settings) -> None:
    global settings
    settings = new_settings


@lru_cache()
def get_settings() -> Settings:
    return settings
