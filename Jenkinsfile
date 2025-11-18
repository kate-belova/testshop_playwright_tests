pipeline {
    agent any

    stages {
        stage('Run Tests') {
            steps {
                sh '''
                    echo "=== Cleaning previous results ==="
                    rm -rf allure-results

                    echo "=== Setting up environment ==="
                    python3 -m venv venv
                    venv/bin/pip install -r requirements.txt
                    venv/bin/pip install allure-pytest allure-python-commons

                    echo "=== Checking installed packages ==="
                    venv/bin/pip list | grep allure

                    echo "=== Running tests ==="
                    venv/bin/pytest -v

                    echo "=== Checking allure results ==="
                    ls -la allure-results/
                    find allure-results -name "*.json" | wc -l
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
                results: [[path: 'allure-results']]
            ])
        }
    }
}