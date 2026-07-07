import logging

from fastapi import APIRouter

logger = logging.getLogger(__name__)

router = APIRouter()


@router.get("/")
async def read_root():
    return {"Hello": "World"}


@router.get("/health")
async def health_check():
    return {"status": "ok"}


@router.get("/version")
async def app_version():
    return {
        "name": "civiscope",
        "version": "0.1.0",
    }


@router.get("/items/{item_id}")
async def read_item(item_id: int, q: str | None = None):
    logger.info(
        "Received request for item_id=%s query=%s",
        item_id,
        q,
    )

    return {"item_id": item_id, "q": q}
