# Engine Notebooks

Owner: Engine team
Status: prototype and experiment notebooks
Runtime role: none

This folder contains notebooks moved out of `src/production/Engine` after `rg` found no non-generated references to the previous paths. The production Engine runtime remains in `src/production/Engine`.

## Moved From Components

| Current path | Previous path |
| --- | --- |
| `src/prototypes/engine/notebooks/generic_engine_pipeline.ipynb` | `src/production/Engine/generic_engine_pipeline.ipynb` |
| `src/prototypes/engine/notebooks/multilabel_engine_pipeline.ipynb` | `src/production/Engine/multilabel_engine_pipeline.ipynb` |
| `src/prototypes/engine/notebooks/optimised_engine_pipeline.ipynb` | `src/production/Engine/optimised_engine_pipeline.ipynb` |
| `src/prototypes/engine/notebooks/surf_features_engine_model.ipynb` | `src/production/Engine/surf_features_engine_model.ipynb` |
| `src/prototypes/engine/notebooks/helpers/tesing2.py.ipynb` | `src/production/Engine/helpers/tesing2.py.ipynb` |

New Engine notebooks should use lowercase, no-space folders under `src/prototypes/engine` unless they are part of a preserved historical experiment.
