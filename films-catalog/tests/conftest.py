import random
import string
from os import getenv
from typing import Generator

import pytest

from api.api_v1.films.crud import storage
from schemas.movie import Movie


@pytest.fixture(scope="session", autouse=True)
def check_testing_env() -> None:
    if getenv("TESTING") != "1":
        pytest.exit("Environment is not ready for tests")


def build_movie_create(
    slug: str,
    description: str,
    name: str = "Some name",
) -> Movie:
    return Movie(
        slug=slug,
        description=description,
        name=name,
    )


def build_movie_random_slug(description: str, name: str) -> Movie:
    return build_movie_create(
        slug="".join(
            random.choices(
                string.ascii_letters,
                k=8,
            ),
        ),
        description=description,
        name=name,
    )


def create_movie(
    slug: str,
    description: str = "A movie",
) -> Movie:
    movie = build_movie_create(
        slug,
        description=description,
    )
    return storage.create(movie)


def create_movie_random_slug(
    description: str,
    name: str = "some name",
) -> Movie:
    movie = build_movie_random_slug(description, name)
    return storage.create(movie)


@pytest.fixture()
def movie() -> Generator[Movie]:
    movie = build_movie_random_slug()
    yield movie
    storage.delete(movie)
