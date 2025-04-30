import logging

from pydantic import BaseModel, ValidationError

from core.config import MOVIE_STORAGE_FILEPATH
from schemas.movie import (
    Movie,
    MovieCreate,
    MovieUpdate,
    MoviePartialUpdate,
    MovieRead,
)

log = logging.getLogger(__name__)


class FilmsStorage(BaseModel):
    slug_to_film: dict[str, Movie] = {}

    def init_storage_from_state(self) -> None:
        try:
            data = FilmsStorage()
            log.warning("Recovered data from storage file")
        except ValidationError:
            self.save_state()
            log.warning("Rewritten storage file due validation error")
            return

    def save_state(self) -> None:
        MOVIE_STORAGE_FILEPATH.write_text(self.model_dump_json(indent=2))
        log.info("Saved movie to storage file.")

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
        log.info("Create new movie.")
        return film

    def delete_by_slag(self, slug) -> None:
        self.slug_to_film.pop(slug, None)

    def delete(self, movie: Movie) -> None:
        self.delete_by_slag(slug=movie.slug)

    def update(
        self,
        movie: Movie,
        movie_in: MovieUpdate,
    ) -> Movie:
        for field_name, value in movie_in:
            setattr(movie, field_name, value)

        return movie

    def update_partial(
        self,
        movie: Movie,
        movie_in: MoviePartialUpdate,
    ):
        for field_name, value in movie_in.model_dump(exclude_unset=True).items():
            setattr(movie, field_name, value)


storage = FilmsStorage()
