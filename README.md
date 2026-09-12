# sample_api

## Prerequisites

- Docker Desktop with WSL 2 integration enabled

## Python API Service

### Build and Run

You can build and run the Python API service using Docker Compose. Navigate to the root of the project and execute the following command:

```bash
docker compose -f infra/docker-compose.yml up --build -d
```

*(Note: `docker-compose` command is also supported as an alias.)*

This will build the Docker image for the `python-api` service and start it in detached mode.

### Verification

Once the service is running, you can verify its functionality by accessing the API endpoints.

**1. Root Endpoint:**

```bash
curl http://localhost:8000/
```

Expected output:
```json
{"message":"Hello Docker API"}
```

**2. Health Endpoint:**

```bash
curl http://localhost:8000/health
```

Expected output:
```json
{"status":"ok"}
```

## Node.js API Service

### Build and Run

You can build and run the Node.js API service using Docker Compose. Add it to the existing `docker-compose.yml` configuration and execute the following command:

```bash
docker compose -f infra/docker-compose.yml up --build -d
```

This will build the Docker image for the `node-api` service and start it in detached mode, alongside the Python API.

### Verification

Once the service is running, you can verify its functionality by accessing the API endpoints. The Node.js API runs on port 8001.

**1. Root Endpoint:**

```bash
curl http://localhost:8001/
```

Expected output:
```json
{"message":"Hello Docker API"}
```

**2. Health Endpoint:**

```bash
curl http://localhost:8001/health
```

Expected output:
```json
{"status":"ok"}
```

## Todo API Service (Android Backend)

A FastAPI-based REST API service for Android TODO applications, featuring JWT user authentication and SQLite file database persistence. Runs on port 8002.

### Build and Run

Included in the standard Docker Compose configuration:

```bash
docker compose -f infra/docker-compose.yml up --build -d
```

### Interactive API Documentation (Swagger UI)

Open in your browser:
- Swagger UI: `http://localhost:8002/docs`
- OpenAPI JSON: `http://localhost:8002/openapi.json`

### Verification

**1. Root & Health Check:**

```bash
curl http://localhost:8002/
curl http://localhost:8002/health
```

**2. User Registration & Login:**

```bash
# Register a user
curl -X POST http://localhost:8002/auth/register \
  -H "Content-Type: application/json" \
  -d '{"username": "testuser", "password": "password123"}'

# Login to get JWT token
TOKEN=$(curl -s -X POST http://localhost:8002/auth/login \
  -H "Content-Type: application/json" \
  -d '{"username": "testuser", "password": "password123"}' | grep -o '"access_token":"[^"]*' | cut -d'"' -f4)
```

**3. Manage Todos:**

```bash
# Create a Todo
curl -X POST http://localhost:8002/todos/ \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"memo": "Buy milk", "due_date": "2026-09-15T18:00:00Z"}'

# List Todos
curl -H "Authorization: Bearer $TOKEN" http://localhost:8002/todos/

# Update Todo (mark completed)
curl -X PUT http://localhost:8002/todos/1 \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"is_completed": true}'
```

---

## Teardown (Stop Services)

To stop and remove containers created by Docker Compose:

```bash
docker compose -f infra/docker-compose.yml down
```
