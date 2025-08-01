import random
import string
from collections.abc import Generator
from typing import ClassVar
from unittest import TestCase

import pytest

from api.api_v1.films.crud import MovieAlreadyExists, storage
from schemas.movie import Movie, MovieCreate, MoviePartialUpdate, MovieUpdate


def create_movie() -> Movie:
    movie_in = MovieCreate(
        slug="".join(
            random.choices(
                string.ascii_letters,
                k=8,
            ),
        ),
        name="film",
        description="some description",
    )

    return storage.create(movie_in)


class MovieCatalogStorageUpdateTestCase(TestCase):

    def setUp(self) -> None:
        self.movie = create_movie()

    def tearDown(self) -> None:
        storage.delete(self.movie)

    def test_update(self) -> None:
        movie_update = MovieUpdate(
            **self.movie.model_dump(),
        )

        source_description = self.movie.description
        movie_update.description *= 2

        updated_movie = storage.update(
            movie=self.movie,
            movie_in=movie_update,
        )

        self.assertNotEqual(
            source_description,
            updated_movie.description,
        )

        self.assertEqual(
            movie_update,
            MovieUpdate(**updated_movie.model_dump()),
        )

    def test_update_partial(self) -> None:
        movie_partial_update = MoviePartialUpdate(
            description=self.movie.description * 2,
        )
        source_description = self.movie.description

        updated_movie = storage.update_partial(
            movie=self.movie,
            movie_in=movie_partial_update,
        )

        self.assertNotEqual(
            source_description,
            movie_partial_update.description,
        )

        self.assertEqual(
            movie_partial_update.description,
            updated_movie.description,
        )


class MovieStorageGetMovieTestCase(TestCase):

    SHORT_URLS_COUNT = 3
    movies: ClassVar[list[Movie]] = []

    @classmethod
    def setUp(cls) -> None:
        cls.movies = [create_movie() for _ in range(cls.SHORT_URLS_COUNT)]

    @classmethod
    def tearDown(cls) -> None:
        for movie in cls.movies:
            storage.delete(movie)

    def test_get_list(self) -> None:
        movies = storage.get()
        expected_slugs = {su.slug for su in self.movies}
        slugs = {su.slug for su in movies}

        expected_diff = set()
        diff = expected_slugs - slugs

        self.assertEqual(expected_diff, diff)

    def test_get_by_slug(self) -> None:
        for movie in self.movies:
            with self.subTest(
                movie=movie.slug,
                msg=f"Validate can get slug {movie.slug!r}",
            ):
                db_movies = storage.get_by_slug(movie.slug)
                self.assertEqual(
                    movie,
                    db_movies,
                )


@pytest.fixture()
def movie() -> Generator[Movie]:
    movie = create_movie()
    yield movie
    storage.delete(movie)


def test_create_or_raise_if_exists(movie: Movie) -> None:
    movie_create = MovieCreate(**movie.model_dump())
    with pytest.raises(
        MovieAlreadyExists,
    ) as exc_info:
        storage.create_or_raise_if_exists(movie_create)

        assert exc_info.value.args[0] == movie_create.slug
