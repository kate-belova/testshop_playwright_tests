pipeline {
    agent any

    stages {
        stage('Run Tests') {
            steps {
                sh '''
                    mkdir -p allure-results-new

                    python3 -m venv venv
                    venv/bin/pip install -r requirements.txt
                    venv/bin/pytest --alluredir=allure-results-new

                    if [ -d "allure-results/history" ]; then
                        cp -r allure-results/history allure-results-new/
                    fi

                    rm -rf allure-results
                    mv allure-results-new allure-results
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