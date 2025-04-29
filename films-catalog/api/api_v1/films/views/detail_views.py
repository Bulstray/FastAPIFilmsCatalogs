from typing import Annotated

from fastapi import Depends, APIRouter, status

from api.api_v1.films.crud import storage
from api.api_v1.films.dependencies import prefetch_film_by_id
from schemas.movie import Movie, MovieUpdate, MoviePartialUpdate, MovieRead

router = APIRouter()


MovieBySlug = Annotated[Movie, Depends(prefetch_film_by_id)]


@router.get(
    "/film/{slug}",
    response_model=MovieRead,
)
def get_film_by_id(movie: MovieBySlug) -> Movie:
    return movie


@router.put(
    "/{slug}/",
    response_model=MovieRead,
)
def update_film_details(
    movie: MovieBySlug,
    movie_in: MovieUpdate,
):
    return storage.update(
        movie=movie,
        movie_in=movie_in,
    )


@router.patch(
    "/{slug}/",
    response_model=MovieRead,
)
def update_partial_details(
    movie: MovieBySlug,
    movie_in: MoviePartialUpdate,
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
