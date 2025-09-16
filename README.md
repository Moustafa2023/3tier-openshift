3-Tier OpenShift Demo
=====================

Structure:
- frontend: Flask app serving a simple HTML page (Dockerfile included)
- backend: Flask API that talks to PostgreSQL (Dockerfile included)
- db: PostgreSQL deployment and PVC

Quick usage (OpenShift Sandbox):

1. Create a project (namespace):
   oc new-project three-tier-demo

2. Apply secret, PVC, DB, services and deployments:
   oc apply -f k8s/namespace.yaml\n
   oc apply -n three-tier-demo -f k8s/secret.yaml
   oc apply -n three-tier-demo -f k8s/db-pvc.yaml
   oc apply -n three-tier-demo -f k8s/db-deployment.yaml
   oc apply -n three-tier-demo -f k8s/db-service.yaml
   oc apply -n three-tier-demo -f k8s/backend-deployment.yaml
   oc apply -n three-tier-demo -f k8s/backend-service.yaml
   oc apply -n three-tier-demo -f k8s/frontend-deployment.yaml
   oc apply -n three-tier-demo -f k8s/frontend-service.yaml
   oc apply -n three-tier-demo -f k8s/frontend-route.yaml

3. Build & push images for frontend and backend to Docker Hub, then edit k8s YAMLs to replace <DOCKERHUB_USER> with your repo name.

Notes:
- Replace <DOCKERHUB_USER> placeholders in k8s manifests with your Docker Hub username and pushed image tags.
- In the OpenShift sandbox you can use the web terminal to build with `buildah`/`podman` or let GitHub Actions build and push images.
- If PVC remains Pending, try smaller size or remove storageClassName to use default storage class.
