# HMI Prototypes

Owner: HMI team
Status: Prototype/reference area; not production runtime

## Scope

This folder contains earlier HMI work, duplicate UI code, digital assets, AI/reference material, and submission overview experiments. The active production HMI remains `src/production/HMI/ui`.

## Current Inventory

- `ui/` - earlier Node/Express HMI implementation. Review against production before archive/merge.
- `Digital Assets/` and `digital_assets/` - design and animal imagery assets. Keep for review; do not delete until production asset usage is checked.
- `ai/` - HMI-owned AI/reference material.
- `submission_overview/` - root submission overview prototype assets moved under HMI ownership.
- `research/project-echo-website/` - standalone awareness website prototype moved from `src/prototypes/R and D/Project Echo Website` after confirming no generated dependency output such as `node_modules` was present.

## Hard-Coded Configuration Audit

| File | Lines | Finding |
| --- | --- | --- |
| `src/prototypes/hmi/ui/server.js` | 66 | CORS origin is fixed to `http://localhost:7080`. |
| `src/prototypes/hmi/ui/public/js/routes.js` | 18 | Prototype message API points to `http://localhost:8000/hmi`. |
| `src/prototypes/hmi/ui/public/index.html` | 740 | Prototype checkout call uses `http://localhost:7080/create-checkout-session`. |
| `src/prototypes/hmi/ui/server.js` | 91-92 | Hard-coded Gmail sender credentials are present. |

## Reorganisation Notes

- Keep this area visible as HMI-owned prototype work.
- Compare features with `src/production/HMI/ui` before moving, merging, or archiving.
- Do not commit generated dependencies such as `node_modules`.
- Use lowercase, no-space paths for new HMI prototype and research material.
