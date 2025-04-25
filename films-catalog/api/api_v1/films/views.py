from typing import Annotated

from fastapi import Depends, APIRouter

from .dependencies import prefetch_film_by_id
from schemas.film import Film
from .crud import FILMS


router = APIRouter(prefix="/films", tags=["Films"])


@router.get(
    "/films/",
    response_model=list[Film],
)
def read_film_list():
    return FILMS


@router.get(
    "/film/{movie_id}",
    response_model=Film,
)
def get_film_by_id(
    film: Annotated[
        Film,
        Depends(prefetch_film_by_id),
    ],
):
    return film
