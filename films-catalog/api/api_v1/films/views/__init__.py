__all__ = ("router",)

from fastapi import APIRouter
from fastapi.params import Depends

from .list_views import router as list_router
from .detail_views import router as detail_router
from ..dependencies import save_storage_state

router = APIRouter(
    prefix="/films",
    tags=["Films"],
    dependencies=[Depends(save_storage_state)],
)

router.include_router(list_router)
router.include_router(detail_router)
