# Torch Engine Prototype

Owner: Engine team, with IoT as a dependent stakeholder
Status: current local compose Engine image source
Runtime role: lightweight EfficientNetV2/TFLite inference for the Engine container

This folder must be preserved during the repository reorganisation. `src/Components/docker-compose.yml` currently builds the `echo_engine` service from this directory, and IoT edge inference docs point to the EfficientNetV2 trained model outputs in this tree.

## Key Files

| Path | Purpose | Status |
| --- | --- | --- |
| `light_echo_engine_efficientnetv2_tflite.py` | MQTT Engine entrypoint wired to EfficientNetV2 TFLite inference. | Preserved for the `echo_engine` container. |
| `light_echo_engine.json` | Runtime config for the lightweight Engine. | Preserved; compose environment variables override key settings. |
| `light_echo_credentials.json` | Runtime credentials placeholder/config consumed by the Engine. | Preserved for local compose compatibility. |
| `light_engine.Dockerfile` | Dockerfile used by the main local compose `echo_engine` service. | Preserved. |
| `requirements.txt` | Python package list used by the Dockerfile build. | Preserved. |
| `helpers/` | Helper package copied into the Engine image. | Preserved. |
| `Integrate_EfficientNetV2_Engine/` | EfficientNetV2 TFLite model artifacts and validation materials copied into the image. | Preserved because the runtime loads `_trained_models/`. |

## IoT Dependency

`src/Components/IoT/edge_inference/README.md` documents the field path that uses EfficientNetV2 TFLite artifacts from:

```text
src/prototypes/engine/torch_impl/Integrate_EfficientNetV2_Engine/_trained_models/
```

Keep `_trained_models/` intact until DVC, Git LFS, or approved external storage is confirmed. The expected edge artifacts are the `.tflite` model plus `class_mapping.json` and `preprocess_config.json`.

## Hard-Coded Configuration Audit

| File:line | Finding |
| --- | --- |
| `src/prototypes/engine/torch_impl/light_echo_engine.json:2` | Local Windows audio path: `d:\data\b3`. |
| `src/prototypes/engine/torch_impl/light_echo_engine.json:3` | Local Windows cache path: `d:\pipeline_cache`. |
| `src/prototypes/engine/torch_impl/light_echo_engine.json:18` | Fixed Docker MQTT host: `ts-mqtt-server-cont`. |
| `src/prototypes/engine/torch_impl/light_echo_engine.json:20` | Fixed Engine MQTT topic: `projectecho/engine/2`. |
| `src/prototypes/engine/torch_impl/light_echo_engine.json:23` | Fixed TensorFlow Serving species URL: `http://ts-echo-model-cont:8501/...`. |
| `src/prototypes/engine/torch_impl/light_echo_engine.json:24` | Fixed TensorFlow Serving weather URL: `http://ts-echo-model-cont:8501/...`. |
| `src/prototypes/engine/torch_impl/Integrate_EfficientNetV2_Engine/validate_efficientnetv2_dataset_inference.py:41` | Absolute `C:\Deakin\...` dataset path. |
| `src/prototypes/engine/torch_impl/Integrate_EfficientNetV2_Engine/validate_efficientnetv2_json_inference.py:44` | Absolute `C:\Deakin\...` sample audio path. |
| `src/prototypes/engine/torch_impl/Integrate_EfficientNetV2_Engine/validate_efficientnetv2_mqtt_message_handler.py:47` | Absolute `C:\Deakin\...` sample audio path. |
| `src/prototypes/engine/torch_impl/Integrate_EfficientNetV2_Engine/validate_efficientnetv2_tflite_inference.py:47` | Absolute `C:\Deakin\...` dataset path. |
| `src/prototypes/engine/torch_impl/Integrate_EfficientNetV2_Engine/validate_efficientnetv2_tflite_inference.py:57` | Absolute `C:\Deakin\...` sample audio path. |
| `src/prototypes/engine/torch_impl/Integrate_EfficientNetV2_Engine/efficientnetv2_dataset_validation_results.csv:2` | Generated results contain absolute `C:\Deakin\...` source data paths. |
| `src/prototypes/engine/torch_impl/error_analysis/outputs/predictions.csv:2` | Generated predictions contain absolute `/Users/jack/...` source data paths. |

## Cleanup Notes

- Non-runtime loose files were removed from this folder root so the compose build context clearly exposes the application run path.
- Keep `_trained_models/` intact until DVC, Git LFS, or approved external storage is confirmed.
