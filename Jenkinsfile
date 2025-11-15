pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Setup Python Environment') {
            steps {
                sh '''
                    echo "=== Environment Check ==="
                    echo "Python version:"
                    python3 --version

                    echo "Playwright version:"
                    playwright --version

                    echo "Available Playwright browsers:"
                    ls -la /root/.cache/ms-playwright/

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
                    echo "Running Playwright tests with global browsers..."
                    python -m pytest --alluredir=allure-results -v
                '''
            }
        }
    }

    post {
        always {
            archiveArtifacts artifacts: 'allure-results/**/*', fingerprint: true
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