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
                    echo "Python version:"
                    python3 --version

                    echo "Playwright version:"
                    playwright --version

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