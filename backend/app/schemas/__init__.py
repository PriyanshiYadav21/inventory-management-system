"""
Pydantic schemas for request/response validation.
Includes schemas for Product, Customer, Order, and OrderItem.
"""

from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, Field, EmailStr


class ProductBase(BaseModel):
    """Base schema for product data."""
    name: str = Field(..., min_length=1, max_length=255)
    sku: str = Field(..., min_length=1, max_length=100)
    price: float = Field(..., gt=0)
    stock_quantity: int = Field(default=0, ge=0)


class ProductCreate(ProductBase):
    """Schema for creating a new product."""
    pass


class ProductUpdate(BaseModel):
    """Schema for updating a product."""
    name: Optional[str] = Field(None, min_length=1, max_length=255)
    price: Optional[float] = Field(None, gt=0)
    stock_quantity: Optional[int] = Field(None, ge=0)


class ProductResponse(ProductBase):
    """Schema for product response."""
    id: int
    created_at: datetime
    
    class Config:
        from_attributes = True


class CustomerBase(BaseModel):
    """Base schema for customer data."""
    name: str = Field(..., min_length=1, max_length=255)
    email: EmailStr
    phone: str = Field(..., min_length=1, max_length=20)


class CustomerCreate(CustomerBase):
    """Schema for creating a new customer."""
    pass


class CustomerUpdate(BaseModel):
    """Schema for updating a customer."""
    name: Optional[str] = Field(None, min_length=1, max_length=255)
    email: Optional[EmailStr] = None
    phone: Optional[str] = Field(None, min_length=1, max_length=20)


class CustomerResponse(CustomerBase):
    """Schema for customer response."""
    id: int
    created_at: datetime
    
    class Config:
        from_attributes = True


class OrderItemBase(BaseModel):
    """Base schema for order item data."""
    product_id: int
    quantity: int = Field(..., gt=0)


class OrderItemCreate(OrderItemBase):
    """Schema for creating an order item."""
    pass


class OrderItemResponse(OrderItemBase):
    """Schema for order item response."""
    id: int
    order_id: int
    price: float
    
    class Config:
        from_attributes = True


class OrderBase(BaseModel):
    """Base schema for order data."""
    customer_id: int
    items: List[OrderItemCreate] = Field(..., min_items=1)


class OrderCreate(OrderBase):
    """Schema for creating a new order."""
    pass


class OrderResponse(BaseModel):
    """Schema for order response."""
    id: int
    customer_id: int
    total_amount: float
    created_at: datetime
    order_items: List[OrderItemResponse] = []
    
    class Config:
        from_attributes = True


class OrderDetailResponse(OrderResponse):
    """Extended schema for detailed order response."""
    customer: CustomerResponse
    order_items: List[OrderItemResponse]
    
    class Config:
        from_attributes = True


class DashboardStats(BaseModel):
    """Schema for dashboard statistics."""
    total_products: int
    total_customers: int
    total_orders: int
    total_revenue: float
