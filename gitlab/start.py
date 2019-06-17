import os
import getpass

from gitlab.client import GitLab
from gitlab.caller import api_caller


def start_gitlab():
    """Starts the GitLab client with an authentication session depending on
    user's choice with using a Password method or a Token-based method.
    """

    print('\nStarting GitLab client!\n')
    GITLAB_API = 'https://gitlab.com/api/v4'

    def auth_session_call(USERNAME, API_TOKEN):
        """Returns an authenticated session object based on given method.

        Method 1: Token

        Other methods not supported yet

        Additionally, prints out some session info after method decision.
        """

        auth_session = GitLab(USERNAME, API_TOKEN)
        auth_session.print_session()
        return auth_session

    # Check or get username
    if os.environ.get('GITLAB_USERNAME') == '':
        print('No environmental variable found for GITLAB_USERNAME.\n')
        USERNAME = input('\nPlease enter your GitLab username: ')
    else:
        USERNAME = os.environ.get('GITLAB_USERNAME')
        print(f'GITLAB_USERNAME found, username = {USERNAME}.\n')

    # Check or get api_token
    print('Checking if token environmental variable exists...')
    if os.environ.get('GITLAB_TOKEN') == '':
        print('No environmental variable found for GITLAB_TOKEN.\n')
        API_TOKEN = getpass.getpass('Please enter your token: ')
    else:
        print('Environmental variable found!\n')
        API_TOKEN = os.environ.get('GITLAB_TOKEN')
        # Returns the authenticated session to use in the api caller
        auth_session = auth_session_call(USERNAME, API_TOKEN)

    # Start program with the api caller
    api_caller(GITLAB_API, auth_session)
    return
