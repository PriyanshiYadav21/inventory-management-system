"""
Main FastAPI application.
Initializes the API, configures middleware, and registers routes.
"""

from contextlib import asynccontextmanager
from pathlib import Path
from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import os

# Load environment from .env before imports and configuration
BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(BASE_DIR / ".env")

from app.database import create_tables
from app.routes import products_router, customers_router, orders_router

# Get environment variables
FRONTEND_URL = os.getenv("FRONTEND_URL", "http://localhost:5173")
ENVIRONMENT = os.getenv("ENVIRONMENT", "development")


@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Application lifespan events.
    Handles startup and shutdown tasks.
    """
    # Startup
    print(f"Starting Inventory Management System in {ENVIRONMENT} mode...")
    try:
        create_tables()
        print("Database tables created/verified")
    except Exception as exc:
        print(
            f"WARNING: Failed to initialize database tables: {exc}\n"
            "Please verify DATABASE_URL, database availability, and .env configuration."
        )
    yield
    # Shutdown
    print("Shutting down application...")


# Create FastAPI application
app = FastAPI(
    title="Inventory Management System API",
    description="Complete REST API for inventory and order management",
    version="1.0.0",
    lifespan=lifespan
)

# CORS Configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=[FRONTEND_URL, "http://localhost:3000", "http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register routers
app.include_router(products_router)
app.include_router(customers_router)
app.include_router(orders_router)


@app.get("/", tags=["health"])
def read_root():
    """Root endpoint - API health check."""
    return {
        "message": "Inventory Management System API",
        "status": "healthy",
        "environment": ENVIRONMENT,
        "docs": "/docs",
        "openapi_schema": "/openapi.json"
    }


@app.get("/health", tags=["health"])
def health_check():
    """Health check endpoint."""
    return {
        "status": "healthy",
        "service": "inventory-management-system"
    }


if __name__ == "__main__":
    import uvicorn
    
    # Development server
    uvicorn.run(
        "app.main:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
        env_file=".env"
    )
