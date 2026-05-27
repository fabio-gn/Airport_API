from fastapi import FastAPI
from contextlib import asynccontextmanager
import logging

from .router import router
from .logging_config import setup_logging

setup_logging()
logger = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("Airport API started")
    yield


app = FastAPI(title="Airport API", lifespan=lifespan)

app.include_router(router)


@app.get("/")
def root():
    logger.info("Health check called")
    return {"message": "Airport API is running"}