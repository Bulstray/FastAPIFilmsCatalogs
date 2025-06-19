from fastapi import APIRouter, Request

router = APIRouter()


@router.get("/")
def read_docs(
    request: Request,
    name: str = "World",
) -> dict[str, str]:
    docs_url = request.url.replace(
        path="/docs",
    )

    return {
        "docs": str(docs_url),
        "message": f"Hello {name}!",
    }
