import setuptools
import textwrap
import getpass
import sys

from github.start import start_github
from gitlab.start import start_gitlab


def exit_program():
    """Simply exits the program."""

    print('Exiting program!')
    sys.exit()


def main():
    """Starts chosen git API caller"""

    option = None
    while option != 0:
        print("Hello and welcome to PyGitWeave!")
        print("To get started, please select one of the following options to use GitHub or GitLab.\n\
              0. Exit Program\n\
              1. GitHub\n\
              2. GitLab\n")
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


if __name__ == '__main__':
    main()
