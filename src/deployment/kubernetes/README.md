# Kubernetes Deployment

Owner: Backend with HMI and Engine support
Status: Active deployment configuration folder

The Kubernetes manifests formerly under `src/Echo_Components_on_K8s/K8s_configs`
now live here. This keeps deployment configuration separate from the duplicated
Kubernetes API, HMI frontend and MongoDB source variants that still need owner
review before any merge or archive work.

Do not move duplicate application source into this folder. Backend, HMI and
Engine source should be reconciled with the owning production or prototype path
first.
