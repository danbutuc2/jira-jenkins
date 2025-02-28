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
                // Create a virtual environment and install 'jira' package inside it
                sh 'python3 -m venv venv' // Create virtual environment
                // Use bash explicitly to activate the virtual environment
                sh 'bash -c "source venv/bin/activate && pip install jira"' // Install dependencies
            }
        }
        stage('Run Script') {
            steps {
                // Use bash explicitly to activate the virtual environment and run the script
                sh 'bash -c "source venv/bin/activate && python create_jira_issue.py"'
            }
        }
    }
}
