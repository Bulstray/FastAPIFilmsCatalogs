from fastapi import APIRouter, status

from api.api_v1.films.crud import storage

from schemas.film import Film, FilmCreate


router = APIRouter()


@router.get(
    "/",
    response_model=list[Film],
)
def read_film_list():
    return storage.get()


@router.post(
    "/",
    response_model=Film,
    status_code=status.HTTP_201_CREATED,
)
def add_film(create_film: FilmCreate):
    return Film(
        **create_film.model_dump(),
    )
