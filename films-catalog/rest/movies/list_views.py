from typing import Any

from fastapi import APIRouter
from fastapi.requests import Request
from fastapi.responses import HTMLResponse

from dependencies.movies import GetMoviesStorage
from templating import templates

router = APIRouter()


@router.get("/", name="movies:list", response_class=HTMLResponse)
def list_view(
    request: Request,
    storage: GetMoviesStorage,
) -> HTMLResponse:
    context: dict[str, Any] = {}
    movies = storage.get()
    context.update(movies=movies)

    return templates.TemplateResponse(
        request=request,
        name="movies/list.html",
        context=context,
    )
