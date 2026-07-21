# IoT Management Application

## Owner

IoT team, with Backend review needed for upload/API contracts and deployment.

## Status

Review required before production use.

This folder contains a Raspberry Pi client, Dockerfile, Kubernetes deployment stub, and Python requirements. The client records audio, runs a local TFLite model, collects basic health data, and posts a JSON payload to an upload endpoint.

## Files

| File | Purpose |
| --- | --- |
| `client_pi.py` | Raspberry Pi client for audio recording, TFLite inference, health collection, optional GPS helper, and upload. |
| `Dockerfile` | Python 3.9 slim image with audio/scientific system dependencies. |
| `requirements.txt` | Python packages for audio, ML, HTTP, GPS, and Flask. |
| `iot-simulator-deployment.yaml` | Kubernetes deployment stub using `ts-simulator:latest`. |

## Current risks

- `SERVER_URL` is hard-coded to `http://192.168.1.122:5000/upload`, so the container only targets one LAN machine.
- `MODEL_PATH`, `CLASS_PATH`, `SAVE_DIR`, sample rate, audio duration, audio device index, and GPS serial defaults are code constants.
- The upload payload contract is local to this script and is not clearly tied to the canonical Backend API.
- The deployment image name is a local development image and has no registry target.
- The script records continuously in an infinite loop and stores local WAV files; field retention and cleanup rules should be confirmed.

## Recommended environment contract

Use environment variables or a device config file before promoting this app:

| Variable | Suggested default | Purpose |
| --- | --- | --- |
| `IOT_MANAGEMENT_UPLOAD_URL` | unset | Backend upload endpoint for health, location, species, and confidence payloads. |
| `IOT_MODEL_PATH` | `models/checkpoint_MobileNetV3-Large.tflite` | Local TFLite model path. |
| `IOT_CLASS_PATH` | `models/class_names_MobileNetV3-Large.json` | Class mapping JSON path. |
| `IOT_AUDIO_SAVE_DIR` | `audioLocal` | Local retained audio directory. |
| `IOT_AUDIO_DEVICE_INDEX` | unset | Device-specific microphone index. |
| `IOT_SAMPLE_RATE` | `16000` | Model input sample rate. |
| `IOT_RECORD_SECONDS` | `5` | Recording duration per inference loop. |
| `IOT_GPS_PORT` | `/dev/ttyACM0` | GPS serial device path. |

## Next review steps

- Confirm whether this app should become part of the local compose/Kubernetes runtime or remain an archived Raspberry Pi prototype.
- Replace the LAN upload URL with configuration after Backend confirms the endpoint.
- Decide whether MQTT publishing should replace direct HTTP upload for consistency with `edge_inference/`.
- Document model artifact storage outside normal Git before adding real `.tflite` files.
