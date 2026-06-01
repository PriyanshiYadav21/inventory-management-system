"""
Order routes for CRUD operations and order management.
Handles order creation, retrieval, and inventory management.
"""

from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy import func

from app.database import get_db
from app.models import Product, Customer, Order, OrderItem
from app.schemas import (
    OrderCreate,
    OrderResponse,
    OrderDetailResponse,
    DashboardStats
)

router = APIRouter(prefix="/orders", tags=["orders"])


@router.post("", response_model=OrderResponse, status_code=status.HTTP_201_CREATED)
def create_order(
    order_data: OrderCreate,
    db: Session = Depends(get_db)
):
    """
    Create a new order with items.
    
    - **customer_id**: ID of the customer placing the order
    - **items**: List of items with product_id and quantity
    
    Business Rules:
    - Validates customer exists
    - Checks inventory availability for all items
    - Prevents order if stock is insufficient for any item
    - Automatically reduces stock for each product
    - Calculates total order amount
    
    Raises:
        HTTPException: If customer not found, product not found, or insufficient stock
    """
    # Verify customer exists
    customer = db.query(Customer).filter(Customer.id == order_data.customer_id).first()
    if not customer:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Customer not found"
        )
    
    # Validate all products exist and have sufficient stock
    order_items_data = []
    total_amount = 0.0
    
    for item in order_data.items:
        product = db.query(Product).filter(Product.id == item.product_id).first()
        if not product:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Product with ID {item.product_id} not found"
            )
        
        # Check stock availability
        if product.stock_quantity < item.quantity:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Insufficient stock for product '{product.name}'. Available: {product.stock_quantity}, Requested: {item.quantity}"
            )
        
        # Calculate item total and accumulate
        item_total = product.price * item.quantity
        total_amount += item_total
        order_items_data.append((product, item.quantity, product.price))
    
    try:
        # Create order
        db_order = Order(
            customer_id=order_data.customer_id,
            total_amount=total_amount
        )
        db.add(db_order)
        db.flush()  # Get order ID without committing
        
        # Create order items and reduce stock
        for product, quantity, price in order_items_data:
            order_item = OrderItem(
                order_id=db_order.id,
                product_id=product.id,
                quantity=quantity,
                price=price
            )
            db.add(order_item)
            
            # Reduce product stock
            product.stock_quantity -= quantity
        
        db.commit()
        db.refresh(db_order)
        return db_order
    except Exception as e:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Failed to create order: {str(e)}"
        )


@router.get("", response_model=List[OrderResponse])
def get_orders(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db)
):
    """
    Retrieve all orders with pagination.
    
    - **skip**: Number of records to skip (default: 0)
    - **limit**: Maximum number of records to return (default: 100)
    """
    orders = db.query(Order).offset(skip).limit(limit).all()
    return orders

@router.get("/stats/dashboard", response_model=DashboardStats)
def get_dashboard_stats(db: Session = Depends(get_db)):
    """
    Get dashboard statistics.
    
    Returns:
        - total_products: Number of products in inventory
        - total_customers: Number of registered customers
        - total_orders: Number of orders created
        - total_revenue: Total revenue from all orders
    """
    total_products = db.query(func.count(Product.id)).scalar() or 0
    total_customers = db.query(func.count(Customer.id)).scalar() or 0
    total_orders = db.query(func.count(Order.id)).scalar() or 0
    total_revenue = db.query(func.sum(Order.total_amount)).scalar() or 0.0
    
    return DashboardStats(
        total_products=total_products,
        total_customers=total_customers,
        total_orders=total_orders,
        total_revenue=total_revenue
    )

@router.get("/{order_id}", response_model=OrderDetailResponse)
def get_order(
    order_id: int,
    db: Session = Depends(get_db)
):
    """
    Retrieve a specific order by ID with full details.
    Includes customer information and all order items.
    
    Raises:
        HTTPException: If order not found
    """
    order = db.query(Order).filter(Order.id == order_id).first()
    if not order:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Order not found"
        )
    return order