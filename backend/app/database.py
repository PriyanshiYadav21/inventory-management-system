"""
Database configuration and session management.
Handles PostgreSQL connection and SQLAlchemy ORM setup.
"""

import os
from pathlib import Path
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy.pool import QueuePool

# Load local .env for database configuration
BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(BASE_DIR / ".env")

# Get database URL from environment variables
DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql://user:password@db:5432/inventory_db"
)

# Create SQLAlchemy engine with connection pooling
engine = create_engine(
    DATABASE_URL,
    poolclass=QueuePool,
    pool_size=10,
    max_overflow=20,
    echo=False,  # Set to True for debugging
    future=True
)

# Create session factory
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
    expire_on_commit=False
)

# Base class for all models
Base = declarative_base()


def get_db():
    """
    Dependency injection function for database sessions.
    Yields a database session and ensures it's properly closed.
    
    Yields:
        SessionLocal: Database session
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def create_tables():
    """Create all database tables based on model definitions."""
    Base.metadata.create_all(bind=engine)


def drop_tables():
    """Drop all database tables. Use with caution."""
    Base.metadata.drop_all(bind=engine)
