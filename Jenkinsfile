pipeline {
    agent any

    stages {
        stage('Checkout Code') {
            steps {
                git branch: 'main', url: 'https://github.com/v3nky13/oneclick.git'
            }
        }

        stage('Check For Python') {
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

        stage('Run Code') {
            steps {
                script {
                    if (isUnix()) {
                        sh 'python3 main.py'
                    } else {
                        bat 'python main.py'
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