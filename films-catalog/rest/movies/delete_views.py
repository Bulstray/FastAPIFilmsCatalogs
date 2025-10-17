from fastapi import APIRouter, Response, status

from dependencies.movies import GetMoviesStorage, MovieBySlug

router = APIRouter(prefix="/{slug}/delete")


@router.delete(
    "/",
    name="movies:delete",
)
async def delete_movies(
    storage: GetMoviesStorage,
    movie: MovieBySlug,
) -> Response:

    storage.delete(movie=movie)
    return Response(
        status_code=status.HTTP_200_OK,
        content="",
    )
