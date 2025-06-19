import logging

import uvicorn
from fastapi import FastAPI

from api import router as api_router
from api.main_views import router as main_router
from core import config

logging.basicConfig(
    level=config.LOG_LEVEL,
    format=config.LOG_FORMAT,
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
