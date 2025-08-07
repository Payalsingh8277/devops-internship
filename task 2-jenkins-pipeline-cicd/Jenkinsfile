pipeline {
    agent any

    stages {
        stage('Clone Repo') {
            steps {
                git branch: 'main', url: 'https://github.com/Payalsingh8277/Flask-ci-cd-demo.git'
            }
        }

        stage('Build') {
            steps {
                echo 'Building the application...'
            }
        }

        stage('Test') {
            steps {
                echo 'Running tests...'
            }
        }

        stage('Deploy') {
            steps {
                sh 'docker build -t flask-app .'
                sh 'docker run -d -p 5000:5000 flask-app'
            }
        }
    }
}
