# Quick Start Guide

## 🚀 Fastest Way to Get Started

### Using Docker Compose (Recommended)

```bash
# Navigate to project root
cd inventory-management-system

# Start all services
docker-compose up --build

# Access the application
# Frontend: http://localhost:5173
# Backend API: http://localhost:8000
# API Docs: http://localhost:8000/docs
```

### Local Development (Without Docker)

#### Prerequisites

- Python 3.11+
- Node.js 20+
- PostgreSQL 16

#### Step 1: Backend Setup

```bash
cd backend

# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Set up database
# Update DATABASE_URL in .env with your PostgreSQL connection

# Start backend
python -m uvicorn app.main:app --reload
```

#### Step 2: Frontend Setup (New Terminal)

```bash
cd frontend

# Install dependencies
npm install

# Start development server
npm run dev
```

#### Step 3: Access the Application

- Frontend: http://localhost:5173
- Backend API: http://localhost:8000
- API Documentation: http://localhost:8000/docs

## 🔧 Using Setup Scripts

### On Windows

```bash
.\setup.bat
```

### On macOS/Linux

```bash
chmod +x setup.sh
./setup.sh
```

## 📝 First Time Setup Checklist

- [ ] Clone the repository
- [ ] Install Python 3.11+ and Node.js 20+
- [ ] Install PostgreSQL 16 (or use Docker)
- [ ] Run setup script or Docker Compose
- [ ] Create .env files with correct database URL
- [ ] Start backend and frontend servers
- [ ] Access http://localhost:5173 in browser
- [ ] Create sample data through the UI

## 🎯 Common Tasks

### Create a Product

1. Go to Products page
2. Click "+ Add Product"
3. Fill in name, SKU, price, stock
4. Click "Create Product"

### Register a Customer

1. Go to Customers page
2. Click "+ Add Customer"
3. Fill in name, email, phone
4. Click "Create Customer"

### Create an Order

1. Go to Orders page
2. Click "+ Create Order"
3. Select customer and products
4. Enter quantities
5. Click "Create Order"

### View Dashboard

- Click "Dashboard" in sidebar
- See real-time stats

## 🐛 Quick Troubleshooting

### Backend not starting

```bash
# Check Python version
python --version  # Should be 3.11+

# Reinstall dependencies
pip install -r requirements.txt

# Check database connection
python -c "from sqlalchemy import create_engine; create_engine('your_db_url')"
```

### Frontend not connecting to API

```bash
# Check .env.local
cat frontend/.env.local

# Verify VITE_API_URL points to backend
# Verify backend is running on http://localhost:8000
```

### Database connection error

```bash
# Check PostgreSQL is running
# Verify credentials in .env
# Check DATABASE_URL format
```

## 📚 Documentation

- Full README: See [README.md](../README.md)
- API Documentation: http://localhost:8000/docs
- Architecture: See project structure in README.md

## 🆘 Need Help?

1. Check the Troubleshooting section in [README.md](../README.md)
2. Review API docs at http://localhost:8000/docs
3. Check container logs: `docker-compose logs`
4. Ensure all prerequisites are installed

## ✨ Tips for Development

- Use `npm run dev` for hot reload in frontend
- Use `--reload` flag with uvicorn for auto-reload in backend
- Use browser DevTools (F12) to debug frontend
- Use FastAPI docs (/docs) to test backend endpoints
- Check container logs for errors: `docker-compose logs -f`

## 🎉 You're Ready!

Start building! The system is fully functional and ready for development.
