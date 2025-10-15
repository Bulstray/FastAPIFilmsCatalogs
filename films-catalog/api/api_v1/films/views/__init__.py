__all__ = ("router",)

from fastapi import APIRouter, status
from fastapi.params import Depends

from dependencies.auth import api_token_or_auth_required_for_unsafe_methods

from .detail_views import router as detail_router
from .list_views import router as list_router

router = APIRouter(
    prefix="/films",
    tags=["Films"],
    dependencies=[
        Depends(api_token_or_auth_required_for_unsafe_methods),
    ],
    responses={
        status.HTTP_401_UNAUTHORIZED: {
            "description": "Unauthenticated. Only for unsafe methods.",
            "content": {
                "application/json": {
                    "example": {
                        "detail": "Invalid API token",
                    },
                },
            },
        },
    },
)

router.include_router(list_router)
router.include_router(detail_router)
