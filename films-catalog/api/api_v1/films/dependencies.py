import logging

from fastapi import HTTPException, BackgroundTasks
from starlette import status

from .crud import storage
from schemas.movie import Movie

log = logging.getLogger(__name__)


def prefetch_film_by_id(slug) -> Movie:
    film: Movie | None = storage.get_by_slug(slug=slug)
    print(film)
    if film:
        return film

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"movie by {slug!r} not found",
    )


def save_storage_state(background_tasks: BackgroundTasks):
    yield
    log.info("Add background task to save storage")
    background_tasks.add_task(storage.save_state)
