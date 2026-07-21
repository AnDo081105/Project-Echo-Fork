# Movement Analysis Tools

Owner: Engine

Status: standalone data utilities, not production runtime

These scripts were moved out of `src/production` because they are not imported
by the API, Engine, HMI, IoT, Simulator or Docker Compose runtime.

## Scripts

- `clean_movement_data.py`: reads movement seed data and writes cleaned
  latitude/longitude records.
- `movement_prediction.py`: reads cleaned movement records and plots simple
  movement predictions.
- `projected_movement.py`: plots movement coordinates from either historical
  `movement` records or current MongoDB `animalTrueLLA` records.
- `vegetation_density.py`: plots region vegetation-density values from
  `vegetation_density.json`.

## Defaults

By default, scripts read the production seed input from
`src/production/MongoDB/init/movements.json` when movement data is needed, but
write generated output under `src/data_tools/movement_analysis/outputs`.

Use environment variables to override paths:

- `MOVEMENTS_SOURCE_FILE`
- `MOVEMENTS_OUTPUT_FILE`
- `MOVEMENTS_CLEANED_FILE`
- `ANIMAL_MOVEMENT_FILE`
- `VEGETATION_DENSITY_FILE`
- `MOVEMENT_ANALYSIS_OUTPUT_DIR`
- `MOVEMENT_PREDICTION_OUTPUT_FILE`
- `PROJECTED_MOVEMENT_OUTPUT_FILE`
- `VEGETATION_DENSITY_OUTPUT_FILE`

Generated plots and cleaned output should stay out of normal Git unless they are
small, intentional fixtures.
