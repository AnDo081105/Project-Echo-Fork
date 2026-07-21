# Backend Deployment and Infrastructure Audit

Date: 2026-07-21
Scope: Backend-owned API, MongoDB, MQTT, Docker Compose, CI, Kubernetes variant,
backend prototypes, environments and load tests.

Source of truth:
`../../Project_Echo_Repository_Ownership.md` from this file, in the parent
workspace folder.

## Ownership Baseline

- Canonical local runtime: `src/production/docker-compose.yml`.
- CI/local test runtime: `src/production/docker-compose.test.yml`.
- Canonical Backend API: `src/production/API`.
- Backend infrastructure: `src/production/MongoDB`, `src/production/MQTT-Server`,
  Compose files, `.github/workflows`, `src/deployment/kubernetes`,
  `src/Echo_Components_on_K8s/api`, `src/Echo_Components_on_K8s/MongoDb`,
  `src/Environments`, `src/loadtest`, `src/prototypes/api`.
- Deployment variant: `src/Echo_Components_on_K8s`; keep as deployment config
  while duplicate source is reviewed.

## Dependency Notes Checked Before Edits

- `.github/workflows/docker-image.yml` builds and starts
  `src/production/docker-compose.test.yml` and expects nine running containers.
- `src/production/docker-compose.yml` currently builds the Engine from
  `../prototypes/engine/torch_impl`, so the Backend compose file depends on an
  Engine-owned prototype path.
- `src/production/docker-compose.test.yml` builds the Engine from
  `./Engine/Engine.test.Dockerfile`, so runtime and test compose variants do not
  use the same Engine build context.
- API, MongoDB and MQTT runtime docs were updated only; production files were not
  moved or deleted.

## Hard-Coded Service Configuration To Externalise

These line references came from `rg -n` on 2026-07-21.

