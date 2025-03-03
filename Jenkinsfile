pipeline {
    agent any
    environment {
        // Bind Jira credentials to environment variables
        JIRA_CREDENTIALS = credentials('Jira-Api-Token') // ID from Jenkins credentials
    }
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
                // Create a virtual environment and install 'jira' package inside it
                sh 'python3 -m venv venv' // Create virtual environment
                sh 'bash -c "source venv/bin/activate && pip install jira"' // Install dependencies
            }
        }
        stage('Run Script') {
            steps {
                // Pass Jira credentials as command-line arguments within the virtual environment
                sh '''
                    bash -c "source venv/bin/activate && python create_jira_issue.py \
                        --jira-url 'https://danbutuc.atlassian.net' \
                        --jira-user '${JIRA_CREDENTIALS_USR}' \
                        --jira-token '${JIRA_CREDENTIALS_PSW}'"
                '''
            }
        }
    }
}
