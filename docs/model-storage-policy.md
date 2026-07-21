# Model And Data Storage Policy

Owner: Engine. Secondary stakeholders: Backend for deployment support and IoT for edge model export.

Model weights, checkpoints, generated caches and experiment output should not be committed to normal Git. Use one of these storage paths instead:

- DVC for reproducible data and model artifacts tied to experiments.
- Git LFS only for artifacts that must remain in the repository workflow and are approved by the team.
- External storage, such as the Project Echo shared drive or cloud bucket, for large trained models and exported deployment bundles.

## Applies To

- `src/production/Engine/models/`
- `src/production/Engine/yamnet_dir/` model assets
- `src/prototypes/engine/torch_impl/model/`
- `src/prototypes/engine/torch_impl/Integrate_EfficientNetV2_Engine/_trained_models/`
- `src/prototypes/data/mel_cache_eff/`
- `src/prototypes/data/mel_cache_panns/`
- `mlruns/`
- local `.onnx`, `.tflite`, `.joblib`, `.pkl`, `.pt`, `.pth` and checkpoint output

## Required Metadata

Each externally stored artifact should have a small text record in Git that includes:

- artifact name and model family
- owner
- storage location
- training data or experiment reference
- expected runtime consumer
- date exported
- validation status

Do not add raw credentials, service account keys or local absolute paths to these records.
