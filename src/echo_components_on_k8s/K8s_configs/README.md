# Kubernetes Configs Moved

The Kubernetes manifests formerly kept here have moved to:

`src/deployment/kubernetes`

This old path is retained only as a compatibility note. Use the new deployment folder for Kubernetes config changes. The rest of `src/Echo_Components_on_K8s` remains in place because its duplicated API, frontend and MongoDB assets need separate owner review before any merge or archive work.
