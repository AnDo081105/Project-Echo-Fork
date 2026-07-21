# Experiments

Owner: Engine team
Status: experiment tracking and model comparison workspace
Runtime role: none

This folder contains MLflow/DVC demonstrations, model comparison scripts, and small tracked artifacts. It should remain separate from the production Engine runtime. Generated MLflow output belongs in external/generated storage, not normal Git.

## Current Files

| Path | Purpose | Treatment |
| --- | --- | --- |
| `mlflow_tracking.py`, `mlflow_model_registry_demo.py`, `model_registry_demo.py` | MLflow tracking and registry examples. | Keep as experiment tooling. |
| `experiment_tracking_demo.py`, `core_tracking_demo.py`, `dvc_training_demo.py`, `dvc_tracking.ps1` | Tracking demonstrations. | Keep and document prerequisites. |
| `simple_model_logistic.py`, `complex_model_rf.py`, `load_registered_model.py` | Example model scripts. | Keep as reproducible experiments. |
| `model_comparison.csv`, `mlflow_vs_dvc_comparison.md` | Comparison outputs/reporting. | Review whether final reports should move to `docs`. |
| `*.dvc` | DVC pointers for generated model/output artifacts. | Keep pointers; keep large artifacts external. |

## Reorganisation Notes

Recommended future grouping:

- `mlflow/`: tracking and registry examples.
- `dvc/`: DVC tracking examples and pointer files.
- `comparisons/`: comparison scripts, CSVs, and reports.

Do not commit `mlruns/` generated run records. The ownership review says generated MLflow output should be removed from normal Git and ignored after useful records are exported.
