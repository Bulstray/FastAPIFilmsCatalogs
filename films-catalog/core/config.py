import logging
from os import getenv
from pathlib import Path
from typing import Literal, Self

from pydantic import BaseModel, model_validator
from pydantic_settings import (
    BaseSettings,
    PydanticBaseSettingsSource,
    SettingsConfigDict,
    YamlConfigSettingsSource,
)

BASE_DIR = Path(__file__).resolve().parent.parent

LOG_FORMAT: str = (
    "[%(asctime)s.%(msecs)03d] %(module)10s:%(lineno)-3d %(levelname)-7s - %(message)s"
)


class LoggingConfig(BaseModel):
    log_level_name: Literal[
        "DEBUG",
        "INFO",
        "WARNING",
        "ERROR",
        "CRITICAL",
    ] = "INFO"
    log_format: str = LOG_FORMAT
    date_format: str = "%Y-%m-%d %H:%M:%S"

    @property
    def log_level(self) -> int:
        return logging.getLevelNamesMapping()[self.log_level_name]


class RedisConnectionConfig(BaseModel):
    host: str = getenv("REDIS_HOST", "localhost")
    port: int = 6379 if getenv("TESTING") else 6380


class RedisDatabaseConfig(BaseModel):
    default: int = 0
    tokens: int = 1
    users: int = 2
    movies: int = 3

    @model_validator(mode="after")
    def validate_dbs_numbers_unique(self) -> Self:
        db_values = list(self.model_dump().values())

        if len(set(db_values)) != len(db_values):
            raise ValueError("Database numbers should be unique")
        return self


class RedisCollectionConfig(BaseModel):
    tokens_set: str = "tokens"
    movie_hash: str = "movie"


class RedisConfig(BaseModel):
    connection: RedisConnectionConfig = RedisConnectionConfig()
    db: RedisDatabaseConfig = RedisDatabaseConfig()
    collections_name: RedisCollectionConfig = RedisCollectionConfig()


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        case_sensitive=False,
        env_file=(BASE_DIR / ".env.template",),
        env_prefix="FILMS_CATALOG__",
        env_nested_delimiter="__",
        yaml_file=(
            BASE_DIR / "config.default.yaml",
            BASE_DIR / "config.local.yaml",
        ),
        yaml_config_section="movies",
    )

    @classmethod
    def settings_customise_sources(
        cls,
        settings_cls: type[BaseSettings],
        init_settings: PydanticBaseSettingsSource,
        env_settings: PydanticBaseSettingsSource,
        dotenv_settings: PydanticBaseSettingsSource,
        file_secret_settings: PydanticBaseSettingsSource,
    ) -> tuple[PydanticBaseSettingsSource, ...]:
        return (
            init_settings,
            env_settings,
            dotenv_settings,
            file_secret_settings,
            YamlConfigSettingsSource(settings_cls),
        )

    logging: LoggingConfig = LoggingConfig()
    redis: RedisConfig = RedisConfig()


# noinspection PyArgumentList
settings = Settings()

print(settings.logging.log_level_name)
