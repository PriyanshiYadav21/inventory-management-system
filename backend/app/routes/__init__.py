"""
API routes module.
Initializes and exports all route routers.
"""

from .products import router as products_router
from .customers import router as customers_router
from .orders import router as orders_router

__all__ = ["products_router", "customers_router", "orders_router"]
