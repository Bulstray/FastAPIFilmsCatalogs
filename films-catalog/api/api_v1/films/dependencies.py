from fastapi import HTTPException
from starlette import status

from .crud import FILMS
from schemas.film import Film


def prefetch_film_by_id(movie_id: int) -> Film:
    film: Film | None = next(
        (film for film in FILMS if film.movie_id == movie_id),
        None,
    )

    if film:
        return film

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"movie by {movie_id!r} not found",
    )
