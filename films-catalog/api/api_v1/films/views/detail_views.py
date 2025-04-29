from typing import Annotated

from fastapi import Depends, APIRouter, status

from api.api_v1.films.crud import storage
from api.api_v1.films.dependencies import prefetch_film_by_id
from schemas.film import Film


router = APIRouter()


@router.get(
    "/film/{slug}",
    response_model=Film,
)
def get_film_by_id(
    film: Annotated[
        Film,
        Depends(prefetch_film_by_id),
    ],
):
    return film


@router.delete(
    "/slug/",
    status_code=status.HTTP_204_NO_CONTENT,
    responses={
        status.HTTP_404_NOT_FOUND: {
            "description": "Film not found",
            "content": {
                "application/json": {"detail": "Film 'slug' not found"},
            },
        },
    },
)
def delete_movie(
    movie: Annotated[
        Film,
        Depends(prefetch_film_by_id),
    ],
):
    storage.delete(movie=movie)
