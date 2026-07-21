# Data Tools Target

Owner: Engine
Status: Active landing area for offline data tooling

`src/data_tools` is reserved for maintained offline data preparation, export, cleaning and small checked-in examples. It is not a production runtime service area.

## Current Compatibility Boundary

- `store/` was moved from `src/Components/Store` after reference checks found no runtime, compose or Docker dependency on the old path.
- `repository_inventory/` contains the local file/database inventory helper moved from the repository root.
- `movement_analysis/` contains standalone movement cleaning, prediction and vegetation-density plotting utilities moved out of `src/Components`.
- Data prototype work remains under `src/prototypes/data` during this planning slice.
- Root-level loose notebooks and scripts are being classified into owner-owned prototype, data-tool or docs areas.

## Move Rules

- Keep generated caches, notebook checkpoints, downloaded datasets and model artifacts out of normal Git.
- Keep only small examples that are useful for repeatable tests or tutorials.
- Document any required external dataset, bucket, DVC remote or environment variable before moving a tool here.
