# 3-Tier Web Application on Kubernetes

This project demonstrates how to deploy a **3-tier web application** (frontend, backend, and database) on **Kubernetes/OpenShift** using Docker images, Deployments, Services, and Routes.

---

## 📌 Architecture
[ User Browser ]
|
(Route)
|
[Frontend Service] --> [Frontend Pods]
|
[Backend Service] --> [Backend Pods]
|
[Database Service] --> [Database Pod]
- **Frontend**: Simple Python Flask app serving the UI.
- **Backend**: Python Flask API handling requests from frontend and talking to DB.
- **Database**: MySQL (with a persistent volume).

---

## 📂 Project Structure
3-tier-app/
├── frontend/

│ ├── app.py

│ ├── requirements.txt

│ └── Dockerfile

├── backend/

│ ├── app.py

│ ├── requirements.txt

│ └── Dockerfile

├── db/

│ └── init.sql

├── k8s/

│ ├── frontend-deployment.yaml

│ ├── backend-deployment.yaml

│ ├── db-deployment.yaml

│ ├── frontend-service.yaml

│ ├── backend-service.yaml

│ ├── db-service.yaml

│ └── route.yaml

└── README.md

## 🚀 How to Run

### 1. Clone Repo
git clone https://github.com/<your-username>/<repo-name>.git
cd <repo-name>
### 2. Build Docker Images
cd frontend
docker build -t <your-dockerhub-username>/frontend:v1 .
cd ../backend
docker build -t <your-dockerhub-username>/backend:v1 .
Push them to Docker Hub:
docker push <your-dockerhub-username>/frontend:v1
docker push <your-dockerhub-username>/backend:v1
### 3. Deploy on Kubernetes
kubectl apply -f k8s/
### 4. Check Status
kubectl get pods
kubectl get svc
### 5. Access the App
Get the Route URL or LoadBalancer IP:
kubectl get routes
###  6.Future Improvements

Add monitoring with Prometheus + Grafana.

Use Helm charts for easier deployment.

Add CI/CD pipeline (GitHub Actions).

Use ConfigMaps & Secrets for DB credentials.
