from typing import Any

from fastapi import APIRouter, Request, status
from fastapi.responses import HTMLResponse, RedirectResponse
from pydantic import ValidationError

from dependencies.movies import GetMoviesStorage
from misc.flash_messages import flash
from schemas.movie import MovieCreate
from services.movies.form_responce_helper import FormResponseHelper
from storage.movies.exceptions import MovieAlreadyExists
from templating import templates

router = APIRouter(
    prefix="/create",
)

form_response = FormResponseHelper(
    model=MovieCreate,
    template_name="movies/create.html",
)


@router.get(
    "/",
    name="movies:create-view",
    response_class=HTMLResponse,
)
def get_page_create_movie(request: Request) -> HTMLResponse:
    return form_response.render(request)


def format_pydantic_errors(
    error: ValidationError,
) -> dict[str, str]:
    return {f"{err["loc"][0]}": err["msg"] for err in error.errors()}


def create_view_validation_response(
    request: Request,
    errors: dict[str, str] | None = None,
    form_data: object = None,
    form_validated: bool = True,
) -> HTMLResponse:

    context: dict[str, Any] = {}
    model_schema = MovieCreate.model_json_schema()
    context.update(
        model_schema=model_schema,
        errors=errors,
        form_validated=form_validated,
        form_data=form_data,
    )

    return templates.TemplateResponse(
        request=request,
        name="movies/create.html",
        context=context,
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
    )


@router.post(
    "/",
    name="movies:create",
    response_model=None,
)
async def create_movie(
    request: Request,
    storage: GetMoviesStorage,
) -> RedirectResponse | HTMLResponse:
    async with request.form() as form:
        try:
            movie_create = MovieCreate.model_validate(form)
        except ValidationError as error:
            return form_response.render(
                request=request,
                form_data=form,
                pydantic_errors=error,
                form_validated=True,
            )

    try:
        storage.create_or_raise_if_exists(
            movie_create,
        )
    except MovieAlreadyExists:
        errors = {
            "slug": f"Movie already with slug {movie_create.slug!r} already exists.",
        }

    else:
        flash(
            request=request,
            message=f"Successfully created movie with slug {movie_create.slug!r}.",
            category="success",
        )
        return RedirectResponse(
            url=request.url_for("movies:list"),
            status_code=status.HTTP_303_SEE_OTHER,
        )

    return create_view_validation_response(
        request=request,
        errors=errors,
        form_data=movie_create,
        form_validated=True,
    )
