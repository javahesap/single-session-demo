"""Database setup and initialization."""

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

DATABASE_URL = "sqlite:///app.db"

# SQLAlchemy base and session setup
engine = create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()


def init_db() -> None:
    """Import all models and create tables."""
    from models.product import Product  # noqa: F401

    Base.metadata.create_all(bind=engine)


# Run migrations automatically on import
init_db()
