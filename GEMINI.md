# sample_api Development & Agent Rules

This file is automatically loaded by Antigravity CLI (`agy`) as workspace rules for the `sample_api` project.

## 1. Project Overview

`sample_api` is a multi-service project orchestrated with Docker Compose:

- **`python-api`** (Port `8000`): Python API service (`services/python-api/`).
- **`node-api`** (Port `8001`): Node.js API service (`services/node-api/`).
- **`todo-api`** (Port `8002`): FastAPI + SQLite backend for Android TODO app (`services/todo-api/`). Features JWT authentication, CRUD operations, and persistent SQLite database in `services/todo-api/data/todo.db`.
- **`infra/docker-compose.yml`**: Docker Compose configuration.

---

## 2. Environment & Prerequisites

- **Docker Desktop** on Windows with **WSL 2 integration enabled** for Ubuntu.
- Use Docker Compose v2 (`docker compose`).

---

## 3. Standard Commands

Always run these commands from the project root (`/home/yonom/sample_api`):

### Start / Rebuild Services
```bash
docker compose -f infra/docker-compose.yml up --build -d
```

### Stop Services
```bash
docker compose -f infra/docker-compose.yml down
```

### Check Logs
```bash
docker compose -f infra/docker-compose.yml logs -f
# Or for a specific service:
docker compose -f infra/docker-compose.yml logs python-api
docker compose -f infra/docker-compose.yml logs node-api
docker compose -f infra/docker-compose.yml logs todo-api
```

---

## 4. Verification & Testing

After modifying code or starting services, verify functionality using `curl`:

- **Python API**:
  - Root: `curl -s http://localhost:8000/` (Expect: `{"message":"Hello Docker API"}`)
  - Health: `curl -s http://localhost:8000/health` (Expect: `{"status":"ok"}`)
- **Node.js API**:
  - Root: `curl -s http://localhost:8001/` (Expect: `{"message":"Hello Docker API"}`)
  - Health: `curl -s http://localhost:8001/health` (Expect: `{"status":"ok"}`)
- **Todo API**:
  - Root: `curl -s http://localhost:8002/`
  - Health: `curl -s http://localhost:8002/health` (Expect: `{"status":"ok","service":"todo-api"}`)
  - Docs: `curl -s -o /dev/null -w "%{http_code}\n" http://localhost:8002/docs` (Expect: `200`)

---

## 5. Agent Guidelines

- **Self-Verification**: After editing service code or Dockerfile, rebuild and restart the containers with `docker compose -f infra/docker-compose.yml up --build -d` and run `curl` checks to ensure the API behaves as expected before finishing the task.
- **Data Persistence**: `todo-api` uses SQLite mounted at `services/todo-api/data/todo.db`. Do not commit `.db` files to git.
- **Minimal Diffs**: Keep changes focused on the requested tasks. Do not delete existing comments or documentation unless explicitly requested.
