#!/usr/bin/env python3
"""
Database initialization script.
Creates all tables and optionally seeds sample data.
"""

import os
import sys
from pathlib import Path

# Add backend to path
sys.path.insert(0, str(Path(__file__).parent / 'backend'))

from app.database import create_tables, SessionLocal, engine
from app.models import Product, Customer, Order, OrderItem
from datetime import datetime


def seed_sample_data():
    """Seed database with sample data."""
    db = SessionLocal()
    
    try:
        # Create sample products
        products = [
            Product(
                name="Laptop",
                sku="SKU-001",
                price=999.99,
                stock_quantity=15
            ),
            Product(
                name="Wireless Mouse",
                sku="SKU-002",
                price=29.99,
                stock_quantity=50
            ),
            Product(
                name="Mechanical Keyboard",
                sku="SKU-003",
                price=129.99,
                stock_quantity=30
            ),
            Product(
                name="USB-C Hub",
                sku="SKU-004",
                price=49.99,
                stock_quantity=25
            ),
            Product(
                name="Monitor 27 inch",
                sku="SKU-005",
                price=299.99,
                stock_quantity=10
            ),
        ]
        
        # Create sample customers
        customers = [
            Customer(
                name="John Doe",
                email="john@example.com",
                phone="+1-555-0001"
            ),
            Customer(
                name="Jane Smith",
                email="jane@example.com",
                phone="+1-555-0002"
            ),
            Customer(
                name="Bob Johnson",
                email="bob@example.com",
                phone="+1-555-0003"
            ),
            Customer(
                name="Alice Williams",
                email="alice@example.com",
                phone="+1-555-0004"
            ),
        ]
        
        # Add products
        for product in products:
            db.add(product)
        db.flush()
        
        # Add customers
        for customer in customers:
            db.add(customer)
        db.flush()
        
        # Create sample order
        if products and customers:
            order = Order(
                customer_id=customers[0].id,
                total_amount=0.0
            )
            db.add(order)
            db.flush()
            
            # Add order items
            item1 = OrderItem(
                order_id=order.id,
                product_id=products[0].id,
                quantity=1,
                price=products[0].price
            )
            item2 = OrderItem(
                order_id=order.id,
                product_id=products[1].id,
                quantity=2,
                price=products[1].price
            )
            
            # Update order total
            order.total_amount = (item1.quantity * item1.price) + (item2.quantity * item2.price)
            
            db.add(item1)
            db.add(item2)
        
        db.commit()
        print("✅ Sample data created successfully!")
        
    except Exception as e:
        db.rollback()
        print(f"❌ Error seeding data: {e}")
    finally:
        db.close()


def main():
    """Main function."""
    print("📊 Inventory Management System - Database Setup")
    print("=" * 50)
    
    # Create tables
    print("Creating database tables...")
    create_tables()
    print("✅ Tables created successfully!")
    
    # Seed sample data
    print("\nSeeding sample data...")
    seed_sample_data()
    
    print("\n" + "=" * 50)
    print("🎉 Database setup complete!")
    print("\nYou can now access:")
    print("  - API: http://localhost:8000")
    print("  - Docs: http://localhost:8000/docs")
    print("  - Frontend: http://localhost:5173")


if __name__ == "__main__":
    main()
