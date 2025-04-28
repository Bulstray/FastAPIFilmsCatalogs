from pydantic import BaseModel


class FilmBase(BaseModel):
    movie_id: int


class FilmCreate(BaseModel):
    name: str
    description: str


class Film(FilmBase):
    name: str
    description: str
