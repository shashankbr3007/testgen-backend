from fastapi import FastAPI
from app.api.testgen import router
from app.core.logging_config import setup_logging

from app.api.testgen import router as testgen_router
from app.api.health import router as health_router
from app.api.upload import router as upload_router

setup_logging()

app = FastAPI()
app.include_router(health_router, prefix="/api")
app.include_router(testgen_router, prefix="/api")
app.include_router(upload_router, prefix="/api")    