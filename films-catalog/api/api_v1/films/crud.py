from pydantic import BaseModel

from schemas.movie import (
    Movie,
    MovieCreate,
    MovieUpdate,
    MoviePartialUpdate,
    MovieRead,
)

FILMS = [
    MovieCreate(
        slug="abc",
        name="Остров проклятых",
        description="Фильм про психбольницу",
    ),
    MovieCreate(
        slug="foo",
        name="Джентельмены",
        description="Фильм про мафию",
    ),
    MovieCreate(
        slug="bar",
        name="Область тьмы",
        description="Фильм про работу мозга",
    ),
]


class FilmsStorage(BaseModel):
    slug_to_film: dict[str, Movie] = {}

    def get(self) -> list[MovieRead]:
        return [self.slug_to_film[film] for film in self.slug_to_film]

    def get_by_slug(self, slug):
        return self.slug_to_film.get(slug)

    def create(self, film: MovieCreate) -> Movie:
        film = Movie(**film.model_dump())
        self.slug_to_film[film.slug] = film
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


for film in FILMS:
    storage.create(film=film)
