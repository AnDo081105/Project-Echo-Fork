# HMI Component

Owner: HMI team
Status: Active production component in the current `src/Components` runtime boundary
Runtime role: Node/Express web server and browser dashboard for EchoNet operators, users, admin views, maps, submissions, donations, and IoT device displays.

## Source Of Truth

This folder follows the parent workspace ownership document, `Project_Echo_Repository_Ownership.md`:

- `src/Components/HMI/ui/server.js` is the production HMI server entry point.
- `src/Components/HMI/ui/public/` contains the browser dashboard, map, admin, sensor-health, and request pages.
- `src/Components/HMI/ui/config`, `controller`, `middleware`, `model`, and `routes` are server-side HMI code.
- `AI/`, `Digital Assets/`, and `Recodings/` are HMI-owned reference/demo assets. They are not confirmed runtime dependencies and should be reviewed before being copied into production images.
- Duplicate HMI code in `src/prototypes/hmi/ui` and `src/Echo_Components_on_K8s/frontend` should be merged or archived only after feature comparison.

## Runtime Dependencies Checked

- `src/Components/docker-compose.yml` and `src/Components/docker-compose.test.yml` build `echo_hmi` from `./HMI/HMI.Dockerfile`.
- Both compose files bind-mount `./HMI/ui` to `/usr/src/app/ui`.
- Compose injects `API_HOST=ts-api-cont`, so HMI code that falls back to `localhost` should prefer environment variables.
- `HMI.Dockerfile` copies `ui/package*.json`, runs `npm ci --omit=dev`, then copies `ui/`.
- The HMI server depends on Redis sessions, the Backend API, MongoDB for donation/admin helpers, external mail service credentials, Stripe, and browser CDN assets.

## Hard-Coded Configuration Audit

These are the HMI-owned URL, localhost, LAN IP, and broker-related findings from this pass:

| File | Lines | Finding |
| --- | --- | --- |
| `src/Components/HMI/ui/server.js` | 15 | `API_BASE_URL` falls back to `http://localhost:9001`; compose API publishes `9000`, so this fallback should be confirmed. |
| `src/Components/HMI/ui/server.js` | 172-174 | CSP `connectSrc` allows fixed local service URLs: `localhost:8080`, `localhost:9000`, `localhost:8000`. |
| `src/Components/HMI/ui/server.js` | 241-242 | Stripe success/cancel URLs are hard-coded to `http://localhost:9001`; should use `CLIENT_URL`. |
| `src/Components/HMI/ui/server.js` | 353, 827 | MongoDB URI fallbacks use `mongodb://localhost:27017`; should use configured compose/K8s service host. |
| `src/Components/HMI/ui/server.js` | 399 | CORS origin includes `http://localhost:8081` and wildcard `*`. |
| `src/Components/HMI/ui/middleware/index.js` | 25 | Redis host is hard-coded to `localhost`; compose service is `echo-redis`. |
| `src/Components/HMI/ui/routes/map.routes.js` | 4 | API URL falls back to `http://localhost:9001`. |
| `src/Components/HMI/ui/routes/auth.routes.js` | 8 | API URL falls back to `http://localhost:9000`. |
| `src/Components/HMI/ui/controller/auth.controller.js` | 4 | API URL falls back to `http://localhost:9000`. |
| `src/Components/HMI/ui/user-visits.html` | 17 | Browser fetch calls `http://localhost:9000/hmi/users` directly. |
| `src/Components/HMI/ui/public/js/HMI.js` | 979 | Weather request calls `http://localhost:9001/hmi/weather...` directly. |
| `src/Components/HMI/ui/public/admin/admin-nodes.html` | 311, 389 | Admin node page fetches `http://localhost:9000/iot/nodes...` directly. |
| `src/Components/HMI/ui/public/admin/admin-nodes.html` | 336 | Placeholder node metadata uses LAN IP `192.168.1.1`. |
| `src/Components/HMI/ui/public/admin/admin-nodes-temp.html` | 185, 195, 275 | Temporary admin node page fetches `http://localhost:9000/iot/nodes...` directly. |
| `src/Components/HMI/ui/robot.txt` | 12 | Sitemap points to `http://localhost:8080/`. |
| `src/Components/HMI/ui/package.json` | 27 | HMI declares `mqtt`, but no production broker endpoint was found in HMI code during this pass. |
| `src/Echo_Components_on_K8s/frontend/server.js` | 37, 54, 326, 698 | K8s frontend fork has fixed local API/CORS URLs and should be merged with the production HMI codebase. |
| `src/Echo_Components_on_K8s/frontend/routes/auth.routes.js` | 47, 72 | K8s frontend fork calls `http://ts-api-cont:9000` directly instead of a shared API base helper. |

Adjacent security findings found during the same audit:

- `src/Components/HMI/ui/server.js:424-425` and `src/Components/HMI/ui/controller/email.controller.js:9-10` contain hard-coded Gmail credentials.
- `src/Components/HMI/ui/server.js:415` uses the literal cookie-session key `"COOKIE_SECRET"` instead of `process.env.COOKIE_SECRET`.

## Reorganisation Notes

- Do not move or delete HMI assets until `AI/`, `Digital Assets/`, and `Recodings/` are checked against Docker image contents and public page references.
- Keep `src/Components/HMI/ui` as the active production path until the HMI team confirms a replacement target.
- Compare `src/prototypes/hmi/ui` and `src/Echo_Components_on_K8s/frontend` against this folder before archive/merge decisions.
