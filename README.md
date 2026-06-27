# sample_api

## Python API Service

### Build and Run

You can build and run the Python API service using Docker Compose. Navigate to the root of the project and execute the following command:

```bash
docker-compose -f infra/docker-compose.yml up --build -d
```

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
