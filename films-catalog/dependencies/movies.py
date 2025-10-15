from typing import Annotated

from fastapi import Depends
from fastapi.requests import Request

from storage.movies import FilmsStorage


def get_movies_storage(
    request: Request,
) -> FilmsStorage:
    return request.app.state.movies_storage  # type: ignore[no-any-return]


GetMoviesStorage = Annotated[
    FilmsStorage,
    Depends(get_movies_storage),
]
