from pydantic import BaseModel


class FilmBase(BaseModel):
    slug: str


class Film(FilmBase):
    name: str
    description: str


class FilmCreate(FilmBase):
    name: str
    description: str


class FilmUpdate(FilmBase):
    slug: str
    name: str
    description: str


class FilmPartialUpdate(FilmBase):
    slug: str
    name: str
    description: str
