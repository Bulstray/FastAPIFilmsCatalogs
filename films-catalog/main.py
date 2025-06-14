import logging

import uvicorn
from fastapi import FastAPI, Request

from api import router as api_router
from core import config

logging.basicConfig(
    level=config.LOG_LEVEL,
    format=config.LOG_FORMAT,
)

app = FastAPI(
    title="Films Catalog",
)

app.include_router(
    api_router,
)


@app.get("/")
def read_docs(request: Request) -> dict[str, str]:
    docs_url = request.url.replace(
        path="/docs",
    )

    return {"docs": str(docs_url)}


if __name__ == "__main__":
    uvicorn.run(app)
