import os
os.environ['DATABASE_URL'] = 'sqlite:///:memory:'
from app.database import Base, engine, SessionLocal
from app.models import Product, Customer, Order, OrderItem
from app.routes.orders import get_dashboard_stats

Base.metadata.create_all(bind=engine)

db = SessionLocal()
try:
    db.add(Customer(name='Test', email='test@example.com', phone='123'))
    db.add(Product(name='Prod', sku='P1', price=10.0, stock_quantity=5))
    db.commit()
    print('DB ready')
    stats = get_dashboard_stats(db=db)
    print(stats)
finally:
    db.close()
