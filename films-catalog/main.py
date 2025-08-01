import logging

import uvicorn
from fastapi import FastAPI

from api import router as api_router
from api.main_views import router as main_router
from core.config import settings

logging.basicConfig(
    level=settings.logging.log_level,
    format=settings.logging.log_format,
    datefmt=settings.logging.date_format,
)

app = FastAPI(
    title="Films Catalog",
)
app.include_router(
    main_router,
)

app.include_router(
    api_router,
)

if __name__ == "__main__":
    uvicorn.run(app)
