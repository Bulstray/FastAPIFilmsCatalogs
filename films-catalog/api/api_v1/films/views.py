from typing import Annotated
import random

from fastapi import Depends, APIRouter, status, Form

from .dependencies import prefetch_film_by_id
from schemas.film import Film, FilmCreate


router = APIRouter(prefix="/films", tags=["Films"])


@router.get(
    "/films/",
    response_model=list[Film],
)
def read_film_list():
    return


@router.post(
    "/",
    response_model=Film,
    status_code=status.HTTP_201_CREATED,
)
def add_film(slug: str, create_film: FilmCreate):
    return Film(
        slug=slug,
        **create_film.model_dump(),
    )


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
