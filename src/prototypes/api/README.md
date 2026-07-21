# API Prototypes

Owner: Backend.

Status: prototype work, not production runtime.

This folder contains Backend-owned API, MQTT and standalone API/model prototypes.
It replaces the previous split where compatibility notes lived in
`src/prototypes/api` and the working prototypes lived in `src/prototypes/backend`.

| Folder | Previous path | Purpose |
| --- | --- | --- |
| `api/` | `src/prototypes/api/FastAPI` | Earlier FastAPI and MongoDB prototype. |
| `mqtt/` | `src/prototypes/api/mqtt` | MQTT publisher/subscriber experiments and sample event payloads. |
| `standalone_api_stub/` | repository root `app/`, `Dockerfile`, `test_request.py` | Standalone API/model demonstration outside the production Compose runtime. |

The canonical production Backend API remains `src/Components/API`. Keep prototype changes here unless they are explicitly reviewed for promotion into production.
