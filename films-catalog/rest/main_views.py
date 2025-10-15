from typing import Any

from fastapi import APIRouter
from fastapi.requests import Request
from fastapi.responses import HTMLResponse

from templating import templates

router = APIRouter(include_in_schema=False)


@router.get(
    "/",
    name="home",
)
def read_docs(request: Request) -> HTMLResponse:
    context: dict[str, Any] = {}
    features = [
        "Create new movie",
        "Real time statistics",
    ]
    context.update(
        features=features,
    )
    return templates.TemplateResponse(
        request=request,
        name="home.html",
        context=context,
    )


@router.get(
    "/about/",
    name="about",
)
def about_page(request: Request) -> HTMLResponse:
    return templates.TemplateResponse(
        request=request,
        name="about.html",
    )
