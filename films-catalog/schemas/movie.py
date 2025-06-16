from typing import Annotated

from annotated_types import Len
from pydantic import BaseModel


class MovieBase(BaseModel):
    slug: Annotated[
        str,
        Len(min_length=3, max_length=10),
    ]
    name: str
    description: str


class MovieRead(MovieBase):
    """
    Модель для чтения фильмов
    """


class Movie(MovieBase):
    """
    Модель для хранения данных о фильме
    """

    notes: str = ""


class MovieCreate(MovieBase):
    """
    Модель для добавления в базу данных фильм
    """

    notes: str = ""


class MovieUpdate(MovieBase):
    """
    Модель для обноваление фильма
    """


class MoviePartialUpdate(MovieBase):
    """
    Модель для частичного обновления фильма
    """

    name: str | None = None
    description: str | None = None
    slug: str | None = None