| File | Lines | Finding | Recommended env/config |
| --- | ---: | --- | --- |
| `src/production/API/app/main.py` | 27 | CORS origin fixed to `http://localhost:8080` before a second permissive CORS middleware block. | Replace duplicate CORS setup with `API_CORS_ORIGINS`. |
| `src/production/API/app/main.py` | 55 | CORS origin allows `*`. | Restrict with `API_CORS_ORIGINS` per environment. |
| `src/production/API/app/database.py` | 12 | `MONGODB_URI` exists, but fallback includes database username, password, host and port. | Move fallback to `.env.example` and fail clearly when missing outside local dev. |
| `src/production/API/app/database.py` | 41 | `USER_MONGODB_URI` exists, but fallback includes root credentials and host. | Move fallback to `.env.example` and fail clearly when missing outside local dev. |
| `src/production/API/app/echo_config.json` | 5 | Database hostname is hard-coded as `ts-mongodb-cont`. | Use `MONGODB_URI` or `DB_HOST`. |
| `src/production/API/app/routers/hmi.py` | 37-39 | MQTT broker host, topic and port are module constants. | Use `MQTT_BROKER_URL`, `MQTT_ENGINE_TOPIC`, `MQTT_BROKER_PORT`. |
| `src/production/API/app/routers/hmi.py` | 44-46 | BOM FTP host and directories are hard-coded. | Use `WEATHER_FTP_SERVER`, `WEATHER_FTP_DIRECTORY`, `WEATHER_STATION_LIST_DIRECTORY`. |
| `src/production/API/app/routers/hmi.py` | 55 | Weather cache path is fixed to `/app/weather_data`. | Use `WEATHER_DATA_DIR`. |
| `src/production/API/app/routers/weather_data.py` | 104-105 | BOM FTP host and directory are also hard-coded in the helper module. | Use shared weather FTP environment variables. |
| `src/production/API/app/routers/hmi.py` | 357 | 2FA generation self-call uses `http://localhost:9000/2fa/generate`. | Use `API_BASE_URL`. |
| `src/production/API/app/routers/hmi.py` | 669 | Engine algorithm self-call uses `http://ts-api-cont:9000/engine/algorithms_data`. | Use `API_BASE_URL` or internal FastAPI call. |
| `src/production/docker-compose.yml` | 37, 41-42, 86, 121, 123, 128, 137, 140, 156-160 | Compose still includes service defaults, credentials, fixed ports and command ports. | Continue parameterizing with Compose variables and move secrets into `.env`/secret stores. |
| `src/production/docker-compose.test.yml` | 73, 110, 119, 122, 138-142 | Test compose still includes fixed ports and MongoDB credentials. | Keep if CI-only, otherwise document or parameterize. |
| `src/production/MongoDB/docker-compose.yml` | 8-12 | Standalone MongoDB compose includes root credentials and fixed host port. | Use env variables and `MONGO_PORT` if running alongside another local MongoDB. |
| `src/production/MongoDB/test_connection.py` | 6 | Smoke test uses localhost and committed credentials. | Read `MONGODB_URI` from environment. |
| `src/loadtest/k6_echo_test.js` | 17 | `BASE_URL` defaults to `http://localhost:9000`. | Acceptable local fallback; document required `BASE_URL` for CI/staging. |
| `src/Echo_Components_on_K8s/api/app/database.py` | 9, 19 | K8s API builds MongoDB URIs with committed credentials and `DB_HOST`. | Use `MONGODB_URI` and `USER_MONGODB_URI` from Secret/ConfigMap. |
| `src/Echo_Components_on_K8s/api/app/echo_config.json` | 4 | Database hostname fixed to `ts-mongodb-cont`, which does not match K8s service naming. | Remove or generate from deployment env. |
| `src/Echo_Components_on_K8s/api/app/routers/hmi.py` | 30 | K8s API HMI router still fixes MQTT port to `1883`. | Use `MQTT_BROKER_PORT`. |
| `src/Echo_Components_on_K8s/api/app/routers/insights.py` | 9-10 | Insights router defaults to `mongodb://db:27017` and database `project_echo`. | Align with `MONGO_URI`/`MONGO_DB` and canonical database name. |
| `src/deployment/kubernetes/configMaps_and_secrets/api-env.yaml` | 7-12 | Usernames, passwords and full MongoDB URIs are stored in a ConfigMap-style file. | Split non-secret config into ConfigMap and credentials into Kubernetes Secret. |
| `src/deployment/kubernetes/deployments/mongodb-deployment.yaml` | 19-22 | MongoDB root username/password are inline deployment values. | Reference Kubernetes Secret keys. |
| `src/deployment/kubernetes/configMaps_and_secrets/engine-env.yaml` | 9 | Root database password is present in environment config. | Move secret to Kubernetes Secret. |
| `src/deployment/kubernetes/configMaps_and_secrets/hmi-env.yaml` | 9 | Root database password is present in environment config. | Move secret to Kubernetes Secret. |
| `src/deployment/kubernetes/configMaps_and_secrets/mserver-env.yaml` | 10 | Root database password is present in environment config. | Move secret to Kubernetes Secret. |
| `src/prototypes/api/api/app.py` | 20 | Prototype CORS origin fixed to `http://localhost:8080`. | Use prototype `.env` if retained. |
| `src/prototypes/api/api/auth_proto.py` | 172 | Prototype Uvicorn host fixed to `127.0.0.1`. | Use CLI/env if retained. |
| `src/prototypes/api/mqtt/publisher.py` | 16 | Prototype publishes to public broker `broker.mqttdashboard.com:1883`. | Use `MQTT_BROKER_URL` and `MQTT_BROKER_PORT`; avoid public broker in tests. |
| `src/prototypes/api/mqtt/subscriber.py` | 36 | Prototype subscribes to public broker `broker.mqttdashboard.com:1883`. | Use `MQTT_BROKER_URL` and `MQTT_BROKER_PORT`; avoid public broker in tests. |
| `src/prototypes/api/mqtt/test.py` | 13 | Prototype test connects to public broker `broker.mqttdashboard.com:1883`. | Use `MQTT_BROKER_URL` and `MQTT_BROKER_PORT`; mark network test explicitly. |

## Gitignore Recommendations Applied

- Added global ignores for `node_modules`, `__MACOSX`, notebook checkpoints,
  MLflow output, model/checkpoint formats, generated caches, local env files,
  local uploads and IoT audio output.
- Removed the previous rule that ignored `src/production/API/app/main.py`, because
  that is a production Backend file.
- Replaced a NUL-padded/corrupted ignore block with normal text.

## Follow-Up Needed

- Confirm GitHub team handles and enable active `.github/CODEOWNERS` entries.
- Move database credentials out of Docker Compose and K8s ConfigMap files.
- Decide whether local-dev fallbacks in API code should remain or become
  environment-required for non-local deployments.
- Diff `src/Echo_Components_on_K8s/api` against `src/production/API` before any
  source merge/archive work.
