# Inventory & Order Management System

A complete full-stack Inventory and Order Management System built with modern technologies for efficient inventory tracking, customer management, and order processing.

## 📋 Table of Contents

- [Features](#features)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Prerequisites](#prerequisites)
- [Local Development Setup](#local-development-setup)
- [Docker Setup](#docker-setup)
- [API Documentation](#api-documentation)
- [Database Schema](#database-schema)
- [Business Rules & Validation](#business-rules--validation)
- [Frontend Features](#frontend-features)
- [Deployment Guide](#deployment-guide)
- [Troubleshooting](#troubleshooting)

## 🚀 Features

### Core Features

- **Product Management**: Add, edit, delete, and track products with SKU, pricing, and stock levels
- **Customer Management**: Manage customer information with email and phone validation
- **Order Management**: Create and manage orders with automatic inventory reduction
- **Dashboard**: Real-time statistics showing total products, customers, orders, and revenue
- **Inventory Tracking**: Real-time stock level updates with visual indicators
- **Responsive Design**: Mobile-friendly interface for all devices

### Business Rules

- ✅ Unique SKU requirement for each product
- ✅ Unique email requirement for each customer
- ✅ Prevent negative stock quantities
- ✅ Inventory validation before order creation
- ✅ Automatic stock reduction on order placement
- ✅ Automatic calculation of order totals
- ✅ Comprehensive error handling and validation

## 🛠 Tech Stack

### Backend

- **Framework**: FastAPI (Python)
- **Database**: PostgreSQL 16
- **ORM**: SQLAlchemy
- **Validation**: Pydantic
- **Server**: Uvicorn

### Frontend

- **Library**: React 18
- **Build Tool**: Vite
- **Router**: React Router v6
- **HTTP Client**: Axios
- **Styling**: Tailwind CSS
- **Package Manager**: npm

### DevOps

- **Containerization**: Docker & Docker Compose
- **PostgreSQL**: Version 16 (Alpine)
- **Python**: 3.11
- **Node.js**: 20

## 📁 Project Structure

```
inventory-management-system/
├── backend/
│   ├── app/
│   │   ├── models/
│   │   │   ├── __init__.py
│   │   │   ├── product.py        # Product model
│   │   │   ├── customer.py       # Customer model
│   │   │   ├── order.py          # Order model
│   │   │   └── order_item.py     # OrderItem model
│   │   ├── routes/
│   │   │   ├── __init__.py
│   │   │   ├── products.py       # Product endpoints
│   │   │   ├── customers.py      # Customer endpoints
│   │   │   └── orders.py         # Order endpoints
│   │   ├── schemas/
│   │   │   └── __init__.py       # Pydantic schemas
│   │   ├── __init__.py
│   │   ├── database.py           # Database configuration
│   │   └── main.py               # FastAPI application
│   ├── Dockerfile                # Backend container
│   ├── .dockerignore
│   ├── requirements.txt          # Python dependencies
│   ├── .env.example              # Environment template
│   └── wsgi.py                   # Production ASGI entry
│
├── frontend/
│   ├── src/
│   │   ├── pages/
│   │   │   ├── Dashboard.jsx     # Dashboard page
│   │   │   ├── Products.jsx      # Products management
│   │   │   ├── Customers.jsx     # Customers management
│   │   │   └── Orders.jsx        # Orders management
│   │   ├── components/
│   │   │   ├── Layout.jsx        # Main layout with navigation
│   │   │   └── StatCard.jsx      # Statistics card component
│   │   ├── services/
│   │   │   └── api.js            # API client
│   │   ├── App.jsx               # Main app component
│   │   ├── main.jsx              # Entry point
│   │   └── index.css             # Global styles
│   ├── Dockerfile                # Frontend container
│   ├── .dockerignore
│   ├── index.html                # HTML template
│   ├── package.json              # Node dependencies
│   ├── vite.config.js            # Vite configuration
│   ├── tailwind.config.js        # Tailwind configuration
│   ├── postcss.config.js         # PostCSS configuration
│   └── .env.example              # Environment template
│
├── docker-compose.yml            # Docker Compose orchestration
└── README.md                      # This file
```

## 📋 Prerequisites

### For Local Development

- **Python 3.11+**: [Download](https://www.python.org/downloads/)
- **Node.js 20+**: [Download](https://nodejs.org/)
- **PostgreSQL 16**: [Download](https://www.postgresql.org/download/)

### For Docker Setup

- **Docker**: [Install Docker](https://docs.docker.com/get-docker/)
- **Docker Compose**: [Install Docker Compose](https://docs.docker.com/compose/install/)

## 🚀 Local Development Setup

### Backend Setup

1. **Navigate to backend directory**

   ```bash
   cd backend
   ```

2. **Create virtual environment**

   ```bash
   python -m venv venv

   # On Windows
   venv\Scripts\activate

   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Create .env file**

   ```bash
   cp .env.example .env
   ```

5. **Configure database connection in .env**

   ```
   DATABASE_URL=postgresql://inventory_user:inventory_password@localhost:5432/inventory_db
   ENVIRONMENT=development
   SECRET_KEY=your-secret-key
   FRONTEND_URL=http://localhost:5173
   ```

6. **Create PostgreSQL database**

   ```bash
   # Using psql
   createdb -U inventory_user inventory_db
   ```

7. **Start the backend server**

   ```bash
   python -m uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
   ```

   The API will be available at: http://localhost:8000
   - Interactive API docs: http://localhost:8000/docs
   - ReDoc: http://localhost:8000/redoc

### Frontend Setup

1. **Navigate to frontend directory**

   ```bash
   cd frontend
   ```

2. **Install dependencies**

   ```bash
   npm install
   ```

3. **Create .env file**

   ```bash
   cp .env.example .env.local
   ```

4. **Update API URL if needed**

   ```
   VITE_API_URL=http://localhost:8000
   ```

5. **Start development server**

   ```bash
   npm run dev
   ```

   The frontend will be available at: http://localhost:5173

## 🐳 Docker Setup

### Build and Run with Docker Compose

1. **Navigate to project root**

   ```bash
   cd inventory-management-system
   ```

2. **Build and start all services**

   ```bash
   docker-compose up --build
   ```

3. **Access the application**
   - Frontend: http://localhost:5173
   - Backend API: http://localhost:8000
   - API Documentation: http://localhost:8000/docs
   - Database: localhost:5432

4. **Stop services**
   ```bash
   docker-compose down
   ```

### Docker Compose Services

The docker-compose.yml defines three services:

- **db**: PostgreSQL 16 database
  - Container name: inventory_db
  - Port: 5432
  - User: inventory_user
  - Password: inventory_password
  - Database: inventory_db

- **backend**: FastAPI application
  - Container name: inventory_backend
  - Port: 8000
  - Depends on: PostgreSQL database

- **frontend**: React application
  - Container name: inventory_frontend
  - Port: 5173
  - Depends on: Backend API

### Useful Docker Commands

```bash
# View logs
docker-compose logs -f backend
docker-compose logs -f frontend
docker-compose logs -f db

# Run commands in container
docker-compose exec backend python -m app.database create_tables
docker-compose exec frontend npm run build

# Remove volumes (database data)
docker-compose down -v

# Rebuild specific service
docker-compose build --no-cache backend
```

## 📚 API Documentation

### Base URL

- Local: `http://localhost:8000`
- Production: `https://your-api-domain.com`

### Authentication

Currently, the API is open (no authentication required). For production, implement:

- JWT Bearer tokens
- API keys
- OAuth 2.0

### Endpoints Overview

#### Products

| Method | Endpoint         | Description        |
| ------ | ---------------- | ------------------ |
| GET    | `/products`      | Get all products   |
| POST   | `/products`      | Create new product |
| GET    | `/products/{id}` | Get product by ID  |
| PUT    | `/products/{id}` | Update product     |
| DELETE | `/products/{id}` | Delete product     |

#### Customers

| Method | Endpoint          | Description         |
| ------ | ----------------- | ------------------- |
| GET    | `/customers`      | Get all customers   |
| POST   | `/customers`      | Create new customer |
| GET    | `/customers/{id}` | Get customer by ID  |
| PUT    | `/customers/{id}` | Update customer     |
| DELETE | `/customers/{id}` | Delete customer     |

#### Orders

| Method | Endpoint                  | Description              |
| ------ | ------------------------- | ------------------------ |
| GET    | `/orders`                 | Get all orders           |
| POST   | `/orders`                 | Create new order         |
| GET    | `/orders/{id}`            | Get order details        |
| GET    | `/orders/stats/dashboard` | Get dashboard statistics |

### API Examples

#### Create Product

```bash
curl -X POST http://localhost:8000/products \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Laptop",
    "sku": "SKU-001",
    "price": 999.99,
    "stock_quantity": 10
  }'
```

#### Create Customer

```bash
curl -X POST http://localhost:8000/customers \
  -H "Content-Type: application/json" \
  -d '{
    "name": "John Doe",
    "email": "john@example.com",
    "phone": "+1-555-0000"
  }'
```

#### Create Order

```bash
curl -X POST http://localhost:8000/orders \
  -H "Content-Type: application/json" \
  -d '{
    "customer_id": 1,
    "items": [
      {
        "product_id": 1,
        "quantity": 2
      }
    ]
  }'
```

#### Get Dashboard Statistics

```bash
curl http://localhost:8000/orders/stats/dashboard
```

## 🗄️ Database Schema

### Products Table

```sql
CREATE TABLE products (
  id SERIAL PRIMARY KEY,
  name VARCHAR(255) NOT NULL,
  sku VARCHAR(100) UNIQUE NOT NULL,
  price FLOAT NOT NULL,
  stock_quantity INTEGER NOT NULL DEFAULT 0,
  created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);
```

### Customers Table

```sql
CREATE TABLE customers (
  id SERIAL PRIMARY KEY,
  name VARCHAR(255) NOT NULL,
  email VARCHAR(255) UNIQUE NOT NULL,
  phone VARCHAR(20) NOT NULL,
  created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);
```

### Orders Table

```sql
CREATE TABLE orders (
  id SERIAL PRIMARY KEY,
  customer_id INTEGER NOT NULL REFERENCES customers(id),
  total_amount FLOAT NOT NULL DEFAULT 0.0,
  created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);
```

### Order Items Table

```sql
CREATE TABLE order_items (
  id SERIAL PRIMARY KEY,
  order_id INTEGER NOT NULL REFERENCES orders(id),
  product_id INTEGER NOT NULL REFERENCES products(id),
  quantity INTEGER NOT NULL,
  price FLOAT NOT NULL
);
```

## ✅ Business Rules & Validation

### Product Rules

- **SKU Uniqueness**: Each product must have a unique SKU
- **Price Validation**: Price must be greater than 0
- **Stock Validation**: Stock quantity cannot be negative

### Customer Rules

- **Email Uniqueness**: Each customer must have a unique email
- **Email Format**: Email must be valid format
- **Phone Required**: Phone number is mandatory

### Order Rules

- **Customer Validation**: Customer must exist before creating order
- **Product Validation**: All products must exist
- **Stock Validation**: Available stock must be sufficient for order quantity
- **Automatic Stock Reduction**: Stock is reduced immediately upon order creation
- **Total Calculation**: Order total is calculated automatically (quantity × price)
- **Error Handling**: Clear error messages for validation failures

## 🎨 Frontend Features

### Pages

#### Dashboard

- Real-time statistics cards
- Total products, customers, and orders count
- Total revenue display
- Quick actions section
- System features overview

#### Products Management

- View all products in table format
- Add new products with form validation
- Edit existing products
- Delete products
- Stock level indicators (color-coded)
- Sort and filter capabilities

#### Customers Management

- View all customers
- Add new customers with validation
- Edit customer information
- Delete customers
- Email and phone validation

#### Orders Management

- Create orders with customer and product selection
- Multiple items per order
- Quantity input with validation
- Stock availability checking
- Order history display
- Order details with total amount

### Responsive Design

- Mobile-first approach
- Breakpoints: 640px, 768px, 1024px, 1280px
- Flexible grid layouts
- Touch-friendly buttons and inputs

## 🌐 Deployment Guide

### Frontend Deployment on Vercel

1. **Push code to GitHub**

   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git push -u origin main
   ```

2. **Connect to Vercel**
   - Visit [vercel.com](https://vercel.com)
   - Click "New Project"
   - Import your GitHub repository
   - Select the `frontend` directory

3. **Environment Variables**
   - Add environment variable: `VITE_API_URL=https://your-api-domain.com`

4. **Deploy**
   - Vercel automatically deploys on push

### Backend Deployment on Render

1. **Create Render Account**
   - Visit [render.com](https://render.com)
   - Sign up and create a new account

2. **Create PostgreSQL Database**
   - Create a new PostgreSQL instance
   - Save the connection string

3. **Deploy Backend**
   - Create New → Web Service
   - Connect GitHub repository
   - Configure settings:
     - **Environment**: Python 3.11
     - **Build Command**: `pip install -r requirements.txt`
     - **Start Command**: `uvicorn app.main:app --host 0.0.0.0 --port 8000`
   - Add environment variables:
     - `DATABASE_URL`: Your PostgreSQL connection string
     - `ENVIRONMENT`: production
     - `SECRET_KEY`: Generate a secure key

4. **Deploy**
   - Click Deploy

### Database on Neon PostgreSQL

1. **Create Account**
   - Visit [neon.tech](https://neon.tech)
   - Sign up for free account

2. **Create Project**
   - Create new project
   - Choose region close to your deployment

3. **Get Connection String**
   - Copy connection string
   - Use in your backend `DATABASE_URL`

4. **Connection String Format**
   ```
   postgresql://user:password@host/database?sslmode=require
   ```

## 🔧 Troubleshooting

### Database Connection Issues

**Error: Connection refused**

```bash
# Check if PostgreSQL is running
docker-compose ps

# View database logs
docker-compose logs db

# Restart database
docker-compose restart db
```

### Backend Not Starting

**Error: ModuleNotFoundError**

```bash
# Reinstall dependencies
pip install -r requirements.txt

# Check Python version
python --version  # Should be 3.11+
```

### Frontend Not Connecting to API

**Error: CORS issues or API 404**

```bash
# Check API URL in .env.local
cat .env.local

# Verify backend is running
curl http://localhost:8000/health

# Check network in browser dev tools (F12)
```

### Docker Issues

**Error: Port already in use**

```bash
# Change port in docker-compose.yml
# Or kill the process using the port

# Windows
netstat -ano | findstr :8000
taskkill /PID <PID> /F

# macOS/Linux
lsof -i :8000
kill -9 <PID>
```

**Error: Permission denied**

```bash
# On Linux, add user to docker group
sudo usermod -aG docker $USER
newgrp docker
```

### Performance Optimization

1. **Database Indexing**
   - SKU is indexed for fast lookups
   - Customer ID and Product ID are indexed in orders

2. **Connection Pooling**
   - Backend uses SQLAlchemy connection pooling
   - 10 connections in pool, max 20 overflow

3. **Caching**
   - Consider adding Redis for caching statistics
   - Cache frequently accessed products list

## 📝 Environment Variables

### Backend (.env)

```
DATABASE_URL=postgresql://user:password@localhost:5432/inventory_db
ENVIRONMENT=development
SECRET_KEY=your-secret-key-change-in-production
FRONTEND_URL=http://localhost:5173
DEBUG=True
```

### Frontend (.env.local)

```
VITE_API_URL=http://localhost:8000
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🆘 Support

For issues, questions, or suggestions:

1. Check the Troubleshooting section above
2. Review API documentation at `/docs`
3. Check Docker logs for errors
4. Open an issue on GitHub

## 🎯 Future Enhancements

- [ ] User authentication and authorization
- [ ] Advanced search and filtering
- [ ] Inventory reports and analytics
- [ ] Export to CSV/PDF
- [ ] Email notifications
- [ ] Payment integration
- [ ] Multi-warehouse support
- [ ] API rate limiting
- [ ] Audit logging
- [ ] Real-time updates with WebSockets

---

**Last Updated**: June 2026
**Version**: 1.0.0
**Status**: Production Ready ✅
