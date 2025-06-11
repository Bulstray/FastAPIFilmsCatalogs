from unittest import TestCase

from pydantic import ValidationError

from schemas.movie import Movie, MovieCreate


class MovieCreateTestCase(TestCase):
    def test_movie_can_be_created_from_create_schema(self) -> None:
        movie_in = MovieCreate(
            slug="some-slug",
            description="some-description",
            name="some-name",
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

        self.assertEqual(
            movie_in.notes,
            movie.notes,
        )

    def test_movie_create_accepts_different_movie(self) -> None:
        data = [
            ("name", "desc", "slug"),
            ("description1", "desc2", "slug3"),
            ("description2", "desc3", "slug4"),
        ]

        for name, desc, slug in data:
            with self.subTest(name=name, desc=desc, slug=slug):
                movie_in = MovieCreate(
                    slug=slug,
                    name=name,
                    description=desc,
                )

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
            )
        print(exc_info.exception)
