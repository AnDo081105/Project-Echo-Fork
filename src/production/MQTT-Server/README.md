# Project Echo MQTT Server

Owner: Backend
Status: active production infrastructure
Runtime boundary: `src/production/MQTT-Server`

This folder builds the HiveMQ broker used by EchoNet for component messaging.
The broker is started by the canonical local runtime in
`src/production/docker-compose.yml`.

## Local Endpoints

- MQTT client endpoint: `mqtt://localhost:1883`
- HiveMQ Control Center: `http://localhost:8080`

Inside the Compose network, services should use the broker service/container name
instead of `localhost`. Backend-owned code should read broker host and port from:

- `MQTT_BROKER_URL`
- `MQTT_BROKER_PORT`

The current API HMI router still has hard-coded MQTT defaults for local Docker.
See `docs/backend-deployment-infrastructure-audit.md` before changing broker
names, ports or topic names.

## Local Command

From `src/production`:

```sh
docker compose up -d echo_mqtt
```
