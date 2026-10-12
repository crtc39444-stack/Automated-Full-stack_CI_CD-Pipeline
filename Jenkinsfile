pipeline {
    agent any

    options {
        timestamps()
    }

    stages {
        stage('Checkout Verification') {
            steps {
                echo 'Jenkins pipeline started!'
                sh 'git rev-parse --short HEAD'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh '''
                    python3 -m venv .venv
                    .venv/bin/python -m pip install --upgrade pip
                    .venv/bin/python -m pip install -r Backend/requirements.txt
                    .venv/bin/python -m pip install pytest
                '''
            }
        }

        stage('Run Tests') {
            steps {
                dir('Backend') {
                    sh 'python3 -m pytest -v'
                }
            }
        }
    }

    post {
        success {
            echo 'Pipeline completed successfully!'
        }

        failure {
            echo 'Pipeline failed. Check Console Output.'
        }
    }
}
