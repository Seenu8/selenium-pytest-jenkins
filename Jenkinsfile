pipeline {
    agent any

    stages {
        stage('Install Dependencies') {
            steps {
                bat '"C:\\Users\\HP ADMIN\\AppData\\Local\\Programs\\Python\\Python310\\python.exe" -m pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                bat '"C:\\Users\\HP ADMIN\\AppData\\Local\\Programs\\Python\\Python310\\python.exe" -m pytest tests/test_login.py --html=report.html'
            }
        }

        stage('Publish Report') {
            steps {
                publishHTML([reportDir: '.', reportFiles: 'report.html', reportName: 'Test Report'])
            }
        }
    }
}
