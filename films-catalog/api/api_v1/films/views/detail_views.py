from typing import Annotated

from fastapi import APIRouter, BackgroundTasks, Depends, status

from api.api_v1.films.crud import storage
from api.api_v1.films.dependencies import prefetch_film_by_id
from schemas.movie import Movie, MoviePartialUpdate, MovieRead, MovieUpdate

router = APIRouter()


MovieBySlug = Annotated[Movie, Depends(prefetch_film_by_id)]


@router.get(
    "/film/{slug}/",
    response_model=MovieRead,
)
def get_film_by_id(
    slug: MovieBySlug,
) -> Movie:
    return slug


@router.put(
    "/{slug}/",
    response_model=MovieRead,
)
def update_film_details(
    slug: MovieBySlug,
    movie_in: MovieUpdate,
    background_tasks: BackgroundTasks,
) -> Movie:
    return storage.update(
        movie=slug,
        movie_in=movie_in,
    )


@router.patch(
    "/{slug}/",
    response_model=MovieRead,
)
def update_partial_details(
    slug: MovieBySlug,
    movie_in: MoviePartialUpdate,
    background_tasks: BackgroundTasks,
) -> Movie:
    return storage.update_partial(
        slug,
        movie_in,
    )


@router.delete(
    "/slug/",
    status_code=status.HTTP_204_NO_CONTENT,
)
def delete_movie(
    slug: MovieBySlug,
    background_tasks: BackgroundTasks,
) -> None:
    storage.delete(movie=slug)
