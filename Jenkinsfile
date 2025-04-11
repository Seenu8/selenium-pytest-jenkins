pipeline {
    agent any

    stages {
        stage('Clone') {
            steps {
                git 'https://github.com/Seenu8/selenium-pytest-jenkins.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                bat 'pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                bat 'pytest tests/ --html=report.html'
            }
        }
    }

    post {
        always {
            archiveArtifacts artifacts: 'report.html', allowEmptyArchive: true
        }
    }
}
