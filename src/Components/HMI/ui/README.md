# Project Echo HMI UI

Owner: HMI team
Status: Active production UI/server for the current `src/Components` Docker Compose stack

## Runtime Role

This directory contains the Node/Express server, server-side route/controller/middleware code, and static browser dashboard assets used by `src/Components/HMI/HMI.Dockerfile`.

`src/Components/docker-compose.yml` builds this service as `echo_hmi`, mounts this directory to `/usr/src/app/ui`, exposes port `8080`, and injects `API_HOST=ts-api-cont`.

## Local Setup

```powershell
npm install
npm run dev
```

The default local URL is `http://localhost:8080`.

## Configuration Notes

- Prefer `API_HOST`, `CLIENT_URL`, `MONGODB_URI`, `MONGO_URI`, `JWT_SECRET`, `COOKIE_SECRET`, and `STRIPE_PRIVATE_KEY` from the environment.
- Current code still contains hard-coded localhost URLs, Redis host defaults, Stripe redirect URLs, and mail credentials. See `../README.md` for the line-numbered audit.
- `node_modules` is a generated dependency folder and should not be committed or documented as a source dependency.
