from pydantic import BaseModel

from schemas.film import Film, FilmCreate, FilmUpdate, FilmPartialUpdate

FILMS = [
    FilmCreate(
        slug="abc",
        name="Остров проклятых",
        description="Фильм про психбольницу",
    ),
    FilmCreate(
        slug="foo",
        name="Джентельмены",
        description="Фильм про мафию",
    ),
    FilmCreate(
        slug="bar",
        name="Область тьмы",
        description="Фильм про работу мозга",
    ),
]


class FilmsStorage(BaseModel):
    slug_to_film: dict[str, Film] = {}

    def get(self) -> list[Film]:
        return [self.slug_to_film[film] for film in self.slug_to_film]

    def get_by_slug(self, slug):
        return self.slug_to_film.get(slug)

    def create(self, film: FilmCreate) -> Film:
        film = Film(**film.model_dump())
        self.slug_to_film[film.slug] = film
        return film

    def delete_by_slag(self, slug) -> None:
        self.slug_to_film.pop(slug, None)

    def delete(self, movie: Film) -> None:
        self.delete_by_slag(slug=movie.slug)

    def update(
        self,
        movie: Film,
        movie_in: FilmUpdate,
    ) -> Film:
        for field_name, value in movie_in:
            setattr(movie, field_name, value)

        return movie

    def update_partial(
        self,
        movie: Film,
        movie_in: FilmPartialUpdate,
    ):
        for field_name, value in movie_in.model_dump(exclude_unset=True).items():
            setattr(movie, field_name, value)


storage = FilmsStorage()


for film in FILMS:
    storage.create(film=film)
