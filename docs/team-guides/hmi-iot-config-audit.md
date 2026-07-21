# HMI and IoT Configuration Audit

## Scope

This note covers HMI and IoT configuration findings from the repository reorganisation pass. It documents hard-coded LAN/API/MQTT settings and recommends environment variables. It does not change runtime code.

## HMI findings

| File | Finding | Recommendation |
| --- | --- | --- |
| `src/production/HMI/ui/server.js` | `API_BASE_URL` uses `API_HOST` but hard-codes port `9001`. | Add `API_PORT` or `API_BASE_URL` so compose, Kubernetes, and live URLs do not diverge. |
| `src/production/HMI/ui/server.js` | Stripe success/cancel URLs are hard-coded to `http://localhost:9001`. | Use `CLIENT_URL` for user-facing redirects and a separate backend callback URL only if needed. |
| `src/production/HMI/ui/server.js` | Gmail SMTP user and app password are hard-coded. | Use `SMTP_SERVICE`, `SMTP_USER`, `SMTP_PASS`, and `HMI_SUPPORT_EMAIL`; rotate the exposed credential. |
| `src/production/HMI/ui/server.js` | Cookie session key is the literal string `COOKIE_SECRET`. | Use `COOKIE_SECRET` from the environment. |
| `src/production/HMI/ui/middleware/index.js` | Redis host is hard-coded to `localhost` and port `6379`. | Use `REDIS_HOST` and `REDIS_PORT`; default to compose service names in containers. |
| `src/production/HMI/ui/public/admin/admin-nodes.html` | Fetches `http://localhost:9000/iot/nodes` directly. | Use relative `/iot/nodes` through the Express proxy or `IOT_API_BASE_URL`. |
| `src/production/HMI/ui/public/admin/admin-nodes-temp.html` | Fetches `http://localhost:9000/iot/nodes` directly. | Same as above; consider archiving temp page if superseded. |
| `src/prototypes/hmi/ui/config/db.config.js` | MongoDB username/password/host are hard-coded. | Keep prototype-only or replace with `MONGO_URI`/`MONGO_*` variables before reuse. |
| `src/prototypes/hmi/ui/server.js` | SMTP credential and port `7080` are hard-coded. | Keep prototype-only or parameterise as `HMI_PORT`, `SMTP_USER`, and `SMTP_PASS`. |

## IoT findings

| File | Finding | Recommendation |
| --- | --- | --- |
| `src/production/IoT/management_application/client_pi.py` | Upload endpoint is fixed to `http://192.168.1.122:5000/upload`. | Use `IOT_MANAGEMENT_UPLOAD_URL`; do not promote container until Backend confirms the endpoint. |
| `src/production/IoT/management_application/client_pi.py` | Model path, class path, save directory, audio device index, sample rate, duration, and GPS port are code constants. | Use env vars or a device config file for field devices. |
| `src/production/IoT/edge_inference/iot_edge_client.py` | Defaults publish to public `broker.hivemq.com`, topic `iot/data/test`, and sample GPS coordinates. | Require explicit production MQTT and device variables for deployments. |
| `src/production/IoT/2025_T3_prototype/*.py` | Legacy prototype uses public HiveMQ broker. | Keep as prototype-only or replace with MQTT env vars. |
| `src/production/IoT/2026_T1_new_onboarding/*.py` | Onboarding scripts use public/cloud HiveMQ broker strings and loopback IP defaults. | Use onboarding-specific MQTT env vars and a generated device IP/reporting contract. |
| `src/production/IoT/previous_implementation/config/devices.json` | Contains fixed LAN device IPs. | Treat as local sample data until device registry/provisioning owns these values. |
| `src/prototypes/iot/component_testing/*.py` | MQTT test scripts connect to `broker.hivemq.com`. | Keep as test scripts; use `IOT_MQTT_BROKER` when reused. |
| `src/prototypes/iot/New Sensor Testing/client.py` | Sensor payload prototype uses public HiveMQ broker. | Same MQTT env-var recommendation. |
| `src/prototypes/iot/hmi_node_connection/src/esp32-http-server.ino` | ESP32 firmware points to LAN host `192.168.1.9` and API port `9000`. | Move host, port, and node ID to PlatformIO build flags or a device provisioning file. |

## Recommended shared variables

| Variable | Owner | Purpose |
| --- | --- | --- |
| `API_BASE_URL` | Backend/HMI | Canonical HMI-to-backend base URL, including scheme and port. |
| `CLIENT_URL` | HMI/Deployment | Public HMI URL for redirects and generated emails. |
| `REDIS_HOST`, `REDIS_PORT` | HMI/Backend | Redis session service location. |
| `MONGO_URI` | HMI/Backend | Canonical MongoDB connection URI. |
| `SMTP_SERVICE`, `SMTP_USER`, `SMTP_PASS`, `HMI_SUPPORT_EMAIL` | HMI | Outbound HMI email configuration. |
| `COOKIE_SECRET`, `JWT_SECRET` | HMI/Backend | Session and token secrets. |
| `IOT_MQTT_BROKER`, `IOT_MQTT_PORT`, `IOT_MQTT_USERNAME`, `IOT_MQTT_PASSWORD`, `IOT_MQTT_TOPIC` | IoT/Backend/Engine | Device MQTT publishing and onboarding. |
| `IOT_DEVICE_ID` | IoT/Backend/HMI | Stable node identifier shown in HMI and API payloads. |
| `IOT_MANAGEMENT_UPLOAD_URL` | IoT/Backend | Upload endpoint for management app payloads if HTTP upload is retained. |
| `IOT_MODEL_PATH`, `IOT_CLASS_PATH` | IoT/Engine | Edge model artifact locations. |
| `IOT_AUDIO_DEVICE_INDEX`, `IOT_SAMPLE_RATE`, `IOT_RECORD_SECONDS`, `IOT_GPS_PORT` | IoT | Device-specific field hardware settings. |

## Open risks

- The HMI repo contains duplicated design/source assets and runtime copies. Moving assets without reference checks could break static pages.
- Prototype HMI and production HMI both contain exposed SMTP credentials; rotate secrets before using either outside a local sandbox.
- Public MQTT brokers are useful for demos but unsafe for production data or device control.
- IoT HTTP upload and MQTT payload contracts need one canonical Backend/Engine agreement before management and edge clients are merged.
