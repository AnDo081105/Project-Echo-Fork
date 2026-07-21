# IoT Component

Owner: IoT team
Status: Mixed production and review area inside the current `src/production` runtime boundary
Runtime role: Field-device edge inference, IoT management client, onboarding experiments, and legacy IoT device implementations.

## Source Of Truth

This folder follows the parent workspace ownership document, `Project_Echo_Repository_Ownership.md`:

- `edge_inference/iot_edge_client.py` is the primary field-device path for Raspberry Pi TFLite inference and MQTT prediction publishing.
- `management_application/client_pi.py` is included in Docker Compose as `echo_iot_management`, but its endpoint usage needs review.
- `2025_T3_prototype/`, `2026_T1_new_onboarding/`, and `previous_implementation/` are retained for reference until migration is confirmed.
- Do not move or delete IoT source until active dependencies, deployment paths, hardware docs, and team usage are checked.
- The Engine-owned TFLite conversion dependency is `src/prototypes/engine/torch_impl/Integrate_EfficientNetV2_Engine/`.

## Runtime Dependencies Checked

- `src/production/docker-compose.yml` builds `echo_iot_management` from `./IoT/management_application/Dockerfile`.
- Compose bind-mounts `./IoT/management_application` to `/app`.
- `edge_inference/` is not a compose service; it is documented as a Raspberry Pi field runtime.
- Edge inference requires local model files next to `iot_edge_client.py` under `edge_inference/models/`.
- IoT code depends on Backend API/MQTT integration and Engine payload handling.

## Hard-Coded Configuration Audit

These are the IoT-owned URL, LAN IP, and MQTT broker findings from this pass:

| File | Lines | Finding |
| --- | --- | --- |
| `src/production/IoT/management_application/client_pi.py` | 15 | Upload endpoint is hard-coded to LAN URL `http://192.168.1.122:5000/upload`; this does not clearly match EchoNet API routing. |
| `src/production/IoT/previous_implementation/client_pi.py` | 15 | Same hard-coded LAN upload endpoint as management application. |
| `src/production/IoT/previous_implementation/config/devices.json` | 4, 10 | Device records contain fixed LAN IPs `192.168.1.122` and `192.168.1.123`. |
| `src/production/IoT/edge_inference/iot_edge_client.py` | 218 | MQTT broker defaults to public broker `broker.hivemq.com`. |
| `src/production/IoT/edge_inference/README.md` | 151, 153, 175, 177, 217, 228 | Documentation examples and notes use `broker.hivemq.com` / `iot/data/test`. |
| `src/production/IoT/2025_T3_prototype/client.py` | 13 | MQTT broker hard-coded to `broker.hivemq.com`. |
| `src/production/IoT/2025_T3_prototype/server.py` | 9 | MQTT broker hard-coded to `broker.hivemq.com`. |
| `src/production/IoT/2026_T1_new_onboarding/onboarding_client.py` | 12, 42 | Public broker `broker.hivemq.com`; fallback IP uses `127.0.0.1`. |
| `src/production/IoT/2026_T1_new_onboarding/onboarding_server.py` | 6 | HiveMQ Cloud broker hostname is hard-coded. |
| `src/production/IoT/previous_implementation/setup/onboarding_client.py` | 9, 37 | HiveMQ Cloud broker hostname and `127.0.0.1` fallback are hard-coded. |
| `src/production/IoT/previous_implementation/setup/onboarding_server.py` | 5 | HiveMQ Cloud broker hostname is hard-coded. |

## Reorganisation Notes

- Keep `edge_inference/` as the primary IoT production path, but externalise the MQTT broker default before production deployment.
- Review `management_application/` with Backend because its upload endpoint points to a LAN Flask-style URL instead of the current API service.
- Archive `previous_implementation/` only after the IoT team confirms no active onboarding, device registry, or deployment scripts depend on it.
- Separate onboarding/tutorial material from active runtime code once folder moves are approved.
