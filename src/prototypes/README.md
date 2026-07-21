# Prototypes

Primary owners: Backend, Engine, HMI and IoT by subfolder.

`src/prototypes` is retained as the repository R&D area. Do not delete it during cleanup. Prototype work can be promoted only after dependencies, imports, Docker paths, CI paths and runtime consumers are reviewed.

| Folder | Owner | Status |
| --- | --- | --- |
| `api/` | Backend | Earlier FastAPI, MQTT and standalone API/model prototypes. Review unique routes/tests before archiving or promotion. |
| `engine/` | Engine | Active ML R&D, including important PyTorch and edge-inference work. |
| `data/` | Engine | Acquisition, cleaning, training data and generated cache pipelines. |
| `eda/` | Engine | Exploratory data analysis and research material. |
| `computer_vision/` | Engine | Separate computer-vision R&D track. Moved from `Computer Vision/` for lowercase/no-space naming. |
| `hmi/` | HMI | Earlier HMI implementation and non-runtime interface assets. |
| `iot/` | IoT | Hardware, firmware, CAD, LoRaWAN and device experiments. Moved from `Iot/` for lowercase naming. |
| `simulator/` | Engine | Simulator prototypes to compare with production Simulator. Moved from `sim/` for clearer ownership. |
| `hmi/research/project-echo-website/` | HMI | Standalone awareness website prototype moved from `R and D/Project Echo Website/` after checking no generated dependency output was present. |

## Compatibility Notes

- Historical notebooks and external links may still refer to older path casing or folder names.
- New prototype work should use lowercase, no-space paths under `src/prototypes`.
- Do not move generated dependency folders such as `node_modules` as part of prototype cleanup.
