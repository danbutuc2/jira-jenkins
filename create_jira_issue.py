import os
from jira import JIRA  # type: ignore

# Jira server URL and credentials from environment variables
jira_server = 'https://danbutuc.atlassian.net/'
jira_user = 'danbutuc@gmail.com'
jira_password = 'ATATT3xFfGF0bN-niXGKB107fwFq9aKrtLFNeSeZw3Yez1Yvc3PSqI6nJqiAhDiR5MC1pgHjs0FF11dLKJiHAbHnDsoTrD_k7XvRHhnS3HQPG19kTAteO_wbFy833aHKdXYSR56GbBN850GC3puG4G6zqRMQduyOIbabbhUHT32R_ZDA1lQCXNs=E8336908'

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
