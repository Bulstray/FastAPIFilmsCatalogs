from fastapi import HTTPException
from starlette import status

from .crud import storage
from schemas.film import Film


def prefetch_film_by_id(slug) -> Film:
    film: Film | None = storage.get_by_slug(slug=slug)
    print(film)
    if film:
        return film

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"movie by {slug!r} not found",
    )
