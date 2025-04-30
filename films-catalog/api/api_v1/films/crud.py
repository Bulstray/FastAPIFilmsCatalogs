import json
from typing import Any, Self

from pydantic import BaseModel, ValidationError
from typing_extensions import overload

from core.config import MOVIE_STORAGE_FILEPATH
from schemas.movie import (
    Movie,
    MovieCreate,
    MovieUpdate,
    MoviePartialUpdate,
    MovieRead,
)


class FilmsStorage(BaseModel):
    slug_to_film: dict[str, Movie] = {}

    def save_state(self) -> None:
        MOVIE_STORAGE_FILEPATH.write_text(self.model_dump_json(indent=2))

    @classmethod
    def from_state(cls):
        if not MOVIE_STORAGE_FILEPATH.exists():
            return FilmsStorage()
        return cls.model_validate_json(MOVIE_STORAGE_FILEPATH.read_text())

    def get(self) -> list[MovieRead]:
        return [self.slug_to_film[film] for film in self.slug_to_film]

    def get_by_slug(self, slug):
        return self.slug_to_film.get(slug)

    def create(self, film: MovieCreate) -> Movie:
        film = Movie(**film.model_dump())
        self.slug_to_film[film.slug] = film
        self.save_state()
        return film

    def delete_by_slag(self, slug) -> None:
        self.slug_to_film.pop(slug, None)
        self.save_state()

    def delete(self, movie: Movie) -> None:
        self.delete_by_slag(slug=movie.slug)

    def update(
        self,
        movie: Movie,
        movie_in: MovieUpdate,
    ) -> Movie:
        for field_name, value in movie_in:
            setattr(movie, field_name, value)
        self.save_state()

        return movie

    def update_partial(
        self,
        movie: Movie,
        movie_in: MoviePartialUpdate,
    ):
        for field_name, value in movie_in.model_dump(exclude_unset=True).items():
            setattr(movie, field_name, value)

        self.save_state()


try:
    storage = FilmsStorage.from_state()
except ValidationError:
    storage = FilmsStorage()
    storage.save_state()
