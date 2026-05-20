pipeline {
    agent any

    tools {
        allure 'allure'
    }

    environment {
        VENV_DIR = '.venv'
        ALLURE_RESULTS_DIR = 'allure-results'
        ALLURE_REPORT_DIR = 'allure-report'
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                bat '''
                    python -m venv %VENV_DIR%
                    call %VENV_DIR%\\Scripts\\activate.bat
                    python -m pip install --upgrade pip
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Run Tests') {
            steps {
                bat '''
                    call %VENV_DIR%\\Scripts\\activate.bat
                    if exist %ALLURE_RESULTS_DIR% rmdir /s /q %ALLURE_RESULTS_DIR%
                    if exist %ALLURE_REPORT_DIR% rmdir /s /q %ALLURE_REPORT_DIR%
                    pytest tests --alluredir=%ALLURE_RESULTS_DIR%
                '''
            }
        }

        stage('Publish Allure') {
            steps {
                allure([
                    includeProperties: false,
                    jdk: '',
                    results: [[path: "${ALLURE_RESULTS_DIR}"]],
                    reportBuildPolicy: 'ALWAYS'
                ])
            }
        }
    }

    post {
        always {
            archiveArtifacts artifacts: 'allure-results/**, allure-report/**', allowEmptyArchive: true
        }
    }
}