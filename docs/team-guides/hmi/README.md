# HMI Guide

Owner: HMI team
Status: Planning and compatibility notes

The production HMI remains `src/production/HMI/ui`. The target production destination is `src/production/hmi` after the HMI team checks server routes, public assets, Docker image inputs, compose mounts, K8s frontend differences and API URL configuration.

## Current HMI Paths

| Path | Status | Note |
| --- | --- | --- |
| `src/production/HMI/ui` | Active production | Node/Express server and browser dashboard. |
| `src/prototypes/hmi/ui` | Prototype | Compare against production before archiving or merging unique views. |
| `src/prototypes/hmi/research/project-echo-website` | HMI research prototype | Moved from `src/prototypes/R and D/Project Echo Website` after confirming no generated dependency output was present. |
| `src/Echo_Components_on_K8s/frontend` | Deployment variant | Merge configuration only; avoid maintaining duplicate frontend source. |
| `Design/Branding` | HMI reference | Keep branding assets visible until production usage is checked. |

## Compatibility Notes

- Do not move `node_modules` into target folders.
- Replace local API URLs, Redis hosts, SMTP credentials, cookie secrets and browser fetch URLs with environment-based configuration before promotion.
- Keep static images and design assets with their prototype until asset references are checked from HTML, CSS and server routes.
