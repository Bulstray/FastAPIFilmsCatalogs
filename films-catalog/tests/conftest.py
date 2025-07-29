import random
import string
from os import getenv
from typing import Generator

import pytest

from api.api_v1.films.crud import storage
from schemas.movie import Movie

if getenv("TESTING") != "1":
    pytest.exit("Environment is not ready for tests")


def build_movie_create(slug: str) -> Movie:
    return Movie(
        slug=slug,
        description="Some description",
        name="Some name",
    )


def build_movie_random_slug() -> Movie:
    return build_movie_create(
        slug="".join(
            random.choices(
                string.ascii_letters,
                k=8,
            ),
        ),
    )


def create_movie(slug: str) -> Movie:
    movie = build_movie_create(slug)
    return storage.create(movie)


@pytest.fixture()
def movie() -> Generator[Movie]:
    movie = build_movie_random_slug()
    yield movie
    storage.delete(movie)
