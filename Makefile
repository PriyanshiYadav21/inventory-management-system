.PHONY: help setup clean build up down logs

help:
	@echo "Inventory Management System - Makefile Commands"
	@echo "================================================="
	@echo "make setup          - Complete setup for development"
	@echo "make build          - Build Docker images"
	@echo "make up             - Start Docker services"
	@echo "make down           - Stop Docker services"
	@echo "make logs           - View Docker logs"
	@echo "make clean          - Remove Docker containers and volumes"
	@echo "make backend-shell  - Access backend container shell"
	@echo "make frontend-shell - Access frontend container shell"
	@echo "make db-shell       - Access database container shell"
	@echo "make test-api       - Test API health"

setup:
	@echo "Setting up development environment..."
	@docker-compose up --build -d
	@echo "✅ Setup complete!"
	@echo "Frontend: http://localhost:5173"
	@echo "Backend: http://localhost:8000"
	@echo "Docs: http://localhost:8000/docs"

build:
	@echo "Building Docker images..."
	@docker-compose build

up:
	@echo "Starting services..."
	@docker-compose up -d
	@echo "✅ Services started!"

down:
	@echo "Stopping services..."
	@docker-compose down

logs:
	@docker-compose logs -f

clean:
	@echo "Cleaning up..."
	@docker-compose down -v
	@echo "✅ Cleanup complete!"

backend-shell:
	@docker-compose exec backend bash

frontend-shell:
	@docker-compose exec frontend sh

db-shell:
	@docker-compose exec db psql -U inventory_user -d inventory_db

test-api:
	@echo "Testing API health..."
	@curl -s http://localhost:8000/health | python -m json.tool

install-frontend:
	@cd frontend && npm install

install-backend:
	@cd backend && pip install -r requirements.txt

run-backend:
	@cd backend && python -m uvicorn app.main:app --reload

run-frontend:
	@cd frontend && npm run dev

run-local:
	@echo "Starting local development..."
	@echo "Make sure PostgreSQL is running!"
	@echo "Terminal 1: make run-backend"
	@echo "Terminal 2: make run-frontend"

format-backend:
	@cd backend && python -m autopep8 --in-place --aggressive -r app/

lint-frontend:
	@cd frontend && npm run lint 2>/dev/null || echo "Linting not configured"

version:
	@echo "Inventory Management System v1.0.0"
