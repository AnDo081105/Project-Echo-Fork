# Production Target

Owner: Backend, Engine, HMI and IoT by service area
Status: Target landing area; current production runtime remains `src/Components`

`src/production` is the proposed long-term home for production source after each team confirms imports, Docker paths, compose mounts, CI paths and runtime dependencies. Do not move active runtime services here until the compatibility checks are complete.

## Current Compatibility Boundary

- Local runtime startup still uses `src/Components/docker-compose.yml`.
- Backend API production source remains `src/Components/API`.
- Engine runtime remains `src/Components/Engine`, with `echo_engine_iot.py` as the main entry point.
- HMI runtime remains `src/Components/HMI/ui`, with `server.js` as the main entry point.
- IoT field inference remains `src/Components/IoT/edge_inference`.
- MongoDB, MQTT, Simulator and Store remain documented under `src/Components` until their dependencies are reviewed.

## Target Areas

| Target | Owner | Planned source |
| --- | --- | --- |
| `backend/` | Backend | `src/Components/API`, database and messaging service code after duplicate API review. |
| `engine/` | Engine | `src/Components/Engine` after notebook/model artifact separation. |
| `hmi/` | HMI | `src/Components/HMI/ui` after prototype and K8s frontend comparison. |
| `iot/` | IoT | `src/Components/IoT/edge_inference` and reviewed device code. |
| `simulator/` | Engine | `src/Components/Simulator` after simulator prototype comparison. |
| `infrastructure/` | Backend | MongoDB, MQTT and shared service configuration after deployment split. |

## Move Rules

- Keep generated dependencies such as `node_modules` out of this tree.
- Keep model weights, checkpoints and generated caches out of normal Git.
- Replace hard-coded URLs, MQTT brokers, LAN IPs and local paths with environment variables before promotion.
