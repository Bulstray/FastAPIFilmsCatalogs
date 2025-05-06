from fastapi import APIRouter, status, BackgroundTasks, Depends

from api.api_v1.films.crud import storage
from api.api_v1.films.dependencies import user_basic_auth_required

from schemas.movie import Movie, MovieCreate, MovieRead

router = APIRouter()


@router.get(
    "/",
    response_model=list[MovieRead],
)
def read_film_list():
    return storage.get()


@router.post(
    "/",
    response_model=Movie,
    status_code=status.HTTP_201_CREATED,
)
def add_film(
    create_film: MovieCreate,
    background_tasks: BackgroundTasks,
):
    return storage.create(film=create_film)
