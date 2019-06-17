import requests
import json

from urllib.parse import urljoin
from requests.exceptions import HTTPError

class GitLab:
    """
            GitLab Session Blueprint
    """

    def __init__(self, API_TOKEN):
        self.session = requests.Session()
        self.username = USERNAME
        self.api_token = API_TOKEN
        self.session.headers['Authorization'] == f'Private-Token {self.api_token}'

    def print_session(self):
        """Create dict from object and return key, val in dict."""

        session_info = {
            "Headers": self.session.headers
        }
        for key, val in session_info.items():
            print(f'{key}: {val}')
        print()

    def create_repo(self, url):
        """Creates repository given the payload information."""
        pass

    def delete_repo(self, url):
        pass

    def list_repo(self, url):
        """Lists all repositories for a user's GitLab account."""

        return self.session.get(url), url
