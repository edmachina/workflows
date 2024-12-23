from fastapi import APIRouter

from app.src.utils.settings import Settings

settings = Settings()
responses = {
    404: {"description": "Not found"},
    500: {"description": "Internal Server Error"},
}
router = APIRouter(responses={**responses}, prefix=settings.APP_PATH)