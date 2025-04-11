pipeline {
    agent any

    stages {
        stage('Install Dependencies') {
            steps {
                bat 'python -m pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                bat 'python -m pytest tests/test_google.py --html=report.html'
            }
        }

        stage('Publish Report') {
            steps {
                publishHTML([reportDir: '.', reportFiles: 'report.html', reportName: 'Test Report'])
            }
        }
    }
}
