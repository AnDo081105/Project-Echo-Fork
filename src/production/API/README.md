# Project Echo API

Owner: Backend
Status: active production runtime
Runtime boundary: `src/production/API`

This folder is the canonical Backend FastAPI service for EchoNet. It owns API entry
point wiring, middleware, route registration, database access, user/auth routes,
admin routes, detection routes, HMI/Engine/IoT integration routes and OpenAPI
export support.

## Important Paths

- `app/main.py` - FastAPI application, middleware and router registration.
- `app/database.py` - MongoDB clients and collection handles.
- `app/routers/` - API endpoints grouped by feature area.
- `app/middleware/` - JWT and request guard middleware.
- `app/services/` - Backend service logic for budgets, projects, model adapter and service state.
- `app/utils/` - utility integrations such as SMS.
- `backend/` - Kubernetes/OpenAPI export support files.
- `tests/` - API test area.

## Runtime Configuration

The API runs in EchoNet from `src/production/docker-compose.yml` and listens on
port `9000` inside the container. Local API docs are available at
`http://localhost:9000/docs` after the compose stack is running.

Backend configuration should come from environment variables where possible:

- `MONGODB_URI` - primary EchoNet database connection string.
- `USER_MONGODB_URI` - user database connection string.
- `MONGO_URI` and `MONGO_DB` - insights router connection and database name.
- `MAIL_STARTTLS` and `MAIL_SSL_TLS` - mail transport flags.
- `TWILIO_ACCOUNT_SID`, `TWILIO_AUTH_TOKEN`, `TWILIO_PHONE_NUMBER` - SMS settings.
- `API_BASE_URL` - internal API base URL for API self-calls.
- `API_CORS_ORIGINS` - comma-separated allowed browser origins.
- `MQTT_BROKER_URL`, `MQTT_BROKER_PORT` - MQTT broker host and port.

Current code still has some hard-coded service fallbacks for local Docker. See
`docs/backend-deployment-infrastructure-audit.md` before changing deployment
names, ports or credentials.

## Duplicate API Paths

Treat this folder as the source of truth for Backend API work. Review these paths
before moving or deleting anything:

- `src/Echo_Components_on_K8s/api` - Kubernetes deployment fork of the API.
- `src/prototypes/api/api` - earlier FastAPI prototype moved from `src/prototypes/api/FastAPI`.
- `src/prototypes/api/standalone_api_stub` - standalone API/model
  demonstration moved out of the repository root; not part of the current Docker
  Compose runtime.

## Local Commands

From `src/production`:

```sh
docker compose up --build
```

From `src/production/API`, for direct local API work:

```sh
pip install -r requirements.txt
python -m uvicorn app.main:app --reload --port 9000
```
