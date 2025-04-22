from fastapi import APIRouter

from . import image

router: APIRouter = APIRouter()

router.include_router(image.router)


__all__ = ["router"]
