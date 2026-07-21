# Echo Library

Owner: Engine team
Status: reusable/legacy installable inference library, not the active Docker Compose Engine runtime
Runtime role: none in the current `src/production/docker-compose.yml`

This package contains an installable-style Engine inference implementation and older sprint work. It should be kept, but its relationship to `src/production/Engine` and `src/Prototypes/engine/torch_impl` needs review before any merge or archive work.

## Current Boundary

| Area | Purpose | Treatment |
| --- | --- | --- |
| `__init__.py` | Library-level preprocessing and EfficientNetV2-style inference code. | Keep, then parameterise local model path. |
| `Sprint 1_ND/` | Older notebooks, audio samples, and sprint task outputs. | Preserve until notebooks and sample data are classified. |

## Configuration Audit

`Echo/__init__.py:95` loads a model from the absolute Windows path `C:\Users\vamsh\Desktop\Project-Echo\echo_model\1`. This should become a constructor argument, environment variable, or package data path before the library is reused.

`Echo/__init__.py:189` writes a temporary `o.pt` file in the current working directory. Review whether this should use `tempfile` or a configured cache directory.

## Reorganisation Notes

Before moving or merging this package, compare it with:

- `src/production/Engine/echo_engine_iot.py`, the current production Engine runtime candidate.
- `src/Prototypes/engine/Echo Local Library/` and `src/Prototypes/engine/echo_local_library/`, which appear to contain earlier reusable library experiments.
- Any root notebooks or scripts that import `Echo`.
