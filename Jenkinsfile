pipeline {
    agent any

    stages {
        stage('Clone Repository') {
            steps {
                git(
                    url: 'https://github.com/danbutuc2/jira-jenkins.git',
                    branch: 'main', 
                    credentialsId: 'github-credentials'
                )
            }
        }
        stage('Install Dependencies') {
            steps {
                sh 'pip install jira'
            }
        }
        stage('Run Script') {
            steps {
                sh 'python create_jira_issue.py'
            }
        }
    }
}
