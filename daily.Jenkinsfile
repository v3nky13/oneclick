pipeline {
    agent any

    stages {
        stage('Checkout Code') {
            steps {
                git branch: 'main', url: 'https://github.com/v3nky13/oneclick.git'
            }
        }

        stage('Setup Environment') {
            steps {
                script {
                    bat 'python -m venv venv && call venv\\bin\\activate'
                }
            }
        }

        stage('Install Dependencies') {
            steps {
                script {
                    if (fileExists('requirements.txt')) {
                        bat 'call venv\\bin\\activate && pip install -r requirements.txt'
                    }
                }
            }
        }

        stage('Run Code') {
            steps {
                script {
                    bat 'call venv\\Scripts\\activate && python main.py'
                }
            }
        }
    }

    post {
        always {
            echo 'Pipeline finished!'
        }
    }
}
