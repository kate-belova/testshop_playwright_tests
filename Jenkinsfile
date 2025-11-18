pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Run Tests') {
            steps {
                sh '''
                    cd testshop_playwright_tests
                    git pull

                    python3 -m venv venv
                    venv/bin/pip install -r requirements.txt

                    venv/bin/pytest
                '''
            }
        }
    }

    post {
        always {
            allure([
                includeProperties: false,
                jdk: '',
                reportBuildPolicy: 'ALWAYS',
                results: [[path: 'testshop_playwright_tests/allure-results']]
            ])
        }
    }
}