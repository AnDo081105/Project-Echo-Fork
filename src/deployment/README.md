# Deployment

Owner: Backend with HMI, Engine and IoT support
Status: Deployment configuration area; current compose runtime remains in `src/Components`

`src/deployment` is for deployment configuration after runtime source is separated from deployment variants.

## Current Compatibility Boundary

- Authoritative local runtime compose files remain in `src/Components/docker-compose.yml` and `src/Components/docker-compose.test.yml`.
- Kubernetes manifests moved from `src/Echo_Components_on_K8s/K8s_configs` to `src/deployment/kubernetes`.
- Duplicated Kubernetes API, frontend and MongoDB source variants remain in `src/Echo_Components_on_K8s` pending owner review.
- Do not copy duplicate API or HMI source here. Merge application source back into the owning production/prototype path first.

## Planned Layout

| Target | Owner | Planned source |
| --- | --- | --- |
| `docker/` | Backend | Compose files and Docker-only deployment helpers after CI/compose path checks. |
| `kubernetes/` | Backend | Kubernetes manifests moved from `src/Echo_Components_on_K8s/K8s_configs`. |

## Compatibility Notes

- HMI deployment-specific frontend configuration should be reconciled with `src/Components/HMI/ui`, not maintained as a second frontend tree.
- Backend deployment configuration should preserve API, MongoDB, MQTT and Redis service names expected by current compose users.
- Engine model-serving configuration remains Engine-owned, with Backend supporting deployment wiring.
