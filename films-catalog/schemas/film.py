from pydantic import BaseModel


class FilmBase(BaseModel):
    slug: str


class FilmCreate(BaseModel):
    name: str
    description: str


class Film(FilmBase):
    name: str
    description: str
