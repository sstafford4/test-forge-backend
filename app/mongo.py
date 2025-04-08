"""
Module for initializing MongoDB connection and configuring Beanie ODM.

This module sets up the connection to the MongoDB database using Motor and initializes
Beanie with the application's document models.
"""

from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient
from app.documents import Course, Quiz, CourseMaterial
from app.config import get_settings

"""
Import any documents created here: 
"""

# Retrieve application settings which include MongoDB connection details.
SETTINGS = get_settings()


async def init_mongo() -> None:
    # Create a Motor client to interact with MongoDB.
    client: AsyncIOMotorClient = AsyncIOMotorClient(SETTINGS.mongodb_url)

    # Access the database using the name provided in the settings.
    db = client[SETTINGS.db_name]

    # Initialize Beanie with the database and the list of document models.
    await init_beanie(database=db, document_models=[Course, Quiz, CourseMaterial])


async def drop_database() -> None:
    client: AsyncIOMotorClient = AsyncIOMotorClient(SETTINGS.mongodb_url)
    await client.drop_database(SETTINGS.db_name)


async def close_mongo() -> None:
    client: AsyncIOMotorClient = AsyncIOMotorClient(SETTINGS.mongodb_url)
    client.close()
