from contextlib import asynccontextmanager
from typing import AsyncIterator

from fastapi import FastAPI

from storage.movies import FilmsStorage


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncIterator[None]:

    app.state.movies_storage = FilmsStorage()

    yield
