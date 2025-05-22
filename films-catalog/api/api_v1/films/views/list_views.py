from fastapi import APIRouter, status, BackgroundTasks, Depends, HTTPException

from api.api_v1.films.crud import storage, MovieAlreadyExists

from schemas.movie import Movie, MovieCreate, MovieRead

router = APIRouter()


@router.get(
    "/",
    response_model=list[MovieRead],
)
def read_film_list() -> list[Movie]:
    return storage.get()


@router.post(
    "/",
    response_model=Movie,
    status_code=status.HTTP_201_CREATED,
    responses={
        status.HTTP_409_CONFLICT: {
            "description": "A movie with such slug already exists",
            "content": {
                "application/json": {
                    "example": {
                        "detail": "Movie with slug='name' already exists",
                    },
                },
            },
        },
    },
)
def add_film(
    create_film: MovieCreate,
    background_tasks: BackgroundTasks,
) -> Movie | None:
    try:
        return storage.create_or_raise_if_exists(create_film)
    except MovieAlreadyExists:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=f"Movie with slug={create_film.slug!r} already exists",
        )
