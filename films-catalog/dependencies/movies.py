from typing import Annotated

from fastapi import Depends, HTTPException
from fastapi.requests import Request
from starlette import status

from schemas.movie import Movie
from storage.movies import FilmsStorage


def get_movies_storage(
    request: Request,
) -> FilmsStorage:
    return request.app.state.movies_storage  # type: ignore[no-any-return]


GetMoviesStorage = Annotated[
    FilmsStorage,
    Depends(get_movies_storage),
]


def prefetch_film_by_id(
    slug: str,
    storage: GetMoviesStorage,
) -> Movie:
    film: Movie | None = storage.get_by_slug(slug=slug)
    if film:
        print(film)
        return film

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"movie by {slug!r} not found",
    )


MovieBySlug = Annotated[Movie, Depends(prefetch_film_by_id)]
