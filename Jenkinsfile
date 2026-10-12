
pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                echo 'Project code checkout successful!'
                sh 'git rev-parse --short HEAD'
            }
        }

        stage('Check Python') {
            steps {
                sh 'python3 --version'
            }
        }

        stage('Run Tests') {
            steps {
                sh '''
                    docker run --rm \
                      -v "$WORKSPACE:/app" \
                      -w /app \
                      python:3.14-slim \
                      sh -c "pip install -r Backend/requirements.txt pytest && python -m pytest -v Backend/tests"
                '''
            }
        }
    }

    post {
        success {
            echo 'All stages completed successfully!'
        }

        failure {
            echo 'Pipeline failed. Check Console Output.'
        }
    }
}
