import requests
import json

from urllib.parse import urljoin
from requests.exceptions import HTTPError

class GitHub:
    """
            GitHub Session Blueprint
    """

    def __init__(self, USERNAME, **kwargs):
        self.username = USERNAME
        if 'PASSWORD' in kwargs:
            self.api_token = ''
            self.password = kwargs['PASSWORD']
        elif 'API_TOKEN' in kwargs:
            self.password = ''
            self.api_token = kwargs['API_TOKEN']
        self.session = requests.Session()
        self.session.headers['Authorization'] = f'token {self.api_token}'

    def print_session(self):
        """Create dict from object and return key, val in dict."""

        session_info = {
            "Username": self.username,
            "Password":self.password,
            "Token":self.api_token,
            "Headers": self.session.headers
        }
        for key, val in session_info.items():
            print(f'{key}: {val}')
        print()

    def create_repo(self, url):
        """Creates repository given the payload information."""

        private = None

        print('Please enter the required data for the repository:\n')
        name = input('Enter the name of the repository: ')
        description = input('\nEnter the description for this repository: ')

        # Structures input to use True or False given the string from the user
        while private is not (True or False):
            private = input("\nEnter True for Private or False for Public: ")
            print()
            if private.lower() == 'true' or private.lower() == 't':
                private = True
                break
            elif private.lower() == 'false' or private.lower() == 'f':
                private = False
                break
            else:
                print('Error in input, please try again.')

        payload = {
            "name": name,
            "description": description,
            "private": private,
            "has_issues": False,
            "has_projects": False,
            "has_wiki": True
        }

        return self.session.post(url, data=json.dumps(payload)), url

    def delete_repo(self, url):
        """Deletes repository given the repository name."""

        deleted_repo = 0

        print('Please enter the name of the repository to delete.')
        print('If no directory is entered, you will be redirected back to the choices prompt')
        print('For multiple repositories, use a command in between each name.')
        print('Example: repo1,repo2 OR repo1, repo2')

        # Build a list of repositories from user input
        try:
            repo_list = list(map(str, input("Input: ").split(',')))
            for name in repo_list:
                counter = 0
                if name == '':
                    raise ValueError
                else:
                    counter += 1
        except ValueError:
            print(f'No repository entered at index: {counter}, redirecting to choices prompt.')
            return
        else:
            # Loop through repo_list, strip whitespace and build url
            for name in repo_list:
                name.strip()
                url = url + '/' + self.username + '/' + name
                print(f'\nURL: {url}')

                # Check if repository exists by receiving status code == 404
                try:
                    print(f'Checking if repository {name} exists...\n')
                    response = self.session.get(url)
                    response.raise_for_status()
                except HTTPError as err:
                    print(err)
                    if response.status_code == 404:
                        print(f'Repository {name} doesn\'t exist, skipping!')
                else:
                    print(f'\nDeleting repository, {name}...')
                    self.session.delete(url)
                    deleted_repo += 1
        finally:
            if deleted_repo > 0:
                print('\nSuccessfully deleted all repositories!')
            else:
                print('\nNo repositories were deleted, returning to prompt.')
                return

    def list_repos(self, url):
        """Lists all repositories for a user's GitHub account."""

        return self.session.get(url), url
