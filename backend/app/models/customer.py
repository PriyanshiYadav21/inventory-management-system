"""
Customer model for managing customer information.
Stores customer details including name, email, and phone.
"""

from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship
from app.database import Base


class Customer(Base):
    """
    Customer model representing individuals who make orders.
    
    Attributes:
        id: Primary key
        name: Customer's full name
        email: Customer's email address (unique)
        phone: Customer's phone number
        created_at: Timestamp of creation
    """
    
    __tablename__ = "customers"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False, index=True)
    email = Column(String(255), unique=True, nullable=False, index=True)
    phone = Column(String(20), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    
    # Relationships
    orders = relationship("Order", back_populates="customer", cascade="all, delete-orphan")
    
    def __repr__(self):
        return f"<Customer(id={self.id}, name='{self.name}', email='{self.email}')>"
