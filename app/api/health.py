from fastapi import APIRouter
from app.core.config import settings
from openai import OpenAI

router = APIRouter()

@router.get("/health")
async def health_check():
    ai_status = "unknown"

    # OpenAI check
    try:
        client = OpenAI(api_key=settings.OPENAI_API_KEY)
        ai_status = "ok"
    except Exception:
        ai_status = "error"

    return {
        "status": "ok",
        "openai_api": ai_status
    }
