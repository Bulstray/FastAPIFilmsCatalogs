from fastapi import APIRouter, BackgroundTasks, status

from dependencies.movies import MovieBySlug
from schemas.movie import Movie, MoviePartialUpdate, MovieRead, MovieUpdate
from storage.movies.crud import storage

router = APIRouter()


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
    "/{slug}/",
    status_code=status.HTTP_204_NO_CONTENT,
)
def delete_movie(
    slug: MovieBySlug,
    background_tasks: BackgroundTasks,
) -> None:
    storage.delete(movie=slug)
