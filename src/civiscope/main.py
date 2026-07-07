import logging
from pathlib import Path

from fastapi import FastAPI

from civiscope.api.routes import router

LOG_DIR = Path("logs")
LOG_DIR.mkdir(exist_ok=True)

LOG_FORMAT = "%(asctime)s | %(levelname)s | %(name)s | %(message)s"

file_handler = logging.FileHandler(
    LOG_DIR / "app.log",
    encoding="utf-8",
)

file_handler.setFormatter(logging.Formatter(LOG_FORMAT))

logger = logging.getLogger("civiscope")
logger.setLevel(logging.INFO)
logger.addHandler(file_handler)
logger.propagate = False


app = FastAPI()

app.include_router(router)
