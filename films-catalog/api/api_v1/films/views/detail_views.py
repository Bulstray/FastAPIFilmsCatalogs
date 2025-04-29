from typing import Annotated

from fastapi import Depends, APIRouter, status

from api.api_v1.films.crud import storage
from api.api_v1.films.dependencies import prefetch_film_by_id
from schemas.film import Film, FilmUpdate


router = APIRouter()


MovieBySlug = Annotated[Film, Depends(prefetch_film_by_id)]


@router.get(
    "/film/{slug}",
    response_model=Film,
)
def get_film_by_id(film: MovieBySlug):
    return film


@router.put(
    "/{slug}/",
    response_model=Film,
)
def update_film_details(
    movie: MovieBySlug,
    movie_in: FilmUpdate,
):
    return storage.update(
        movie=movie,
        movie_in=movie_in,
    )


@router.delete(
    "/slug/",
    status_code=status.HTTP_204_NO_CONTENT,
)
def delete_movie(
    movie: Annotated[
        Film,
        Depends(prefetch_film_by_id),
    ],
):
    storage.delete(movie=movie)
