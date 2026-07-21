# Echo Engine Component

Owner: Engine team
Status: production runtime boundary, with legacy and prototype-adjacent files still present
Runtime role: audio preprocessing, species/weather classification, MQTT message handling, API/database submission, and TensorFlow Serving client support

This folder is the canonical production Engine component under `src/production`. The current ownership review treats `echo_engine_iot.py` as the main runtime path and `echo_engine.py` as the older runtime that still needs comparison before any merge or archive decision.

The local Docker Compose files currently disagree about the Engine image source:

| Compose file | Engine build source | Meaning |
| --- | --- | --- |
| `src/production/docker-compose.yml` | `../prototypes/engine/torch_impl` with `light_engine.Dockerfile` | Current local compose path uses the important PyTorch/TFLite prototype runtime. |
| `src/production/docker-compose.test.yml` | `./Engine` with `Engine.test.Dockerfile` | Test compose still exercises this production Engine folder. |

Do not move or delete model weights, YAMNet assets, notebooks, or `torch_impl` dependencies without a separate dependency review.

## Key Files

| Path | Purpose | Status |
| --- | --- | --- |
| `echo_engine_iot.py` | Main Engine runtime with IoT MQTT support and API submission. | Keep as active runtime candidate. |
| `echo_engine.py` | Earlier Engine runtime with similar preprocessing and TF Serving calls. | Compare before merge/archive. |
| `echo_engine.json` | Runtime configuration for data/cache paths, MQTT, model servers, API, MongoDB, and IoT MQTT. | Needs environment override support. |
| `Engine.Dockerfile` | Production-style Engine image, copies `echo_engine_iot.py` as `echo_engine.py`. | Keep. |
| `Engine.test.Dockerfile` | Test Engine image used by `docker-compose.test.yml`. | Keep for CI/local validation. |
| `Model.Dockerfile` and `models.config` | TensorFlow Serving model image and model config. | Keep, but model artifacts should be externally tracked. |
| `yamnet_dir/` | YAMNet model and helper assets used by the runtime. | Keep; treat weights as model artifacts. |
| `*.ipynb` | Engine development/training notebooks. | Moved to `src/prototypes/engine/notebooks` in the Engine/data-tools reorganisation slice after reference checks. |

## Notebook Compatibility

The following experiment notebooks moved out of this production runtime folder:

- `generic_engine_pipeline.ipynb` -> `src/prototypes/engine/notebooks/generic_engine_pipeline.ipynb`
- `multilabel_engine_pipeline.ipynb` -> `src/prototypes/engine/notebooks/multilabel_engine_pipeline.ipynb`
- `optimised_engine_pipeline.ipynb` -> `src/prototypes/engine/notebooks/optimised_engine_pipeline.ipynb`
- `surf_features_engine_model.ipynb` -> `src/prototypes/engine/notebooks/surf_features_engine_model.ipynb`
- `helpers/tesing2.py.ipynb` -> `src/prototypes/engine/notebooks/helpers/tesing2.py.ipynb`

No production Engine runtime files, Dockerfiles, model folders, or helper Python modules were moved in this slice.

## Model Artifacts

Expected production TensorFlow Serving layout is still `models/echo_model/1/` and matching entries in `models.config`. The root ownership document says model weights/checkpoints must not be treated as ordinary source files. Use DVC, Git LFS, or approved external storage for `.h5`, `.pkl`, `.pt`, `.pth`, `.onnx`, `.tflite`, SavedModel directories, and generated caches.

## Configuration Audit

The following hard-coded values should be replaced with environment-based configuration after the Backend/Engine runtime variable contract is agreed:

| File:line | Finding |
| --- | --- |
| `src/production/Engine/echo_engine.json:2` | Local Windows audio path: `d:\data\b3`. |
| `src/production/Engine/echo_engine.json:3` | Local Windows cache path: `d:\pipeline_cache`. |
| `src/production/Engine/echo_engine.json:18` | Fixed Docker MQTT host: `ts-mqtt-server-cont`. |
| `src/production/Engine/echo_engine.json:20` | Fixed Engine MQTT topic: `projectecho/engine/2`. |
| `src/production/Engine/echo_engine.json:24` | Fixed TensorFlow Serving species URL: `http://ts-echo-model-cont:8501/...`. |
| `src/production/Engine/echo_engine.json:25` | Fixed TensorFlow Serving weather URL: `http://ts-echo-model-cont:8501/...`. |
| `src/production/Engine/echo_engine.json:27` | Public test IoT MQTT broker default: `broker.hivemq.com`. |
| `src/production/Engine/echo_engine_iot.py:116` | Relative YAMNet weight path: `yamnet_dir/yamnet.h5`. |
| `src/production/Engine/echo_engine_iot.py:118` | Relative local Keras model path: `yamnet_dir/model_3_82_16000.h5`. |
| `src/production/Engine/echo_engine_iot.py:124` | Relative SavedModel path: `yamnet_dir/model`. |
| `src/production/Engine/echo_engine_iot.py:851` | Code fallback for public IoT MQTT broker: `broker.hivemq.com`. |
| `src/production/Engine/echo_engine.py:108` | Legacy runtime has the same relative YAMNet weight path. |
| `src/production/Engine/echo_engine.py:110` | Legacy runtime has the same relative local Keras model path. |
| `src/production/Engine/echo_engine.py:116` | Legacy runtime has the same relative SavedModel path. |
| `src/production/Engine/test_iot_publisher.py:41` | Manual test defaults to public MQTT broker `broker.hivemq.com`. |
| `src/production/Engine/test_iot_integration.py:56-61` | Test fixture uses localhost service endpoints and public IoT broker defaults. |

## Manual Docker Notes

The older direct Docker workflow still requires a trained model under `models/echo_model/1/`.

```sh
docker volume create myvolume
docker network create --driver bridge echo-net
docker build --file Model.Dockerfile -t ts-echo-model .
docker run -p 8501:8501 --name ts-echo-model-cont --network echo-net -d ts-echo-model
docker build --file Engine.Dockerfile -t ts-echo-engine .
docker run --name ts-echo-engine-cont -it --rm -v myvolume:/root --network echo-net ts-echo-engine
```
