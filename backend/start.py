from contextlib import asynccontextmanager

from fastapi import FastAPI
from backend.api.handler import router
import uvicorn
from backend.logger import status_logger

import os
@asynccontextmanager
async def app_logger(application):
	status_logger.info("Starting my new application")
	yield
	status_logger.info("Shutting down application")


app = FastAPI(lifespan=app_logger)#docs_url=None, redoc_url=None
app.include_router(router, prefix="/api")

if __name__ == "__main__":
	uvicorn.run(app, host="127.0.0.1", port=8000)
