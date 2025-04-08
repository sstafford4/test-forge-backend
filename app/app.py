from contextlib import asynccontextmanager
from typing import AsyncGenerator

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api import router as api_router
from app.config import get_settings
from app.mongo import init_mongo

# Load application settings from environment or configuration.
SETTINGS = get_settings()


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator:
    # Connect to MongoDB during app startup
    await init_mongo()
    yield
    # TODO: Add cleanup logic during shutdown (e.g., disconnect MongoDB)


# Create a FastAPI application instance, using the custom lifespan context manager.
app = FastAPI(lifespan=lifespan)

# Apply middleware settings from the configuration.
app.add_middleware(
    CORSMiddleware,
    allow_origins=SETTINGS.origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include API routes for product management.
# The "api_router" contains all the endpoint definitions and is mounted under "/courses.".
app.include_router(api_router, prefix="/courses")
