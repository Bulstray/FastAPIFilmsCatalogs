import logging

import uvicorn
from fastapi import FastAPI
from starlette.middleware.sessions import SessionMiddleware

from api import router as api_router
from app_lifespan import lifespan
from core.config import settings
from rest import router as main_router

logging.basicConfig(
    level=settings.logging.log_level,
    format=settings.logging.log_format,
    datefmt=settings.logging.date_format,
)

app = FastAPI(
    title="Films Catalog",
    lifespan=lifespan,
)

app.add_middleware(
    SessionMiddleware,
    secret_key=settings.session.secret_key,
)

app.include_router(main_router)
app.include_router(api_router)

if __name__ == "__main__":
    uvicorn.run(app)
