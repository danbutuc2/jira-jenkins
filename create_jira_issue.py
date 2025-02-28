import os
from jira import JIRA  # type: ignore

# Jira server URL and credentials from environment variables
jira_server = 'https://danbutuc.atlassian.net/'
jira_user = os.getenv('JIRA_USER')
jira_password = os.getenv('JIRA_PASSWORD')

# Connect to Jira
jira = JIRA(server=jira_server, basic_auth=(jira_user, jira_password))

# Issue details
issue_dict = {
    'project': {'key': 'AUT'},
    'summary': 'New issue summary',
    'description': 'Description of the issue',
    'issuetype': {'name': 'Task'},
}

# Create the issue
new_issue = jira.create_issue(fields=issue_dict)

print(f"Issue {new_issue.key} created successfully.")