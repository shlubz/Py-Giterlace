import requests
import json
import sys

from gitlab.respformat import response_loop
from gitlab.client import GitLab
from requests.exceptions import HTTPError


def api_caller(GITLAB_API, auth_session):
    """Calls the class function based on user option input passed through a
    switch.
    """

    def return_to_main():
        print('Returning to main menu!')
        return

    def one():
        # Call create_repo class function
        return auth_session.create_repo(GITLAB_API + '/projects')

    def two():
        # Call delete_repo class function
        return auth_session.delete_repo(GITLAB_API + '/projects')

    def three():
        # Call list_groups class function
        return auth_session.list_groups(GITLAB_API + '/groups')

    def four():
        # Call list_repo_owned class function
        return auth_session.list_repo_owned(GITLAB_API + f'/users/{auth_session.username}/projects')

    def five():
        group_name = input("Please enter a group name: ")
        # Call list_repo_groups class function
        return auth_session.list_repo_groups(GITLAB_API + f'/groups/{group_name}')

    def function_switcher(option):
        # Returns function based on option argument
        switch_options = {
            0: return_to_main,
            1: one,
            2: two,
            3: three,
            4: four,
            5: five
        }
        func = switch_options.get(option)
        return func()

    # Input options for user, if option eq 0 then exit loop
    option = None
    while option != 0:
        print("Please type in the number of an option to interact with GitLab's API:\n\
              0. Return to main menu\n\
              1. Create repository\n\
              2. Delete repository\n\
              3. List groups\n\
              4. List all repositories owned \n\
              5. List all repositories from a group\n")

        while True:
            try:
                option = int(input('Option: '))
                # Check if invalid option was used
                if option > 5 or option < 0:
                    raise ValueError
            except ValueError:
                print('Invalid selection in reponse, please try again.')
            else:
                try:
                    # Get response based on option selected
                    if option == 0 or option == 2:
                        function_switcher(option)
                        break
                    else:
                        response, url = function_switcher(option)

                        # If response was successful, No Exception is raise
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
                    # Output response
                    response_loop(response.json(), option)
                break
