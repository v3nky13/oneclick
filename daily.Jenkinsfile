pipeline {
    agent any

    options {
        buildDiscarder(logRotator(numToKeepStr: '10', artifactNumToKeepStr: '5'))
    }

    stages {
        stage('Checkout Code') {
            steps {
                git branch: 'main', url: 'https://github.com/v3nky13/oneclick.git'
            }
        }

        stage('Setup Environment') {
            steps {
                script {
                    bat 'python -m venv venv && call venv\\Scripts\\activate'
                }
            }
        }

        stage('Install Dependencies') {
            steps {
                script {
                    if (fileExists('requirements.txt')) {
                        bat 'call venv\\Scripts\\activate && pip install -r requirements.txt'
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
