"""
Product model for inventory management.
Stores product information including SKU, price, and stock quantity.
"""

from datetime import datetime
from sqlalchemy import Column, Integer, String, Float, DateTime
from sqlalchemy.orm import relationship
from app.database import Base


class Product(Base):
    """
    Product model representing items in the inventory.
    
    Attributes:
        id: Primary key
        name: Product name
        sku: Stock Keeping Unit (unique identifier)
        price: Product price
        stock_quantity: Current stock quantity
        created_at: Timestamp of creation
    """
    
    __tablename__ = "products"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False, index=True)
    sku = Column(String(100), unique=True, nullable=False, index=True)
    price = Column(Float, nullable=False)
    stock_quantity = Column(Integer, default=0, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    
    # Relationships
    order_items = relationship("OrderItem", back_populates="product", cascade="all, delete-orphan")
    
    def __repr__(self):
        return f"<Product(id={self.id}, name='{self.name}', sku='{self.sku}', stock={self.stock_quantity})>"
