
pipeline {
    agent any

    options {
        timestamps()
        disableConcurrentBuilds()
        skipDefaultCheckout(true)
    }

    parameters {
        booleanParam(
            name: 'PUSH_TO_DOCKERHUB',
            defaultValue: false,
            description: 'Push built images to Docker Hub'
        )
    }

    environment {
        BACKEND_IMAGE = 'ci-cd-backend'
        FRONTEND_IMAGE = 'ci-cd-frontend'
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm

                sh '''
                    echo "Repository checkout successful"
                    git rev-parse --short HEAD
                    test -f Backend/requirements.txt
                    test -f Backend/app.py
                    test -f Backend/tests/test_app.py
                    test -f Frontend/Dockerfile
                    test -f Backend/Dockerfile
                '''
            }
        }

        stage('Test Application') {
            steps {
                sh '''
                    docker run --rm \
                      -v "$WORKSPACE:/workspace" \
                      -w /workspace \
                      python:3.14-slim \
                      sh -ec '
                        python -m pip install --no-cache-dir \
                          -r Backend/requirements.txt
                        python -m pip install --no-cache-dir pytest
                        python -m pytest -v Backend/tests
                      '
                '''
            }
        }

        stage('Build Docker Images') {
            steps {
                sh '''
                    docker build \
                      -t ci-cd-backend:${BUILD_NUMBER} \
                      -f Backend/Dockerfile Backend

                    docker build \
                      -t ci-cd-frontend:${BUILD_NUMBER} \
                      -f Frontend/Dockerfile Frontend
                '''
            }
        }

        stage('Push to Docker Hub') {
            when {
                expression {
                    return params.PUSH_TO_DOCKERHUB
                }
            }

            steps {
                withCredentials([
                    usernamePassword(
                        credentialsId: 'dockerhub-creds',
                        usernameVariable: 'DH_USER',
                        passwordVariable: 'DH_PASSWORD'
                    )
                ]) {
                    sh '''
                        set -eu

                        echo "$DH_PASSWORD" | docker login \
                          --username "$DH_USER" \
                          --password-stdin

                        docker tag ci-cd-backend:${BUILD_NUMBER} \
                          "$DH_USER/ci-cd-backend:${BUILD_NUMBER}"

                        docker tag ci-cd-frontend:${BUILD_NUMBER} \
                          "$DH_USER/ci-cd-frontend:${BUILD_NUMBER}"

                        docker push "$DH_USER/ci-cd-backend:${BUILD_NUMBER}"
                        docker push "$DH_USER/ci-cd-frontend:${BUILD_NUMBER}"

                        docker logout
                    '''
                }
            }
        }
    }

    post {
        success {
            echo 'CI pipeline completed successfully!'
        }

        failure {
            echo 'CI pipeline failed. Check Console Output for the first error.'
        }

        always {
            echo 'Pipeline execution finished.'
        }
    }
}
