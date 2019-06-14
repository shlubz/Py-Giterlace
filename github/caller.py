import requests
import json
import sys

from github.client import GitHub
from urllib.parse import urljoin
from requests.exceptions import HTTPError


def response_loop(response_dicts, option):
    """Loops through a given dictionary and one layer of nested dictionaries.

    Loop path is dependent on the option passed as argument using if/elif.
    Recursive function with option-based pathing would better approach.
    """

    # Matching strings for response output, can be modified
    str_match_repo_resp = ["name", "private", "login", "id", "description",
                           "fork", "url", "html_url", "created_at",
                           "updated_at", "pushed_at"]
    print()

    def create_repo_loop(str_match_repo_resp):
        """Loop for formatting response data output for rep creation."""

        # If option is create_repo
        for k1, v1 in response_dicts.items():
            for list_item in str_match_repo_resp:
                if list_item == k1:
                    if isinstance(v1, dict):
                        for k2, v2 in v1.items():
                            print(f'{k2}: {v2}')
                    else:
                        print(f'{list_item}: {v1}')
        print()

    def list_repo_loop(str_match_repo_resp):
        """Loop for formatting response data output in listing repos."""

        for i in response_dicts:
            for k in str_match_repo_resp:
                for key, val in i.items():
                    if k == key:
                        if isinstance(val, dict):
                            for key2, val2 in val.items():
                                print(f'{key2}: {val2}')
                        else:
                            print(f'{k}: {val}')
            print()

    # Option determines which loop function to call
    if option == 1:
        create_repo_loop(str_match_repo_resp)
    elif option == 3:
        list_repo_loop(str_match_repo_resp)
    else:
        pass


def api_caller(GITHUB_API, auth_session):
    """Little switcharoo that calls the class function based on user option input.
    """
    def switch_exit():
        print('Exiting program!')
        sys.exit()

    def one():
        # Call create_repo class function
        return auth_session.create_repo(urljoin(GITHUB_API, 'user/repos'))

    def two():
        # Call delete_repo class function
        return auth_session.delete_repo(urljoin(GITHUB_API, 'repos'))

    def three():
        # Call list_repo class function
        return auth_session.list_repos(urljoin(GITHUB_API, 'user/repos'))

    def switcharoo(arg):
        # Returns function based on option argument
        switch_options = {
            0: switch_exit,
            1: one,
            2: two,
            3: three
        }
        func = switch_options.get(arg)
        return func()

    # Input options for user, if option eq 0 then exit loop
    option = None
    while option != 0:
        print("Please type in the number of an option to interact with Github's API:\n\
              0. Exit Program\n\
              1. Create Repository\n\
              2. Delete Repository\n\
              3. List Repositories\n")

        while True:
            try:
                option = int(input('Option: '))
                # Check if invalid option was selected
                if option > 3 or option < 0:
                    raise ValueError
            except ValueError:
                print('Invalid selection in response, please try again.')
            else:
                try:
                    # Get response based on option selected
                    if option == 0 or option == 2:
                        switcharoo(option)
                        break
                    else:
                        response, url = switcharoo(option)

                        # If response was successful, No Exception is raised
                        response.raise_for_status()

                except HTTPError as http_err:
                    print(f'URL: {url}')
                    print(f'HTTP error occurred: {http_err}\n')
                except Exception as err:
                    print(f'URL: {url}')
                    print(f'A non-HTTP error has occurred: {err}\n')
                else:
                    print(f'URL: {url}')
                    print('Connection successful!')
                    # Send response in JSON format to output loop
                    response_loop(response.json(), option)
                break
