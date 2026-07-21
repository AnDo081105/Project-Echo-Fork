# Tests Target

Owner: Backend, Engine, HMI and IoT by covered component
Status: Target landing area; current tests remain next to their components

`src/tests` is reserved for shared integration, smoke and cross-component tests after test runners and CI paths are agreed.

## Current Compatibility Boundary

- Component-local tests should stay where they are until CI references are checked.
- Backend load tests currently remain in `src/loadtest`.
- Engine and IoT model validation tests remain near their runtime or prototype code until model artifact handling is clear.

## Suggested Grouping

| Target | Scope |
| --- | --- |
| `backend/` | API, database, auth and messaging tests. |
| `engine/` | preprocessing, inference, model-serving and simulator tests. |
| `hmi/` | server route, browser smoke and API contract tests. |
| `iot/` | edge inference, device messaging and health publishing tests. |
| `integration/` | compose-level and cross-service checks. |
