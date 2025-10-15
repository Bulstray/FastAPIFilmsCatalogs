from unittest import TestCase

from pydantic import ValidationError

from schemas.movie import Movie, MovieCreate


class MovieCreateTestCase(TestCase):
    def test_movie_can_be_created_from_create_schema(self) -> None:
        movie_in = MovieCreate(
            slug="some-slug",
            description="some-description",
            name="some-name",
            url="https://some-url.com",
        )

        movie = Movie(
            **movie_in.model_dump(),
        )

        self.assertEqual(
            movie_in.slug,
            movie.slug,
        )

        self.assertEqual(
            movie_in.name,
            movie.name,
        )

        self.assertEqual(
            movie_in.description,
            movie.description,
        )

    def test_movie_create_accepts_different_movie(self) -> None:
        data = [
            ("name", "desc", "slug", "https://www.google.com"),
            ("description1", "desc2", "slug3", "https://www.google.com"),
            ("description2", "desc3", "slug4", "https://www.google.com"),
        ]

        for name, desc, slug, url in data:
            with self.subTest(name=name, desc=desc, slug=slug, url=url):
                movie_in = MovieCreate(slug=slug, name=name, description=desc, url=url)

                movie = Movie(**movie_in.model_dump())
                self.assertEqual(movie_in.slug, movie.slug)
                self.assertEqual(movie_in.name, movie.name)
                self.assertEqual(movie_in.description, movie.description)

    def test_movie_create_accepts_different_movies(self) -> None:
        with self.assertRaises(ValidationError) as exc_info:
            MovieCreate(
                slug="so",
                name="some-name",
                description="some-description",
                url="https://some-url.com",
            )
        print(exc_info.exception)

    def test_movie_create_raises_validation_error_regex(self) -> None:
        with self.assertRaisesRegex(
            ValidationError,
            expected_regex="String should have at least 3 characters",
        ) as exc_info:
            MovieCreate(
                slug="s",
                name="some-name",
                description="some-description",
                url="https://some-url.com",
            )
        print(exc_info.exception)
