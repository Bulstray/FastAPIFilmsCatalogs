import random
import string
from os import getenv

import pytest

from schemas.movie import Movie, MovieCreate
from storage.movies.crud import storage


@pytest.fixture(scope="session", autouse=True)
def check_testing_env() -> None:
    if getenv("TESTING") != "1":
        pytest.exit("Environment is not ready for tests")


def build_movie_create(
    slug: str,
    description: str,
    name: str = "Some name",
    url: str = "https://www.google.com",
) -> MovieCreate:
    return MovieCreate(
        slug=slug,
        description=description,
        name=name,
        url=url,
    )


def build_movie_random_slug(description: str, name: str) -> MovieCreate:
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
    url: str = "https://www.google.com",
) -> Movie:
    movie = build_movie_create(
        slug,
        description=description,
        url=url,
    )
    return storage.create(movie)


def create_movie_random_slug(
    description: str,
    name: str = "some name",
) -> Movie:
    movie = build_movie_random_slug(description, name)
    return storage.create(movie)
