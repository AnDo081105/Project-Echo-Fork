# Echo Simulator Component

Owner: Engine team
Status: production support component
Runtime role: simulates animal movement, microphone proximity, and vocalisation events for the local EchoNet stack

The simulator is part of the production `src/production` boundary, but it is Engine-owned because it produces testable animal/audio events for the Engine runtime. It publishes simulated recordings to MQTT and listens for simulator control messages.

## Key Files

| Path | Purpose | Status |
| --- | --- | --- |
| `src/system_manager.py` | Starts the simulator control loop and subscribes to MQTT control topics. | Active. |
| `src/comms_manager.py` | Publishes simulator audio/vocalisation messages to MQTT using environment variables. | Active. |
| `src/simulator.py` | Coordinates animal movement and recording events. | Active. |
| `src/entities/` | Animal, species, microphone, and base entity models. | Active support code. |
| `src/factories/` | Animal and sensor factory helpers. | Active support code. |
| `src/config/mics_info.json` | Microphone location/config sample. | Keep as simulator config. |
| `Simulator.Dockerfile` | Docker image used by `src/production/docker-compose.yml`. | Active. |

## Runtime Configuration

`src/comms_manager.py` and `src/system_manager.py` read MQTT settings from environment variables:

| Variable | Use |
| --- | --- |
| `MQTT_CLIENT_URL` | Broker host used by the simulator client. |
| `MQTT_CLIENT_PORT` | Broker port. |
| `MQTT_PUBLISH_URL` | Topic used for simulated audio/vocalisation messages. |

`src/control_sim.py` is a manual helper and still hard-codes `MQTT_BROKER_URL = "echo_mqtt"` at line 5 and `MQTT_BROKER_PORT = 1883` at line 6. Replace these with environment values before treating the helper as portable runtime tooling.

## Reorganisation Notes

Keep this folder in the production boundary for now. Earlier simulator/R&D work under `src/prototypes/simulator` should only be archived or merged after comparison with this component.
