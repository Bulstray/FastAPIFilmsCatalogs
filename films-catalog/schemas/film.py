from pydantic import BaseModel


class FilmBase(BaseModel):
    slug: str


class FilmCreate(FilmBase):
    name: str
    description: str


class Film(FilmBase):
    name: str
    description: str
