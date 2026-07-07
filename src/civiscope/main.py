import logging
from pathlib import Path

from fastapi import FastAPI

LOG_DIR = Path("logs")
LOG_DIR.mkdir(exist_ok=True)

LOG_FORMAT = "%(asctime)s | %(levelname)s | %(name)s | %(message)s"

file_handler = logging.FileHandler(
    LOG_DIR / "app.log",
    encoding="utf-8",
)

file_handler.setFormatter(logging.Formatter(LOG_FORMAT))

logger = logging.getLogger(__name__)

logger.setLevel(logging.INFO)
logger.addHandler(file_handler)
logger.propagate = False


app = FastAPI()


@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
async def read_item(item_id: int, q: str | None = None):
    logger.info(
        "Received request for item_id=%s query=%s",
        item_id,
        q,
    )

    return {"item_id": item_id, "q": q}


@app.get("/health")
async def health_check():
    return {"status": "ok"}


@app.get("/version")
async def version():
    return {"name": "civiscope", "version": "0.1.0"}
