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
            subject: "Jenkins Job Failed: ${env.JOB_NAME}",
            body: """<p>Job ${env.JOB_NAME} failed at stage.</p>
                     <p>See report at: ${env.BUILD_URL}report.html</p>""",
            recipientProviders: [[$class: 'DevelopersRecipientProvider']],
            to: "mseenu7871@gmail.com"
        )
    }
}

}
