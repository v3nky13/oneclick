pipeline {
    agent any

    stages {
        stage('Checkout Code') {
            steps {
                git branch: 'main', url: 'https://github.com/v3nky13/oneclick.git'
            }
        }

        stage('Check Python Version') {
            steps {
                script {
                    if (isUnix()) {
                        sh 'python3 --version'
                        sh 'which python3'
                    } else {
                        bat 'python --version'
                        bat 'where python'
                    }
                }
            }
        }

        stage('Setup Environment') {
            steps {
                script {
                    if (isUnix()) {
                        sh 'python3 -m venv venv && source venv/bin/activate'
                    } else {
                        bat 'python -m venv venv && call venv\\Scripts\\activate'
                    }
                }
            }
        }

        stage('Install Dependencies') {
            steps {
                script {
                    if (fileExists('requirements.txt')) {
                        if (isUnix()) {
                            sh 'source venv/bin/activate && pip install -r requirements.txt'
                        } else {
                            bat 'call venv\\Scripts\\activate && pip install -r requirements.txt'
                        }
                    }
                }
            }
        }

        stage('Run Code') {
            steps {
                script {
                    if (isUnix()) {
                        sh 'source venv/bin/activate && python main.py'
                    } else {
                        bat 'call venv\\Scripts\\activate && python main.py'
                    }
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