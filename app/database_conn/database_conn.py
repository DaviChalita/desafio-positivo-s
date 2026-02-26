import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

Sessao = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=create_engine(
        url=f"postgresql://{os.getenv("DB_USER")}:"
            f"{os.getenv("DB_PASS")}@"
            f"{os.getenv("DB_HOST")}:"
            f"{os.getenv("DB_PORT")}/"
            f"{os.getenv("DB_NAME")}"
    )
)


def get_session():
    session = Sessao()
    try:
        yield session
    finally:
        session.close()
