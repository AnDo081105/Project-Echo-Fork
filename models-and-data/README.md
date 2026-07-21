# Models And Data

Owner: Engine. Secondary stakeholders: Backend for deployment packaging and IoT for edge exports.

This directory records where large model and data artifacts live outside normal Git. Keep only lightweight metadata, manifests and retrieval notes here.

Do not commit:

- trained weights or checkpoints
- generated mel caches
- MLflow run directories
- exported ONNX or TFLite bundles unless approved for Git LFS or DVC
- raw credentials or local absolute paths

Use `docs/model-storage-policy.md` for the storage rules and required metadata.
