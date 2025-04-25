from pydantic import BaseModel


class Film(BaseModel):
    movie_id: int
    name: str
    description: str
