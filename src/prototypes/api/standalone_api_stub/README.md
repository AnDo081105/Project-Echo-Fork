# Standalone API Stub

Owner: Backend with Engine support

Status: prototype, not part of the production Compose runtime

This folder contains the standalone FastAPI/model demonstration that previously
lived at repository root as `app/`, `Dockerfile` and `test_request.py`.

The canonical production Backend API remains `src/production/API`. Use this
prototype only for isolated API/model experiments.

## Run

From the repository root:

```bash
uvicorn src.prototypes.api.standalone_api_stub.app.main:app --host 0.0.0.0 --port 8000
```

Build the prototype image from the repository root so the Dockerfile can read
the shared root `requirements.txt`:

```bash
docker build -f src/prototypes/api/standalone_api_stub/Dockerfile -t project-echo-api-stub .
```
