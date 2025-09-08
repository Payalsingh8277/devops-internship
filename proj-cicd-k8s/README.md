# Student Management App – Docker & Kubernetes Deployment

## Project Overview
This is a simple **Flask-based Student Management App** deployed using **Docker** and **Kubernetes**, with a **CI/CD pipeline** configured via **GitHub Actions**.

The app allows you to:
- Add students via POST request (`/add`)
- List all students via GET request (`/list`)
- Access a welcome message at the root route (`/`)

The project demonstrates containerization, orchestration, and automated deployment in a DevOps environment.

---

## Tools & Technologies
- **Flask** – Python web framework
- **Docker** – Containerization
- **Kubernetes** – Deployment and service orchestration
- **Minikube** – Local Kubernetes cluster for testing
- **GitHub Actions** – CI/CD workflow
- **Docker Hub** – Hosting container images

---

## Project Structure

proj-cicd-k8s/
├── app.py
├── requirements.txt
├── Dockerfile
├── k8s/
│ ├── flask-deployment.yaml
│ └── flask-service.yaml
├── .github/
│ └── workflows/cicd.yml
└── README.md
