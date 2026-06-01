# Build stage
FROM node:20-alpine AS build

WORKDIR /app

COPY package*.json ./
RUN npm ci

COPY . .
RUN npm run build

# Production stage — lightweight static file server
FROM node:20-alpine

WORKDIR /app

# Install 'serve' globally for production-grade static file serving
RUN npm install -g serve@14

# Copy only the built output from the build stage
COPY --from=build /app/dist ./dist

# Expose port (documentation only, Railway uses $PORT)
EXPOSE ${PORT:-8000}

# Serve the built static files — Railway injects $PORT
CMD sh -c "serve -s dist -l ${PORT:-8000}"