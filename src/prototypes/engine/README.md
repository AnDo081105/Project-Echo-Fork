# Engine Prototypes

Owner: Engine team
Status: non-production R&D, with selected candidates feeding production and IoT edge inference
Runtime role: none by default, except where `src/Components/docker-compose.yml` currently builds the Engine image from `torch_impl`

This directory contains the large Engine prototype surface: PyTorch work, TensorFlow/YAMNet experiments, augmentation, event detection, benchmarking, weather/noise modelling, ensemble/overlap work, local library experiments, student tasks, and generated outputs. Do not delete or flatten it during this reorganisation. Reorganise by technical topic only after active dependencies are checked.

## Topic Map

| Topic | Current examples | Treatment |
| --- | --- | --- |
| PyTorch and edge Engine | `torch_impl/` | Preserve. This is an important Engine prototype with IoT dependencies and current compose usage. |
| Transfer learning | `transfer_learning_models/`, `transfer_learning_tasks/` | Keep, then consolidate successful approaches. |
| Augmentation | `augmentation_tasks/`, `augmentation_prototypes/`, `audio_augmentation_comparison/`, `audio_augmentation_probability_task/` | Keep, then group under one augmentation topic. |
| Benchmarking | `benchmarking_and_experimentation/`, reports | Keep working experiments here; move final reports to docs after review. |
| Event detection/segmentation | `event_detection_tasks/`, `event_segmentation_yamnet/`, `completed_event_segmenter/`, `yamnet/` | Keep, identify the canonical implementation. |
| Weather and noise | `weather_detection/`, `weather_detection_nd/`, `noise_detection/`, `lower_audio_quality/`, `removing_background_noise_tasks/` | Keep until relevance is confirmed. |
| Ensemble and overlap | `combining_models_pipeline/`, `overlapping_sound/`, `working_with_overlapping_audio/` | Keep as research. |
| Local libraries | `echo_local_library/` | Compare against root `Echo/` package before merge/archive. |
| Data pipeline and utilities | `data_pipeline/`, `mel_spectrogram_display_function/`, `notebooks/legacy_pipelines/`, `roadmap/` | Keep as organized prototype support material. |
| Student task folders | Named sprint/task folders under normalized snake_case folders | Classify by technical topic before moving. |

## Dependency Notes

- `src/Components/docker-compose.yml` currently builds the `echo_engine` service from `src/prototypes/engine/torch_impl`.
- `src/Components/IoT/edge_inference/README.md` references `torch_impl` model outputs and configuration as an edge inference dependency.
- Large artifacts in prototype paths include `.onnx`, `.pt`, `.pth`, `.tflite`, `.h5`, `.pkl`, generated CSVs, and cached mel arrays. Keep them out of normal Git through DVC, Git LFS, or approved external storage.
- Engine topic folders have been reconciled to normalized snake_case names. Check imports, notebook paths, docs links, and compose references before deeper consolidation.
