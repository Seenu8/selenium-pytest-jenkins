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
                bat '"C:\\Users\\HP ADMIN\\AppData\\Local\\Programs\\Python\\Python310\\python.exe" -m pytest tests/ --html=report.html'
            }
        }

        stage('Publish Report') {
            steps {
                publishHTML([reportDir: '.', reportFiles: 'report.html', reportName: 'Test Report'])
            }
        }
    }

    post {
        failure {
            emailext(
                to: 'mseenu7871@gmail.com',
                subject: "❌ Jenkins Job '${env.JOB_NAME} [#${env.BUILD_NUMBER}]' Failed",
                body: """
Hello,

The Jenkins job '${env.JOB_NAME}' [Build #${env.BUILD_NUMBER}] has FAILED.

You can review the build here: ${env.BUILD_URL}

Regards,
Jenkins CI
                """.stripIndent()
            )
        }
    }
}
