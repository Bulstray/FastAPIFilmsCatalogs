from typing import Annotated, Any

from fastapi import APIRouter, Form, Request
from fastapi.responses import HTMLResponse, RedirectResponse

from schemas.movie import MovieCreate
from templating import templates

router = APIRouter(
    prefix="/create",
)


@router.get(
    "/",
    name="movies:create-view",
    response_class=HTMLResponse,
)
def get_page_create_movie(request: Request) -> HTMLResponse:
    context: dict[str, Any] = {}
    model_schema = MovieCreate.model_json_schema()
    context.update(
        model_schema=model_schema,
    )

    return templates.TemplateResponse(
        request=request,
        name="movies/create.html",
        context=context,
    )


@router.post(
    "/",
    name="movies:create",
)
def create_movie(
    movie_create: Annotated[
        MovieCreate,
        Form(),
    ],
) -> RedirectResponse:
    return movie_create.model_dump(mode="json")
