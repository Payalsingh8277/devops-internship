# Flask CI/CD Pipeline using Jenkins, Docker, and GitHub

This repository contains a simple Flask application integrated with a CI/CD pipeline using **Jenkins**, **Docker**, and **GitHub**.

---

## What I Did

- Created a basic **Flask** application (`app.py`)
- Defined required packages in `requirements.txt`
- Wrote a `Dockerfile` to containerize the app
- Configured a `Jenkinsfile` to:
  - Clone the GitHub repository
  - Build the Docker image
  - Run the Docker container automatically

---

## Technologies Used

- **Python (Flask)**
- **Docker**
- **Jenkins**
- **Git & GitHub**

---

## CI/CD Pipeline Flow

1. Push code to GitHub
2. Jenkins pulls the latest code using a **Jenkinsfile**
3. Jenkins builds a Docker image
4. Jenkins runs a Docker container
5. Flask app is deployed on `http://localhost:5000`

---

## How to Run Locally

```bash
# Clone the repository
git clone https://github.com/Payalsingh8277/Flask-ci-cd-demo.git
cd Flask-ci-cd-demo

# Build Docker image
docker build -t flask-app .

# Run the container
docker run -d -p 5000:5000 flask-app
