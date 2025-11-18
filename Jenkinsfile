pipeline {
    agent any

    tools {
        allure 'allure'
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Setup Python Environment') {
            steps {
                sh '''
                    echo "Python version:"
                    python3 --version

                    python3 -m venv venv
                    . venv/bin/activate

                    echo "Installing project dependencies..."
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Run Playwright Tests') {
            steps {
                sh '''
                    . venv/bin/activate
                    echo "Running Playwright tests..."
                    python -m pytest --alluredir=allure-results -v
                '''
            }
        }
    }

    post {
        always {
            allure([
                includeProperties: false,
                jdk: '',
                results: [[path: 'allure-results']]
            ])
            echo "Build completed with status: ${currentBuild.result}"
        }

        success {
            echo '✅ All Playwright tests passed successfully!'
        }

        failure {
            echo '❌ Playwright tests failed!'
        }
    }
}