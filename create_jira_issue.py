#!/usr/bin/env python3
import argparse
from jira import JIRA  # type: ignore

def connect_to_jira(jira_url, jira_user, jira_token):
    """Connect to Jira using provided credentials."""
    try:
        jira = JIRA(server=jira_url, basic_auth=(jira_user, jira_token))
        return jira
    except Exception as e:
        print(f"Failed to connect to Jira: {e}")
        raise

def create_issue(jira, project_key, summary, description, issue_type):
    """Create a new Jira issue."""
    issue_dict = {
        'project': {'key': project_key},
        'summary': summary,
        'description': description,
        'issuetype': {'name': issue_type},
    }
    return jira.create_issue(fields=issue_dict)

def main():
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description="Create a Jira issue")
    parser.add_argument('--jira-url', required=True, help="Jira server URL (e.g., https://danbutuc.atlassian.net)")
    parser.add_argument('--jira-user', required=True, help="Jira user email")
    parser.add_argument('--jira-token', required=True, help="Jira API token")
    parser.add_argument('--project-key', default='AUT', help="Jira project key (default: AUT)")
    parser.add_argument('--summary', default='New issue summary', help="Issue summary")
    parser.add_argument('--description', default='Description of the issue', help="Issue description")
    parser.add_argument('--issue-type', default='Task', help="Issue type (default: Task)")
    args = parser.parse_args()

    # Connect to Jira
    jira = connect_to_jira(args.jira_url, args.jira_user, args.jira_token)

    # Create the issue
    new_issue = create_issue(jira, args.project_key, args.summary, args.description, args.issue_type)
    print(f"Issue {new_issue.key} created successfully.")

if __name__ == "__main__":
    main()
