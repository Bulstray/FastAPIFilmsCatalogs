from fastapi import APIRouter

from rest.movies.list_views import router as list_views_router

from .create_views import router as create_views_router

router = APIRouter(
    tags=["movies REST"],
    prefix="/movies",
)

router.include_router(list_views_router)
router.include_router(create_views_router)
