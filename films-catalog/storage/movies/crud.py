import logging
from typing import cast

from pydantic import BaseModel
from redis import Redis

from core import config
from core.config import settings
from schemas.movie import (
    Movie,
    MovieCreate,
    MoviePartialUpdate,
    MovieUpdate,
)
from storage.movies.exceptions import MovieAlreadyExists

log = logging.getLogger(__name__)

redis = Redis(
    host=settings.redis.connection.host,
    port=settings.redis.connection.port,
    db=settings.redis.db.movies,
    decode_responses=True,
)


class FilmsStorage(BaseModel):

    def save_movie(self, movie: Movie) -> None:
        redis.hset(
            name=settings.redis.collections_name.movie_hash,
            key=movie.slug,
            value=movie.model_dump_json(),
        )

    def get(self) -> list[Movie]:
        return [
            Movie.model_validate_json(json_data=json_data)
            for json_data in redis.hvals(
                name=settings.redis.collections_name.movie_hash,
            )
        ]

    def get_by_slug(self, slug: str) -> Movie | None:
        if answer := redis.hget(
            name=config.settings.redis.collections_name.movie_hash,
            key=slug,
        ):
            return Movie.model_validate_json(answer)
        return None

    def exists(self, slug: str) -> bool:
        return cast(
            bool,
            redis.hexists(
                name=settings.redis.collections_name.movie_hash,
                key=slug,
            ),
        )

    def create_or_raise_if_exists(self, movie_in: MovieCreate) -> Movie | None:
        if not self.exists(movie_in.slug):
            return self.create(movie_in)

        raise MovieAlreadyExists(movie_in.slug)

    def create(self, film: MovieCreate) -> Movie:
        movie = Movie(**film.model_dump())
        self.save_movie(movie=movie)
        log.info("Create new movie.")
        return movie

    def delete_by_slag(self, slug: str) -> None:
        redis.hdel(settings.redis.collections_name.movie_hash, slug)

    def delete(self, movie: Movie) -> None:
        self.delete_by_slag(slug=movie.slug)

    def update(
        self,
        movie: Movie,
        movie_in: MovieUpdate | MoviePartialUpdate,
    ) -> Movie:

        for field_name, value in movie_in:
            setattr(movie, field_name, value)

        self.save_movie(movie=movie)
        return movie

    def update_partial(
        self,
        movie: Movie,
        movie_in: MoviePartialUpdate,
    ) -> Movie:
        for field_name, value in movie_in.model_dump(exclude_unset=True).items():
            setattr(movie, field_name, value)

        self.save_movie(movie=movie)
        return movie


storage = FilmsStorage()
