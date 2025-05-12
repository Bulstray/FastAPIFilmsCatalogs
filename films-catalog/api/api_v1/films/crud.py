import logging

from pydantic import BaseModel, ValidationError
from redis import Redis

from core.config import MOVIE_STORAGE_FILEPATH
from core import config
from schemas.movie import (
    Movie,
    MovieCreate,
    MovieUpdate,
    MoviePartialUpdate,
    MovieRead,
)

log = logging.getLogger(__name__)

redis = Redis(
    host=config.REDIS_HOST,
    port=config.REDIS_PORT,
    db=config.REDIS_DB_MOVIE,
    decode_responses=True,
)


class FilmsStorage(BaseModel):

    def save_movie(self, movie: Movie) -> None:
        redis.hset(
            name=config.REDIS_MOVIE_HASH_NAME,
            key=movie.slug,
            value=movie.model_dump_json(),
        )

    def get(self) -> list[Movie]:
        return [
            Movie.model_validate_json(json_data=json_data)
            for json_data in redis.hvals(name=config.REDIS_MOVIE_HASH_NAME)
        ]

    def get_by_slug(self, slug):
        if answer := redis.hget(
            name=config.REDIS_MOVIE_HASH_NAME,
            key=slug,
        ):
            return Movie.model_validate_json(answer)
        return None

    def create(self, film: MovieCreate) -> Movie:
        film = Movie(**film.model_dump())
        self.save_movie(movie=film)
        log.info("Create new movie.")
        return film

    def delete_by_slag(self, slug: str) -> None:
        redis.hdel(config.REDIS_MOVIE_HASH_NAME, slug)

    def delete(self, movie: Movie) -> None:
        self.delete_by_slag(slug=movie.slug)

    def update(
        self,
        movie: Movie,
        movie_in: MovieUpdate,
    ) -> Movie:

        for field_name, value in movie_in:
            setattr(movie, field_name, value)

        self.save_movie(movie=movie)
        return movie

    def update_partial(
        self,
        movie: Movie,
        movie_in: MoviePartialUpdate,
    ):
        for field_name, value in movie_in.model_dump(exclude_unset=True).items():
            setattr(movie, field_name, value)

        self.save_movie(movie=movie)
        return movie


storage = FilmsStorage()
