import requests
import json

from urllib.parse import urljoin
from requests.exceptions import HTTPError

class GitLab(object):
    """
            GitLab Session Blueprint
    """

    def __init__(self, USERNAME, API_TOKEN):
        self.session = requests.Session()
        self.username = USERNAME
        self.api_token = API_TOKEN
        self.session.headers.update({'Private-Token': f'{self.api_token}'})

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
        """Deletes a single or multiple repositories given the name of the
        repository.
        """
        pass

    def list_groups(self, url):
        """Lists all groups for authenticated user."""

        return self.session.get(url), url

    def list_repo_owned(self, url):
        """Lists all repositories owned."""
        resp = self.session.get(url)
        if resp == None:
            print('You don\'t own any repositories.')
            return resp, url
        else:
            return self.session.get(url), url

    def list_repo_groups(self, url):
        """Lists all repositories from a group."""

        return self.session.get(url), url
