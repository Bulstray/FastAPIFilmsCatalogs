from typing import Annotated
import random

from fastapi import Depends, APIRouter, status, Form

from .dependencies import prefetch_film_by_id
from schemas.film import Film
from .crud import FILMS


router = APIRouter(prefix="/films", tags=["Films"])


@router.get(
    "/films/",
    response_model=list[Film],
)
def read_film_list():
    return


@router.post("/", response_model=Film, status_code=status.HTTP_201_CREATED)
def add_film(name: Annotated[str, Form()], description: Annotated[str, Form()]):
    return Film(name=name, description=description, movie_id=random.randint(3, 100))


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
