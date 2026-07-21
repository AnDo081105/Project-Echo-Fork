# Project Echo HMI Prototype UI

Owner: HMI team
Status: Prototype/reference implementation; not the canonical production HMI

The production HMI is `src/production/HMI/ui`. This folder should be reviewed for unique features before it is merged or archived.

## Local Setup

```powershell
npm install
node server.js
```

## Reorganisation Notes

- Do not rely on checked-in `node_modules`; reinstall dependencies from `package.json`.
- Hard-coded local API and checkout URLs remain in this prototype. See `../README.md` for exact audit lines.
- Keep this folder until HMI confirms whether any prototype-only pages, routes, or assets should be promoted.
