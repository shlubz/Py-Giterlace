# -*- coding: utf-8 -*-
"""Py-Giterlace/github/client.py

This module is used to build an authenticated session to GitHub using method of
authentication by the user.

An object is instantiated from the caller.py module with the constructor.

Current functions:
    print_session()  - Takes no arugments and outputs infomation from the session
                       headers.

    create_repo(url) - Takes a url for argument and returns the POST request to
                       the url and the url to be used in variables.

    delete_repo(url) - Takes a url for argument and returns POST request(s) to
                       delete the repository request, can also delete multiple
                       repositories using a comma ',' between each of the repo
                       names.  It also returns the url to be used in variables.

    list_repo(url)   - Takes a url for argument and returns the GET request to the
                       url and the url to be used in variables.
"""

import requests
import json

from urllib.parse import urljoin
from requests.exceptions import HTTPError

class GitHub(object):
    """
            GitHub Session Blueprint
    """

    def __init__(self, username, **kwargs):
        self.session = requests.Session()
        self.username = username
        if 'password' in kwargs:
            self.api_token = ''
            self.password = kwargs['password']
            self.session.auth = (self.username, self.password)

        elif 'api_token' in kwargs:
            self.password = ''
            self.api_token = kwargs['api_token']
            self.session.headers['Authorization'] = f'token {self.api_token}'

    def print_session(self):
        """Create dict from object and return key, val in dict."""

        session_info = {"Headers": self.session.headers}

        for key, val in session_info.items():
            print(f'{key}: {val}')

    def create_repo(self, url):
        """Creates repository given the payload information."""

        private = None

        print('Please enter the required data for the repository:\n')
        name = input('Enter the name of the repository: ')
        description = input('\nEnter the description for this repository: ')

        # Structures input to use True or False given the string from the user
        while private is not (True or False):
            private = input("\nEnter True for Private or False for Public: ")

            if private.lower() == 'true' or private.lower() == 't':
                private = True
                break

            elif private.lower() == 'false' or private.lower() == 'f':
                private = False
                break

            else:
                print('\nError in input, please try again.')

        # Add ability to change payload data
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

        else:
            # Loop through repo_list, strip whitespace and build url
            for name in repo_list:
                new_url = url + '/' + self.username + '/' + name.strip()
                print(f'\nURL: {new_url}')

                # Check if repository exists by receiving status code == 404
                try:
                    print(f'Checking if repository {name} exists...\n')
                    response = self.session.get(new_url)
                    response.raise_for_status()

                except HTTPError as err:
                    print(err)
                    if response.status_code == 404:
                        print(f'Repository {name} doesn\'t exist, skipping!')

                    else:
                        print(f'\nDeleting repository, {name}...')
                        self.session.delete(new_url)
                        deleted_repo += 1
        finally:
            # Output depending on if any repositories were deleted
            if deleted_repo > 0:
                print('\nSuccessfully deleted all repositories!')

            else:
                print('\nNo repositories were deleted, returning to prompt.')

        return

    def list_repos(self, url):
        """Lists all repositories for a user's GitHub account."""

        return self.session.get(url), url
