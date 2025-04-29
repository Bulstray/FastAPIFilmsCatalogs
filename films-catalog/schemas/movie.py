from pydantic import BaseModel


class MovieBase(BaseModel):
    slug: str
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


class MovieUpdate(MovieBase):
    """
    Модель для обноваление фильма
    """


class MoviePartialUpdate(MovieBase):
    """Модель для частичного обновления фильма"""
