import logging
from contextlib import asynccontextmanager
from temporalio.client import Client
from fastapi import FastAPI

from app.src.utils.settings import Settings
from app.src.controllers.apiRouter import router

settings = Settings()

@asynccontextmanager
async def lifespan(fa_app: FastAPI):
    logging.info("Setting up temporal client")
    fa_app.state.temporal_client = await Client.connect('localhost:7233')
    yield

app = FastAPI(root_path=settings.APP_PATH, lifespan=lifespan)

app.include_router(router)
