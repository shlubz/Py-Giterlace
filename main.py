import sys
import os

from github.client import GitHub
from github.caller import api_caller

if __name__ == '__main__':

    username = input('\nWhat is your github username? ')
    API_TOKEN = os.environ.get('github_token')  # Define GitHub token
    GITHUB_API = 'https://api.github.com'  # Default url for GitHub API

    print()

    # Creates an authenticated session object with given username and token
    auth_session = GitHub(username, API_TOKEN)
    auth_session.print_session()

    # Start program with function_caller
    api_caller(GITHUB_API, auth_session)
