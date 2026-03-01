# app/tests/conftest.py

import os
from dotenv import load_dotenv

def pytest_configure():
    load_dotenv()

    os.environ.setdefault("MONGO_DB_NAME", "projeto-positivo-s")
    os.environ.setdefault("MONGO_USER", "mock")
    os.environ.setdefault("MONGO_PASS", "mock")
    os.environ.setdefault("MONGO_URL", "mockurl:27017")
