import os

# Replace values either to environmental variables or statically

# Local configuration file for github_client
github_client = {'username': os.environ['github_username'],
                 'password': os.environ['github_password'],
                 'api_token': os.environ['github_token']}

# Local configuration file for gitlab_client
gitlab_client = {'username': '',
                 'password': ''}
