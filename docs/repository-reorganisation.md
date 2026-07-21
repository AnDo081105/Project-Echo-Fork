# Repository Reorganisation Notes

Source of truth: `Project_Echo_Repository_Ownership.md`.

This repository currently keeps `src/production` as the production runtime boundary. File moves should be handled through reviewed pull requests after imports, Docker paths, compose mounts, CI paths and documentation links are checked.

## Current Decisions

| Area | Owner | Status | Action |
| --- | --- | --- | --- |
| `src/production` | Backend with Engine, HMI, IoT | Production runtime | Keep as the authoritative local Docker Compose boundary. |
| `src/production/docker-compose.yml` | Backend | Authoritative local runtime | Use this file for local EchoNet startup. |
| `src/production/docker-compose.test.yml` | Backend / Engine | Test runtime | Keep for CI/local test review. |
| `src/production/API` | Backend | Canonical Backend API | Treat duplicate APIs as prototype or deployment variants until merged. |
| `src/production/Engine/echo_engine_iot.py` | Engine | Main Engine runtime | Keep as production runtime while `echo_engine.py` remains legacy. |
| `src/prototypes/engine/torch_impl` | Engine with IoT | Production-adjacent prototype | Preserve. It is used by the local compose engine build and contains PyTorch, ONNX, TFLite and model-serving work. |
| `src/data_tools/store` | Engine | Offline data tooling | Moved from `src/production/Store` after `rg` found no non-generated references to the old path. |
| `src/data_tools/repository_inventory` | Engine / Backend | Local utility | Moved root file/database inventory helper out of the repository root. |
| `src/data_tools/movement_analysis` | Engine | Standalone movement/data analysis tooling | Moved root-level production scripts that are not imported by runtime services. |
| `src/prototypes/engine/notebooks` | Engine | Prototype notebooks | Holds Engine notebooks moved out of `src/production/Engine`; production Engine runtime files remain in place. |
| `src/prototypes/api/standalone_api_stub` | Backend with Engine support | Prototype API/model demo | Moved root `app/`, `Dockerfile` and `test_request.py`; canonical production API remains `src/production/API`. |
| `src/prototypes/hmi/submission_overview` | HMI | Prototype UI assets | Moved root submission overview files under HMI prototype ownership. |
| `src/echo_components_on_k8s` | Backend / HMI / Engine | Deployment variant | Keep K8s configs; merge duplicated API/HMI source in a reviewed follow-up. |
| `mlruns`, `node_modules`, `.ipynb_checkpoints`, `__MACOSX` | Engine / HMI | Generated output | Keep out of normal Git. |

## Follow-up Moves Requiring Review

- Review notebook-internal paths under `src/prototypes/engine/notebooks` before running old experiments.
- Review notebook-internal paths under `src/data_tools/store` before running old data preparation workflows.
- Group `src/prototypes/engine` by technical topic: PyTorch, augmentation, event detection, benchmarking, weather/noise, ensemble/overlap and local library work.
- Group `src/prototypes/iot` by platform: Raspberry Pi, PlatformIO/ESP32, CAD/enclosure, LoRaWAN/network and HMI node connection.
- Compare `src/echo_components_on_k8s/api` and `frontend` against production API/HMI before removing duplicate source.
- Export any useful MLflow records before removing generated `mlruns` history from version control.

## Configuration Policy

Runtime service endpoints, MQTT brokers, MongoDB hosts, model server URLs, GCP project names and local data/cache paths must be configurable through environment variables. JSON config files may remain as local defaults, but deployment should override them through compose, Kubernetes or CI secrets.
