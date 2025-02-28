pipeline {
    agent any

    stages {
        stage('Clone Repository') {
            steps {
                git 'https://github.com/your-username/your-repository.git'
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