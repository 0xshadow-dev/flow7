from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

from app.core.config import settings

# Create database engine
engine = create_engine(
    settings.database_url,
    poolclass=StaticPool,
    echo=settings.debug # Log SQL queries in development
)

# Create session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for all models
Base = declarative_base()

# dependency to get database session
def get_db():
    """
    Database session dependency.
    Creates a new session for each request and closes when its done
    """

    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
