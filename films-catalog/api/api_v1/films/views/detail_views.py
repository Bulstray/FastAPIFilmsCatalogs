from typing import Annotated

from fastapi import Depends, APIRouter, status

from api.api_v1.films.crud import storage
from api.api_v1.films.dependencies import prefetch_film_by_id
from schemas.film import Film, FilmUpdate, FilmPartialUpdate

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


@router.patch(
    "/{slug}/",
    response_model=Film,
)
def update_partial_details(
    movie: MovieBySlug,
    movie_in: FilmPartialUpdate,
):
    return storage.update_partial(
        movie,
        movie_in,
    )


@router.delete(
    "/slug/",
    status_code=status.HTTP_204_NO_CONTENT,
)
def delete_movie(
    movie: MovieBySlug,
):
    storage.delete(movie=movie)
