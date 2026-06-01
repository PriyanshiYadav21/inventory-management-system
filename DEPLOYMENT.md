# Deployment Configuration Files

This directory should contain deployment configurations for different platforms.

## Vercel (Frontend)

For frontend deployment on Vercel, use:

- Root directory: `frontend`
- Build command: `npm run build`
- Output directory: `dist`
- Install command: `npm install`

Environment variables:

```
VITE_API_URL=https://your-api-domain.com
```

## Render (Backend)

For backend deployment on Render, use:

- Root directory: `backend`
- Build command: `pip install -r requirements.txt`
- Start command: `uvicorn app.main:app --host 0.0.0.0 --port 8000`

Environment variables:

```
DATABASE_URL=postgresql://...
ENVIRONMENT=production
SECRET_KEY=<generate-secure-key>
FRONTEND_URL=https://your-frontend-domain.com
```

## Neon PostgreSQL (Database)

- Create a PostgreSQL instance on Neon
- Use the connection string in `DATABASE_URL`
- Format: `postgresql://user:password@host/database?sslmode=require`

## AWS/DigitalOcean/Other Platforms

- Use Docker Compose for easy deployment
- Build images: `docker build -t inventory-backend ./backend`
- Push to container registry
- Deploy using Kubernetes or docker-compose on your server
