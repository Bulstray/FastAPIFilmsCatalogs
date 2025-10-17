from fastapi import APIRouter, Request, status
from fastapi.responses import HTMLResponse, RedirectResponse
from pydantic import ValidationError

from dependencies.movies import GetMoviesStorage, MovieBySlug
from schemas.movie import MoviePartialUpdate, MovieUpdate
from services.movies import FormResponseHelper

router = APIRouter(
    prefix="/{slug}/update",
)

form_response = FormResponseHelper(
    model=MoviePartialUpdate,
    template_name="movies/update.html",
)


@router.get(
    "/",
    name="movies:update-view",
)
def get_page_update(
    request: Request,
    movie: MovieBySlug,
) -> HTMLResponse:
    form = MovieUpdate(**movie.model_dump())
    return form_response.render(
        request=request,
        form_data=form,
        movie=movie,
    )


@router.post(
    "/",
    name="movies:update",
    response_model=None,
)
async def update_movie(
    request: Request,
    movie: MovieBySlug,
    storage: GetMoviesStorage,
) -> HTMLResponse | RedirectResponse:

    async with request.form() as form:
        try:
            movie_in = MoviePartialUpdate.model_validate(form)
        except ValidationError as err:
            return form_response.render(
                request=request,
                form_data=form,
                pydantic_errors=err,
                form_validated=True,
                movie=movie,
            )

    storage.update(
        movie=movie,
        movie_in=movie_in,
    )

    return RedirectResponse(
        url=request.url_for("movies:list"),
        status_code=status.HTTP_303_SEE_OTHER,
    )
