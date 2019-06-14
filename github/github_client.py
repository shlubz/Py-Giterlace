import requests
import json

from urllib.parse import urljoin


class GitHub:
    """
            GitHub Session Blueprint
    """

    def __init__(self, username, api_token):
        self.username = username
        self.api_token = api_token
        self.session = requests.Session()
        self.session.headers['Authorization'] = f'token {api_token}'

    def print_session(self):
        """Create dict from object and return key, val in dict."""

        session_info = {
            "Username": self.username,
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

        print('Please enter the name of the repository to delete.')
        print('If no directory is entered, you will be redirected back to the choices prompt')
        print('For multiple repositories, use a command in between each name.')
        print('Example: repo1,repo2 OR repo1, repo2')

        try:
            repo_list = list(map(str, input("Input: ").split(',')))
            for name in repo_list:
                counter = 0
                if name == '':
                    raise ValueError
                else:
                    counter += 1
        except ValueError:
            print(f'No repository entered at index-{counter}, redirecting to choices prompt.')
            return
        else:
            for name in repo_list:
                name.strip()
                url = url + '/' + self.username + '/' + name
                print(f'URL: {url}')
                try:
                    print(f'Checking if repository {name} exists...')
                    self.session.delete(url)
                except HTTPError as http_err:
                    print(f'URL: {url}')
                    print(f'HTTP error occurred: {http_err}\n')
                except Exception as err:
                    print(f'URL: {url}')
                    print(f'A non-HTTP error has occurred: {err}\n')
                else:
                    print(f'\nDeleting repository, {name}...')

        print('\nSuccessfully deleted all repositories!')

    def list_repos(self, url):
        """Lists all repositories for a user's GitHub account."""

        return self.session.get(url), url
