# IoT Prototypes

Owner: IoT team
Status: Hardware, firmware, Raspberry Pi, LoRaWAN, CAD, and component-test prototype area

## Scope

This folder is not production runtime. It preserves IoT experiments that may inform field-device deployment, enclosure design, PlatformIO/ESP32 integration, onboarding, and edge inference.

## Current Inventory

- `component_testing/` - MQTT/audio/GPS/health component experiments.
- `hmi_node_connection/` - ESP32/PlatformIO experiment for HMI/API node registration.
- `IoT Device Case Birdhouse Holder/` and `iot_device_case_birdhouse_holder/` - enclosure/CAD reference assets. The duplicate naming should be resolved only after file comparison.
- `lorawan_investigation/` - LoRaWAN research.
- `microphone/` - microphone firmware experiments.
- `mobilenet_rpi_prototype/` and `yamnet_rpi_prototype/` - Raspberry Pi model/device prototypes.
- `New Sensor Testing/` and `new_sensor_testing/` - sensor testing work. The duplicate naming should be resolved only after file comparison.
- `power-management/` and `power_management/` - power-management notes. The duplicate naming should be resolved only after file comparison.
- `Rasberry Pi Emulation/` and `raspberry_pi_emulation/` - Raspberry Pi emulation work. The spelling/duplicate naming should be resolved only after file comparison.

## Hard-Coded Configuration Audit

| File | Lines | Finding |
| --- | --- | --- |
| `src/prototypes/iot/New Sensor Testing/client.py` | 30, 54 | MQTT broker is hard-coded to `broker.hivemq.com`. |
| `src/prototypes/iot/component_testing/audio.py` | 15 | MQTT broker is hard-coded to `broker.hivemq.com`. |
| `src/prototypes/iot/component_testing/audio_server.py` | 31 | MQTT broker is hard-coded to `broker.hivemq.com`. |
| `src/prototypes/iot/component_testing/gps.py` | 9 | MQTT broker is hard-coded to `broker.hivemq.com`. |
| `src/prototypes/iot/component_testing/health.py` | 8 | MQTT broker is hard-coded to `broker.hivemq.com`. |
| `src/prototypes/iot/component_testing/json_server.py` | 14 | MQTT broker is hard-coded to `broker.hivemq.com`. |
| `src/prototypes/iot/hmi_node_connection/src/esp32-http-server.ino` | 40 | API host is hard-coded to LAN IP `192.168.1.9`. |
| `src/prototypes/iot/hmi_node_connection/src/esp32-http-server.ino` | 115, 161, 222 | Device API URLs are built from `http://` plus the hard-coded LAN IP and port `9000`. |
| `src/prototypes/iot/hmi_node_connection/wokwi.toml` | 6, 8 | Wokwi local forwarding uses `localhost:8180`. |
| `src/prototypes/iot/hmi_node_connection/src/esp32-http-server.ino` | 9 | Wokwi instructions refer to `http://localhost:9080`. |
| `src/prototypes/iot/mobilenet_rpi_prototype/README.md` | 27 | Raspberry Pi SSH example uses LAN IP `192.168.1.100`. |
| `src/prototypes/iot/Rasberry Pi Emulation/start.sh` | 18 | Emulation SSH forwarding message uses `localhost:2222`. |
| `src/prototypes/iot/Rasberry Pi Emulation/Dockerfile` | 19, 24, 26 | Build downloads Raspberry Pi image/kernel assets from fixed external URLs. |

## Reorganisation Notes

- Keep prototypes grouped by hardware/platform when moves are approved.
- Do not delete CAD, firmware, or Raspberry Pi assets during cleanup.
- Before any folder rename, check duplicate pairs and update scripts/docs that reference the original paths.
