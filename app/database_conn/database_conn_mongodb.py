import os

from pymongo import AsyncMongoClient

MONGO_CONN_URL = (f"mongodb://{os.getenv('MONGO_USER')}:"
                  f"{os.getenv('MONGO_PASS')}"
                  f"@{os.getenv('MONGO_URL')}")

client = AsyncMongoClient(MONGO_CONN_URL)
db = client[os.getenv("MONGO_DB_NAME")]


async def get_session_mongo():
    try:
        yield db
    finally:
        pass
