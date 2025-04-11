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
                subject: "❌ Jenkins Job Failed: ${env.JOB_NAME}",
                body: """<p>Hi Seenu,</p>
                         <p>The Jenkins job <b>${env.JOB_NAME}</b> has failed.</p>
                         <p><a href="${env.BUILD_URL}">Click here to view the build</a></p>
                         <p><a href="${env.BUILD_URL}report.html">View Test Report</a></p>""",
                to: "mseenu7871@gmail.com"
            )
        }
    }
}
