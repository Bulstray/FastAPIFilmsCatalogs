from typing import Annotated

from annotated_types import Len
from pydantic import AnyHttpUrl, BaseModel

DESCRIPTION_MAX_LENGTH = 200


class MovieBase(BaseModel):
    slug: Annotated[
        str,
        Len(min_length=3, max_length=10),
    ]
    name: str
    description: Annotated[
        str,
        Len(max_length=200),
    ]
    url: AnyHttpUrl


class MovieRead(MovieBase):
    """
    Модель для чтения фильмов
    """


class Movie(MovieBase):
    """
    Модель для хранения данных о фильме
    """


class MovieCreate(MovieBase):
    """
    Модель для добавления в базу данных фильм
    """


class MovieUpdate(MovieBase):
    """
    Модель для обноваление фильма
    """


class MoviePartialUpdate(BaseModel):
    """
    Модель для частичного обновления фильма
    """

    name: str | None = None
    description: Annotated[
        str | None,
        Len(max_length=200),
    ] = None
    url: AnyHttpUrl | None = None
