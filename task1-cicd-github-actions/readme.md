# CI/CD pipeline

This repository contains a simple Flask application with a working **CI/CD pipeline using GitHub Actions**.

## What I Did

- Created a basic Flask app (`app.py`)
- Dockerized the application using a `Dockerfile`
- Wrote a GitHub Actions workflow (`.github/workflows/cicd.yml`) to:
  - Install Python dependencies
  - Build the Docker image
  - Run the container

## How to Run Locally

```bash
# Clone the repo
git clone https://github.com/Payalsingh8277/Flask-ci-cd-demo.git
cd Flask-ci-cd-demo

# Build Docker image
docker build -t flask-app .

# Run the container
docker run -d -p 5000:5000 flask-app
