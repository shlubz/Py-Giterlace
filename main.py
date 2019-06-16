import getpass
import sys
import os

from github.client import GitHub
from github.caller import api_caller


def exit_program():
    print('Exiting program!')
    sys.exit()


def start_github():
    print('Starting GitHub client!')
    GITHUB_API = 'https://api.github.com'

    def auth_session_call():
        pass

    if os.environ.get('GITHUB_USERNAME') == '':
        print('No environmental variable found for GITHUB_USERNAME')
        USERNAME = input('\nWhat is your github username? ')
    else:
        USERNAME = os.environ.get('GITHUB_USERNAME')
        print(f'GITHUB_USERNAME found, username = {USERNAME}.')
    while True:
        try:
            p_or_t = input('Please enter p for password or t for token: ')
            print(p_or_t)
            if p_or_t.lower() in ['p', 't', 'true', 'false']:
                pass
            else:
                raise ValueError
        except ValueError:
            print('Invalid selection in response, please try again.')
        else:
            # Check for password or token option
            if p_or_t.lower() == 'p':
                print('Checking if password environmental variables exists...')
                if os.environ.get('GITHUB_PASSWORD') == '':
                    print('No environmental variable found or GITHUB_PASSWORD')
                    PASSWORD = getpass.getpass('Please enter your password: ')
                    # Creates an authentication session object with given
                    # username and password
                    auth_session = GitHub(USERNAME, PASSWORD)
                    auth_session.print_session()

                    # Start program with the api caller
                    api_caller(GITHUB_API, auth_session)
                else:
                    print('Environmental variable found!')
                    PASSWORD = os.environ.get('GITHUB_PASSWORD')
                    # Creates an authentication session object with given
                    # username and password
                    auth_session = GitHub(USERNAME, PASSWORD)
                    auth_session.print_session()

                    # Start program with the api caller
                    api_caller(GITHUB_API, auth_session)
            else:
                print('Token it is, checking if token environmental\
                      variable exists...')
                if os.environ.get('GITHUB_TOKEN') == '':
                    print('No environment variable found for GITHUB_TOKEN')
                else:
                    API_TOKEN = os.environ.get('GITHUB_TOKEN')

                    # Creates an authentication session object with given
                    # username and token
                    auth_session = GitHub(USERNAME, API_TOKEN=API_TOKEN)
                    auth_session.print_session()

                    # Start program with the api caller
                    api_caller(GITHUB_API, auth_session)


def start_gitlab():
    print('Starting GitLab client!')


if __name__ == '__main__':
    option = None
    while option != 0:
        print("Hello and welcome to PyGit-HubLab!")
        print('To get started, please select one of the following options to use\
              GitHub or GitLab.\n\
              1. GitHub\n\
              2. GitLab\n')
        while True:
            try:
                option = int(input('Option: '))
                # Check if invalid option was selected
                if option > 2 or option < 0:
                    raise ValueError
            except ValueError:
                print('Invalid selection in response, please  try again.')
            else:
                # Get response based on option selected
                if option == 0:
                    exit_program()
                elif option == 1:
                    start_github()
                elif option == 2:
                    start_gitlab()
